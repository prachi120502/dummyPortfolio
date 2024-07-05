import mysql.connector as connector
import PySimpleGUI as sg
from userPageGUI import userPage;

def login():


    con = connector.connect(host='localhost',
            port='3306',
            user='root',
            password='mySql@123',
            database='project1');

    cur = con.cursor(buffered = True);
    


    layout2 = [
        [sg.Text("Enter email/username:",size = (20,1)) , sg.Input(key='-email-')],
        [sg.Text("Enter password:" , size = (20 , 1)) , sg.Input(key='password')],
        [sg.Button('OK')],
        [sg.Text("OR")],
        [sg.Text("New User?") , sg.Button("Sign Up")]
    ];

    window2 = sg.Window('LoginPage' , layout2 , size = (400,400));

    while True:
        event , values = window2.read();

        if event == 'OK':
            print('Hello' + values['-email-']);
            email = values['-email-'];
            password = values['password'];


            query = "select email from user_info";
            cur.execute(query);
            emailRecords = cur.fetchall();

            found = 0;
            for emails in emailRecords:
                if(emails[0] == email):
                    found = 1;

            if(found == 0):
                window2['-email-'].update('Invalid email! Enter again.');
                window2['password'].update('');
                continue;
            else:
                query = "select password from user_info where email ='{}'".format(email);
                cur.execute(query);
                passwordRecord = cur.fetchall();

                print("Here");

                attempts = 0;#no of attempts

                for passwords in passwordRecord:
                    if(passwords[0] != password):
                        window2['password'].update('Invalid Password! Enter again.');
                        attempts += 1;
                        if(attempts > 3):
                            break;
                        else:
                          continue;
                    else:
                        print("Succesfully logged in.");
                        window2.close();
                        userPage(email,password);

        if(event == 'Sign Up'):
            print("New user");

            signUp();

            




        if event == sg.WINDOW_CLOSED:
            break;