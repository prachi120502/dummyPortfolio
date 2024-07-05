# from email import message
import PySimpleGUI as sg;
import mysql.connector as connector;
from buySharesGUI import buyShares;


def userPage(email,password):

    con = connector.connect(host='localhost',
            port='3306',
            user='root',
            password='mySql@123',
            database='project1');

    cur = con.cursor(buffered = True);


    #getting fname and lname corresponding to the email
    query = "select fname,lname from user_info where email = '{}'".format(email);

    cur.execute(query);
    nameRecords = cur.fetchall();


    for name in nameRecords:
        fname = name[0];
        lname = name[1];

    print(fname +" " + lname);

    #getting portfolio companies corresponding to the email
    queryForPortfolioCompanies = "select company_name from portfolio where email = '{}'".format(email);
    cur.execute(queryForPortfolioCompanies);
    portfolioCompaniesRecords = cur.fetchall();

    portfolioCompaniesUser = [];
    for portfollioCompany in portfolioCompaniesRecords:
        company = portfollioCompany[0];
        portfolioCompaniesUser.append(company);
        print(company);

    portfolioCompaniesUserLtp = [];
    for company in portfolioCompaniesUser:
        queryForLtp = "select ltp from stock_info where company_name = '{}'".format(company);
        cur.execute(queryForLtp);
        ltp = cur.fetchall();

        for lastPrice in ltp:
            portfolioCompaniesUserLtp.append(lastPrice[0]);
            print(lastPrice);


    userQty = [] ;
    userBuyPrice = [];
    for company in portfolioCompaniesUser:
        query = "select buy_price , Qty from portfolio where email = '{}' AND company_name = '{}'".format(email,company);
        cur.execute(query);

        infoRecord = cur.fetchall();

        for row in infoRecord:
            userQty.append(row[1]);
            userBuyPrice.append(row[0]);







    #for the message to be displayed on the GUI
    noOfCompaniesInPortfolio = len(portfolioCompaniesRecords);
    if(len(portfolioCompaniesRecords) == 0):
        print("Empty portfolio!");
        message = "EMPTY PORTFOLIO!";
    else:
        message = str(noOfCompaniesInPortfolio) + " companies currently in your portfolio.";

    i = 1;
    totalInvestedAmt = 0;
    currentValue = 0;
    for company in portfolioCompaniesUser:
        print(company);
        print(portfolioCompaniesUserLtp[i - 1]);
        print(userBuyPrice[i - 1]);
        print(userQty[i - 1]);
        totalInvestedAmt += (userBuyPrice[i - 1] * userQty[i - 1]);
        currentValue += (portfolioCompaniesUserLtp[i - 1] *  userQty[i - 1]);
        i+=1;
        print("end");