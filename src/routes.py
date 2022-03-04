from app import app
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime, timedelta
from stocks_service import stocks_service
from services.user_service import user_service
from services.market_service import market_service

ELISA = stocks_service.read_file("elisa.csv")
FINNAIR = stocks_service.read_file("fia1s.csv")
FORTUM = stocks_service.read_file("fortum.csv")
KONE = stocks_service.read_file("knebv.csv")
METSO = stocks_service.read_file("metso.csv")
NESTE = stocks_service.read_file("neste.csv")
NOKIA = stocks_service.read_file("nokia.csv")
NORDEA = stocks_service.read_file("nda.csv")
ORNB = stocks_service.read_file("orionb.csv")
SAMPO = stocks_service.read_file("sampo.csv")
UPM = stocks_service.read_file("upm.csv")
WARTSILA = stocks_service.read_file("wartsila.csv")

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

@app.route("/", methods=["GET"])
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

@app.route("/", methods=["GET", "POST"])
def handle_home():
    stats= market_service.get_stats()
    
    return render_template("index.html", stats=stats)

@app.route("/register", methods=["POST"])
def handle_register():
    username = request.form.get("username")
    password = request.form.get("password")
    password_confirmation = request.form.get("password_confirmation")

    check_if_user = user_service.check_username(username)
    if check_if_user is not None:
        return render_template("register.html", error = "Username already taken")

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

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

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

# end page, shows complete stats
@app.route("/game_over", methods=["GET", "POST"])
def handle_game_over():
    owner = session["username"]
    portfolio = market_service.find_portfolio_name(owner)
    portfolio_id = market_service.find_portfolio_id(owner)

# count value of remaining stocks, buy _price of remaining stocks, balance
# rem 0 company, rem 1 amount, rem 2 buy_price

    endvalue = 0
    invested = 0
    
    remaining = market_service.find_remaining_stocks(portfolio_id)
    last_prices = stocks_service.last_day()
    
    for rem in remaining:
        for price in last_prices:
            if rem[0]==price:
                print(price) #company
                print(last_prices[price]) #price 30.12.
                endvalue += rem[1]*last_prices[price]
                invested += rem[1]*rem[2]
                print(rem[1])
                print(rem[0])
                print(rem[2])
    print(endvalue)
    print(invested)
    portfolio_balance = endvalue-invested

# count dividends for remaining stocks, spaghetti, refactor
    divs_from_remaining = 0
    div20 = stocks_service.dividends_2020()
    div21 = stocks_service.dividends_2021()

    for div in div20:
        for rem in remaining:
            if div==rem[1]:
                if rem[3] < div20[div][0]:
                    divs_from_remaining += div20[div][1] * rem[2]
    for div in div21:
        if div==rem[1]:
            if rem[3] < div21[div][0]:
                divs_from_remaining += div21[div][1] * rem[2]
    
    print(divs_from_remaining)

# count rest of the stats

    transactions = market_service.find_transactions(portfolio_id)

    sales_balance = 0
    dividends = 0
    banking = 0
    result = 0
    taxes = 0
    bought = 0
    sold = 0

    for transaction in transactions:
        sales_balance += transaction[7]
        dividends += transaction[6]
        banking += transaction[5]
        bought += transaction[3]
        sold += transaction[4]
    
    taxable = sales_balance + dividends - banking

    if taxable > 0:
        result = taxable*0.7
        taxes = taxable - result
    else:
        result = taxable*-1
    
    final = portfolio_balance+result
    expenses = bought + banking
    investment_stat = int(expenses)

    percent = (((expenses+portfolio_balance+result)/expenses)-1)*100

    


# format to show results
    endvalue = "{:.2f}".format(endvalue)
    portfolio_balance = "{:.2f}".format(portfolio_balance)
    sales_balance = "{:.2f}".format(sales_balance)
    dividends = "{:.2f}".format(dividends)
    bought = "{:.2f}".format(bought)
    sold = "{:.2f}".format(sold)
    taxes = "{:.2f}".format(taxes)
    result = "{:.2f}".format(result)
    final = "{:.2f}".format(final)
    percent = "{:.2f}".format(percent)

#create stats
    result = float(percent)
    market_service.create_stat(portfolio, owner, investment_stat, result)

    return render_template("game_over.html", portfolio=portfolio, endvalue=endvalue, transactions=transactions, portfolio_balance=portfolio_balance, sales_balance=sales_balance, dividends=dividends, banking=banking, bought=bought, sold=sold, taxes=taxes, result=result, final=final, percent=percent)
            

