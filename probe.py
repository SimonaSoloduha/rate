users_data = '1999-06-02'
date_for_url = f'{users_data[-2:]}.{users_data[-5:-3]}.{users_data[:4]}'
print(date_for_url)

# import requests
# import datetime
# from app import db, ExchangeRate, get_data, url_privat
#
#
# data = db.session.query(ExchangeRate).all()[-1]
# print(type(data.date), data.date)
# # query = db.session.query(ExchangeRate.date)
# # for row in query:
# #     print(row._asdict())
#
# employee_data = get_data(url_privat)
# new_data = employee_data['date']
# print(type(new_data), new_data)
#
# exists = db.session.query(ExchangeRate.id).filter_by(id=new_data).scalar() is None
# if exists == False:
#     print('tytytyt')
#
# print(exists)
