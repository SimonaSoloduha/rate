import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

url_privat = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rate.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class ExchangeRate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow, unique=True)
    AZN = db.Column(db.Float)
    BYN = db.Column(db.Float)
    CAD = db.Column(db.Float)
    CHF = db.Column(db.Float)
    CNY = db.Column(db.Float)
    CZK = db.Column(db.Float)
    DKK = db.Column(db.Float)
    EUR = db.Column(db.Float)
    GBP = db.Column(db.Float)
    GEL = db.Column(db.Float)
    HUF = db.Column(db.Float)
    ILS = db.Column(db.Float)
    JPY = db.Column(db.Float)
    KZT = db.Column(db.Float)
    MDL = db.Column(db.Float)
    NOK = db.Column(db.Float)
    PLZ = db.Column(db.Float)
    RUB = db.Column(db.Float)
    SEK = db.Column(db.Float)
    SGD = db.Column(db.Float)
    TMT = db.Column(db.Float)
    TRY = db.Column(db.Float)
    UAH = db.Column(db.Float)
    USD = db.Column(db.Float)
    UZS = db.Column(db.Float)

    def __repr__(self):
        return f"<exchangerate {self.id}>"


from get_data_from_url import get_data, get_dates_from_db, add_dates_to_db

all_exchenge = ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'HUF', 'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLZ',
       'RUB', 'SEK', 'SGD', 'TMT', 'TRY', 'UAH', 'USD', 'UZS', 'GEL']


@app.route('/exchengerate_info/', methods=['GET', 'POST'])
def exchengerate_info():
    if request.method == "POST":
        users_data = request.form['users_data']
        if users_data is '':
            message = 'Введите дату'
            return render_template('index.html', message=message)
        date_for_url = f'{users_data[-2:]}.{users_data[-5:-3]}.{users_data[:4]}'
        exchengerate_dict = get_data(date_for_url)

        return render_template('exchengerate.html', exchengerate_dict=exchengerate_dict, users_data=users_data)


@app.route('/exchengerate_info_for_dates/', methods=['GET', 'POST'])
def exchengerate_info_for_dates():
    if request.method == "POST":
        users_data_start = request.form['users_data_start']
        users_data_end = request.form['users_data_end']
        if users_data_start is '' or users_data_end is '':
            message = 'Введите две даты'
            return render_template('index.html', message=message)
        exchenges_for_filter = []
        for exchenge in all_exchenge:
            if request.form.get(exchenge):
                exchenges_for_filter.append(exchenge)
        add_dates_to_db(users_data_start, users_data_end)
        result = get_dates_from_db(users_data_start, users_data_end, exchenges_for_filter)

        return render_template('exchengerate_dates.html', result=result, users_data_start=users_data_start,
                               users_data_end=users_data_end)


@app.route('/')
def index():
    return render_template('index.html', all_exchenge=all_exchenge)