@app.route("/give_date", methods=["GET", "POST"])
def render_give_date():
    owner = session["username"]
    if not market_service.check_portfolio(owner):
        return render_template("portfolio.html", error = "You don't have a portfolio. Please create one.")
    return render_template("give_date.html")

@app.route("/choose_stock", methods=["GET","POST"])
def handle_choose_stock():

    date_given = request.form["date"]
    if not date_given:
        return render_template("give_date.html", error = "Please give a date.")
        
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

        results.append(stocks_service.give_values("Elisa", date, ELISA))
        results.append(stocks_service.give_values("Finnair", date, FINNAIR))
        results.append(stocks_service.give_values("Fortum", date, FORTUM))
        results.append(stocks_service.give_values("Kone", date, KONE))
        results.append(stocks_service.give_values("Metso", date, METSO))
        results.append(stocks_service.give_values("Neste", date, NESTE))
        results.append(stocks_service.give_values("Nokia", date, NOKIA))
        results.append(stocks_service.give_values("Nordea", date, NORDEA))
        results.append(stocks_service.give_values("Orion B", date, ORNB))
        results.append(stocks_service.give_values("Sampo", date, SAMPO))
        results.append(stocks_service.give_values("UPM", date, UPM))
        results.append(stocks_service.give_values("Wärtsilä", date, WARTSILA))

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
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)

    if request.form["submit_button"] == "Buy":
        amount = request.form.get("amount")
        if not amount:
            market_service.delete_sold_stocks()
            return render_template("give_date.html", error = "Amount was missing.")

        intamount = int(amount)
        if intamount > 0:
            market_service.buy(amount)
            market_service.add_transaction(date, company, float(price)*intamount, 0, 7, 0, 0, portfolio_id)
            
            return redirect_to_portfolio()
        else:
            market_service.delete_sold_stocks()
            return render_template("give_date.html", error = "Amount should be at least 1.")

    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)

    return render_template("buying.html", company=company, date=date, price=price)
    

@app.route("/selling/<company>/<date>/<price>", methods=["GET"])
def render_selling(company, date, price):    
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)
    sellable_stocks = market_service.get_sellable_stocks(company, portfolio_id)
    max = len(sellable_stocks)
    if max == 0:
        message = "You have no stocks from this company. You can return to your portfolio by clicking the Finish sale button."
    else:
        message = f"You have {max} batches to sell. If you give a larger amount, all will be sold."
             
    return render_template("selling.html", company=company, date=date, price=price, sellable_stocks=sellable_stocks, max=max, message=message)

@app.route("/selling/<company>/<date>/<price>", methods=["GET","POST"])
def handle_selling(company, date, price):
    
    print("handling sale")
    
    owner = session["username"]
    portfolio_id = market_service.find_portfolio_id(owner)
    sellable_stocks = market_service.get_sellable_stocks(company, portfolio_id)
    batches = len(sellable_stocks)
    div20 = stocks_service.dividends_2020()
    div21 = stocks_service.dividends_2021()
    divs = 0
    tsold_date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    sold_date = datetime.date(tsold_date)

    if request.form["submit_button"] == "Submit":
        number = request.form.get("number")
        if not number:
            return render_template("give_date.html", error = "Number of batches was missing.")
       
        to_be_sold = int(number)
        if to_be_sold <= 0:
            return render_template("give_date.html", error = "Number of batches was too small.")
        if to_be_sold > batches:
            to_be_sold = batches

        i=0
        while i<to_be_sold:
            market_service.sell(sellable_stocks[i][2], date, price, sellable_stocks[i][0])
            sales_price = float(price)*(sellable_stocks[i][2])
            acq_price = sellable_stocks[i][5]*sellable_stocks[i][2]
            win_loss = sales_price-acq_price
            for div in div20:
                if div==sellable_stocks[i][1]:
                    if sellable_stocks[i][3] < div20[div][0] < sold_date:
                        divs += div20[div][1] * sellable_stocks[i][2]
            for div in div21:
                if div==sellable_stocks[i][1]:
                    if sellable_stocks[i][3] < div21[div][0] < sold_date:
                        divs += div21[div][1] * sellable_stocks[i][2]

            market_service.add_transaction(date, company, 0, sales_price, 7, divs, win_loss, sellable_stocks[i][7])
            i += 1
        return render_template("selling.html", company=company, date=date, price=price, batches=batches)

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
        market_service.add_transaction(date, "company", 0, 0, 0, 0, 0, portfolio_id)
        return redirect_to_portfolio()