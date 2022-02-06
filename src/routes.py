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
    
    return redirect_to_portfolio()

@app.route("/portfolio", methods=["GET", "POST"])
def portfolio():
    return redirect_to_give_date()

@app.route("/give_date", methods=["GET", "POST"])
def render_give_date():
    return render_template("give_date.html")


@app.route("/choose_stock", methods=["GET","POST"])
def handle_choose_stock():
    date_given = request.form["date"]
    date = datetime.strptime(date_given, "%d.%m.%Y")
    results = []

    results.append(stocks_service.give_values("Nordea", date, NORDEA))
    results.append(stocks_service.give_values("Nokia", date, NOKIA))
    results.append(stocks_service.give_values("Finnair", date, FINNAIR))
    results.append(stocks_service.give_values("Kone", date, KONE))
    results.append(stocks_service.give_values("Neste", date, NESTE))

    return render_template("choose_stock.html", items=results)

@app.route("/result<company>", methods=["GET","POST"])
def render_result(company):
    market_service.create_stock(company, None, None, None, None, None)
         
    
    return render_template("result.html")

