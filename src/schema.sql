CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT NOT NULL
);

CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    owner TEXT,
    date DATE,
    name TEXT
);

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    company TEXT,
    amount INTEGER,
    buy_date DATE,
    sell_date DATE,
    buy_price FLOAT,
    sell_price FLOAT,
    portfolio_id INTEGER REFERENCES portfolios
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE,
    company TEXT,
    buy_price FLOAT,
    sell_price FLOAT,
    banking FLOAT,
    dividend FLOAT,
    balance FLOAT,
    portfolio_id INTEGER REFERENCES portfolios
);

CREATE TABLE stats (
    id SERIAL PRIMARY KEY,
    portfolio_name TEXT,
    user_name TEXT,
    investment INTEGER,
    result FLOAT
);
