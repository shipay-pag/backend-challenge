# -*- coding: utf-8 -*-
import os, sys, traceback, logging, configparser
import xlsxwriter
from datetime import datetime, timedelta, timezone
from apscheduler.schedulers.blocking import BlockingScheduler
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler
from sqlalchemy import text


def main(argv):
    greetings()

    print('Press Crtl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))

    app = Flask(__name__)
    handler = RotatingFileHandler('bot.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/shipay'

    db = SQLAlchemy(app)

    config = configparser.ConfigParser()
    config.read('settings/config.ini')

    var1 = int(config.get('scheduler','IntervalInMinutes'))
    app.logger.warning('Intervalo entre as execucoes do processo: {}'.format(var1))
    scheduler = BlockingScheduler()

    task1_instance = scheduler.add_job(task1, 'interval', id='task1_job', minutes=var1, args=[app, db])

    try:
        scheduler.start()
    except(KeyboardInterrupt, SystemExit):
        pass

def greetings():
    print('             ##########################')
    print('             # - ACME - Tasks Robot - #')
    print('             # - v 1.0 - 2020-07-28 - #')
    print('             ##########################')


def task1(app, db):
    with app.app_context():
        file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
        file_path = os.path.join(os.path.curdir, file_name)
        workbook = xlsxwriter.Workbook(file_path)
        worksheet = workbook.add_worksheet()

        query = text('SELECT * FROM users')
        orders = db.session.execute(query)

        index = 1

        column_names = ['ID', 'Name', 'Email', 'Password', 'Role Id', 'Created At', 'Updated At']
        for i, column_name in enumerate(column_names):
            cell = '{0}{1}'.format(chr(65 + i), index)
            worksheet.write(cell, column_name)

        for index, order in enumerate(orders, start=2):
            print('--------------------NEW ROW--------------------------')
            for i, value in enumerate(order):
                cell = '{0}{1}'.format(chr(65 + i), index)
                worksheet.write(cell, value)
                print('{0}: {1}'.format(column_names[i], value))
            print('--------------------END ROW---------------------------')
            print('--------------------xxxxxxx---------------------------')

        workbook.close()
        print('job executed!')

def task2(db):
    file_name = 'data_export_{0}.xlsx'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    file_path = os.path.join(os.path.curdir, file_name)
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()

    qs = text('SELECT * FROM users WHERE id = :user_id')
    orders = db.session.execute(qs, {'user_id': 30})

    orders = db.session.execute('SELECT * FROM users;')

    index = 1

    worksheet.write('A{0}'.format(index),'Id')
    worksheet.write('B{0}'.format(index),'Name')
    worksheet.write('C{0}'.format(index),'Email')
    worksheet.write('D{0}'.format(index),'Password')
    worksheet.write('E{0}'.format(index),'Role Id')
    worksheet.write('F{0}'.format(index),'Created At')
    worksheet.write('G{0}'.format(index),'Updated At')

    for order in orders:
        index = index + 1

        print('Id: {0}'.format(order[0]))
        worksheet.write('A{0}'.format(index),order[0])
        print('Name: {0}'.format(order[1]))
        worksheet.write('B{0}'.format(index),order[1])
        print('Email: {0}'.format(order[2]))
        worksheet.write('C{0}'.format(index),order[2])
        print('Password: {0}'.format(order[3]))
        worksheet.write('D{0}'.format(index),order[3])
        print('Role Id: {0}'.format(order[4]))
        worksheet.write('E{0}'.format(index),order[4])
        print('Created At: {0}'.format(order[5]))
        worksheet.write('F{0}'.format(index),order[5])
        print('Updated At: {0}'.format(order[6]))
        worksheet.write('G{0}'.format(index),order[6])

    workbook.close()
    print('job executed!')

if __name__ == '__main__':
    main(sys.argv)
