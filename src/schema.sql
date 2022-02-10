CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT NOTNULL
);

CREATE TABLE stocks (
    id SERIAL PRIMARY KEY,
    company TEXT,
    amount INTEGER,
    buy_date TEXT,
    sell_date TEXT,
    buy_price FLOAT,
    sell_price FLOAT
);

CREATE TABLE portfolios (
    id SERIAL PRIMARY KEY,
    username TEXT,
    date TEXT,
    name TEXT,
    stock_id INTEGER REFERENCES stocks
);
