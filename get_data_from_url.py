import requests
import datetime
from sqlalchemy import exc


from app import db, ExchangeRate


url_privat = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='


def get_data(date_for_url):
    url = url_privat + date_for_url
    response = requests.get(url).json()
    exchengerate_dict = {}

    date_str = response['date']
    date = datetime.datetime.strptime(date_str, '%d.%m.%Y').date()
    exchengerate_dict['date'] = date

    exchangerate_data = response['exchangeRate']

    for i in exchangerate_data:
        try:
            exchengerate_dict[i['currency']] = i['saleRateNB']
        except KeyError:
            continue

    add_to_db(exchengerate_dict)

    return exchengerate_dict


def add_dates_to_db(user_date_start, user_date_end):
    dates = []
    date_of_start = datetime.datetime.strptime(user_date_start, '%Y-%m-%d').date()
    date_of_end = datetime.datetime.strptime(user_date_end, '%Y-%m-%d').date()

    while date_of_start <= date_of_end:
        dates.append(datetime.datetime.strftime(date_of_start, '%d.%m.%Y'))
        date_of_start += datetime.timedelta(days=1)

    for data in dates:
        get_data(data)


def add_to_db(exchengerate_dict):
        new_data = exchengerate_dict['date']
        try:
            employee = ExchangeRate(**exchengerate_dict)
            db.session.add(employee)
            db.session.commit()
            massage = f'Добавили дату {new_data} в БД'
            print(massage)

        except exc.IntegrityError:
            db.session.rollback()
            massage = f'Дата {new_data} эта уже есть в БД'
            print(massage)
            db.session.rollback()
        finally:
            db.session.close()


def get_dates_from_db(date_of_start, date_of_end, exchenges_for_filter):
    dates = db.session.query(ExchangeRate).filter(ExchangeRate.date.between(date_of_start, date_of_end))
    resulr = []
    for row in dates:
        info = dict(row.__dict__)
        info.pop('_sa_instance_state', None)
        info.pop('id', None)
        date = info['date']
        info.pop('date', None)
        if exchenges_for_filter != []:
            filter_info = {}
            for exc in exchenges_for_filter:
                filter_info[exc] = info[exc]
            resulr.append({'date': date, 'info': filter_info})
        else:
            resulr.append({'date': date, 'info': info})

    return resulr

