# -*- coding: utf-8 -*-
# bot.py
import os
import logging
import configparser 
import sys
import xlsxwriter
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

def main(argv):
    greetings()

    app = Flask(__name__)
    configure_logging(app)

    db = init_database(app)
    scheduler = BlockingScheduler()
    config = configparser.ConfigParser()
    config.read('/tmp/bot/settings/config.ini')

    var1 = int(config.get('scheduler', 'IntervalInMinutes'))
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(var1))

    task1_instance = scheduler.add_job(task1, 'interval', id='task1_job', minutes=var1, args=[db])

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass

def configure_logging(app):
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

def init_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:123mudar@127.0.0.1:5432/bot_db'
    return SQLAlchemy(app)

def greetings():
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')

def task1(db):
    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(os.path.curdir, file_name)
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    orders = db.session.execute('SELECT * FROM users;')

    index = 1

    headers = ['Id', 'Name', 'Email', 'Password', 'Role Id', 'Created At', 'Updated At']
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    for order in orders:
        index += 1
        for col, value in enumerate(order):
            worksheet.write(index, col, value)

    workbook.close()
    print('Job executed!')

if __name__ == '__main__':
    main(sys.argv)
