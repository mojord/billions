from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from stocks_service import stocks_service
from services.user_service import user_service
from services.market_service import market_service

NORDEA = stocks_service.read_file("nda.csv")
NOKIA = stocks_service.read_file("nokia.csv")
FINNAIR = stocks_service.read_file("fia1s.csv")
KONE = stocks_service.read_file("knebv.csv")
NESTE = stocks_service.read_file("neste.csv")

def redirect_to_register():
    return redirect(url_for("render_register"))

def redirect_to_login():
    return redirect(url_for("render_login"))

def redirect_to_home():
    return redirect(url_for("render_home"))

def redirect_to_choose_stock():
    return redirect(url_for("render_choose_stock"))

def redirect_to_give_date():
    return redirect(url_for("render_give_date"))

def redirect_to_portfolio():
    return redirect(url_for("render_portfolio"))

def redirect_to_create_portfolio():
    return redirect(url_for("create_portfolio"))

def redirect_to_game_over():
    return redirect(url_for("game_over"))


@app.route("/", methods=["GET", "POST"])
def render_home():
    return render_template("index.html")

@app.route("/register", methods=["GET"])
def render_register():
    return render_template("register.html")

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("login.html")

@app.route("/portfolio", methods=["GET"])
def render_portfolio():
    return render_template("portfolio.html")

@app.route("/create_portfolio", methods=["GET"])
def render_create_portfolio():
    return render_template("create_portfolio.html")

@app.route("/game_over", methods=["GET"])
def render_game_over():
    return render_template("game_over.html")




@app.route("/register", methods=["POST"])
def handle_register():
    print("kutsutaan handle_register")
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")

#    check_if_user = user_repository.find_username(username)

#    if check_if_user is not None:
#        return render_template("register.html", error = "Username already taken")

    if password != password_confirmation:
        return render_template("register.html", error = "Passwords do not match")

    if not (username and password and password_confirmation):
        return render_template("register.html", error = "Fill all fields")
    
    if len(password) < 4:
        return render_template("register.html", error = "Password must be at least 4 characters")

    if len(username) < 3:
        return render_template("register.html", error = "Username must be at least 3 characters")
            
    user_service.create_user(username, password)    
    return redirect_to_login()

@app.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    session["username"] = username
    
    return redirect_to_portfolio()

@app.route("/portfolio", methods=["GET", "POST"])
def handle_portfolio():
    owner = session["username"]

    if market_service.check_portfolio(owner):
        portfolio = market_service.find_portfolio_name(owner)
    else:
        return render_template("portfolio.html", error = "You don't have a portfolio. Please create one.")

    if portfolio is not None:
        portfolio_id = market_service.find_portfolio_id(owner)
        today = market_service.get_latest_transaction(portfolio_id)
        stocks = market_service.find_stocks(portfolio_id)
    
    return render_template("portfolio.html", portfolio=portfolio, today=today, stocks=stocks)

@app.route("/game_over", methods=["GET", "POST"])
def handle_game_over():
    owner = session["username"]
    portfolio = market_service.find_portfolio_name(owner)
    portfolio_id = market_service.find_portfolio_id(owner)

    transactions = market_service.find_transactions(portfolio_id)

    bought = 0
    sold = 0
    banking = 0
    result = 0
    taxes = 0

    for transaction in transactions:
        bought += transaction[3]
        sold += transaction[4]
        banking += transaction[5]
    
    taxable = sold - bought - banking

    if taxable > 0:
        result = taxable*0.7
        taxes = taxable - result
    else:
        result = taxable*-1
    
    return render_template("game_over.html", portfolio=portfolio, transactions=transactions, bought=bought, sold=sold, banking=banking, taxes=taxes, result=result)
            

@app.route("/give_date", methods=["GET", "POST"])
def render_give_date():
    return render_template("give_date.html")

@app.route("/choose_stock", methods=["GET","POST"])
def handle_choose_stock():

    date_given = request.form["date"]
    date = datetime.strptime(date_given, "%d.%m.%Y")
    given_date = datetime.date(date)
    
    end_date = "31.12.2021"
    ending = datetime.strptime(end_date, "%d.%m.%Y")
    end = datetime.date(ending)

    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)
    latest = market_service.get_latest_transaction(portfolio_id)

    print(type(ending))
    print(end)

    print(latest>given_date)

    if latest > given_date:
        return render_template("give_date.html", error = "Game has already passed this date. Please give a later date.")
    
    if given_date > end:
        return render_template("give_date.html", error = "Game ends 31.12.2021.")    
    else:

        results = []

        results.append(stocks_service.give_values("Nordea", date, NORDEA))
        results.append(stocks_service.give_values("Nokia", date, NOKIA))
        results.append(stocks_service.give_values("Finnair", date, FINNAIR))
        results.append(stocks_service.give_values("Kone", date, KONE))
        results.append(stocks_service.give_values("Neste", date, NESTE))

        return render_template("choose_stock.html", items=results)

@app.route("/buying/<company>/<date>/<price>", methods=["GET"])
def render_buying(company, date, price):

    print("render buy page")
    print(company)
    
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)

    market_service.create_stock(company, 0, date, None, price, None, portfolio_id)
                  
    return render_template("buying.html", company=company, date=date, price=price)

@app.route("/buying/<company>/<date>/<price>", methods=["GET","POST"])
def handle_buying(company, date, price):
    
    print("handling buy")

    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)

    if request.form["submit_button"] == "Buy":
        amount = request.form.get("amount")
        market_service.buy(amount)
        market_service.add_transaction(date, company, float(price)*int(amount), 0, 7, 0, portfolio_id)
        
        return redirect_to_portfolio()

    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)

    return render_template("buying.html", company=company, date=date, price=price)
    

@app.route("/selling/<company>/<date>/<price>", methods=["GET"])
def render_selling(company, date, price):

    print("sale page")
    
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)
    sellable_stocks = market_service.get_sellable_stocks(company, portfolio_id)
             
    return render_template("selling.html", company=company, date=date, price=price, sellable_stocks=sellable_stocks)

@app.route("/selling/<company>/<date>/<price>", methods=["GET","POST"])
def handle_selling(company, date, price):
    
    print("handling sale")
    
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)
    sellable_stocks = market_service.get_sellable_stocks(company, portfolio_id)


    if request.form["submit_button"] == "Submit":
        print("submitting number")
        number = request.form.get("number")
        batches = int(number)
        print("number")
        print(number)
        i=0
        while i<batches:
            market_service.sell(sellable_stocks[i][2], date, price, sellable_stocks[i][0])
            print(sellable_stocks[i][2], date, price, sellable_stocks[i][0])
            print(type(price))
            print(type(sellable_stocks[i][2]))
            market_service.add_transaction(date, company, 0, float(price)*(sellable_stocks[i][2]), 7, 0, sellable_stocks[i][7])
            i += 1
        return render_template("selling.html", company=company, date=date, price=price)

    else:
        if request.form["submit_button"] == "Click to finish sale":
            market_service.delete_sold_stocks()
            return redirect_to_portfolio()
    
    return render_template("selling.html", company=company, date=date, price=price)


@app.route("/create_portfolio", methods=["GET", "POST"])
def create_portfolio():
    owner = session["username"]
    name = request.form.get("portfolio_name")
    date = "01.01.2020"
    if market_service.check_portfolio(owner):
        return render_template("portfolio.html", error = "You already have a portfolio.")
    else:
        market_service.create_portfolio(owner, date, name)
        portfolio_id = market_service.find_portfolio_id(owner)
        market_service.add_transaction(date, "", 0, 0, 0, 0, portfolio_id)
        return redirect_to_portfolio()