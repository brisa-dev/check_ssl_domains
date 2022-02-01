import ssl
import sys
from socket import *
import os
from datetime import datetime
import json
import mysql.connector
import argparse

class DomainTools:

    def __init__(self):
        self.fullpath = os.path.abspath(os.path.dirname(__file__))

    def get_domains(self):
        try:
            # Split items by '\n'
            data = open(f'{self.fullpath}/../domains.txt', 'r').read().split('\n')
            # Return data with null items removed
            domains_list = []
            [ 
                domains_list.append({
                    'customer' : x.split(';')[0],
                    'domain' : x.split(';')[1]
                }) 
                for x in data if x != '' 
            ]
            return domains_list
        except Exception as err:
            print('Error: {}'.format(str(err)))
            sys.exit(1)

    def get_ssl_info(self):
        try:
            domains = self.get_domains()
            setdefaulttimeout(2)
            domains_status = []
            for item in domains:
                custormer = item['customer']
                domain = item['domain']
                # get SSL certificate data
                try:
                    ctx = ssl.create_default_context()
                    s = ctx.wrap_socket(socket(), server_hostname=domain)
                    s.connect((domain, 443))
                    cert = s.getpeercert()
                    # format date ( notAfter )
                    notAfter = datetime.strptime(cert['notAfter'], '%b  %d %H:%M:%S %Y %Z')
                    domains_status.append({
                        'message' : '',
                        'notAfter' : str(notAfter),
                        'status' : 1,
                        'domain' : domain,
                        'customer' : custormer })
                except Exception as ssl_err:
                    domains_status.append({
                        'message' : str(ssl_err),
                        'notAfter' : '',
                        'status' : 0,
                        'domain' : domain,
                        'customer' : custormer })
                    pass
            return domains_status            
        except Exception as err:
            print('Error: {}'.format(str(err)))
            sys.exit(1)

    def insert_data_to_db(self):
        try:
            # Create MySQL connection
            conn = mysql.connector.connect(
                user=os.environ['MYSQL_USER'],
                password=os.environ['MYSQL_PASS'],
                host=os.environ['MYSQL_HOST'],
                database=os.environ['MYSQL_DATABASE']
            )
            conn.autocommit = True
            cursor = conn.cursor()
            for item in self.get_ssl_info():
                domain = item['domain']
                # delete domain if exists
                sql_delete = f'delete from ssl_domains_info where domain="{domain}"'
                cursor.execute(sql_delete)
                # insert data from domain
                custormer = item['customer']
                notAfter = item['notAfter']
                if notAfter != "":
                    notAfter_datetime = datetime.strptime(notAfter, '%Y-%m-%d %H:%M:%S')
                else:
                    notAfter_datetime = datetime.strptime('1111-11-11 00:00:00', '%Y-%m-%d %H:%M:%S')
                status = item['status']
                message = item['message']
                sql_insert = f'insert into ssl_domains_info (customer,domain,notAfter,status,message,date) \
                    values ("{custormer}","{domain}","{notAfter_datetime}",{status},"{message}",now())'
                cursor.execute(sql_insert)
            cursor.close()
            conn.close()
        except mysql.connector.Error as err:
            print(str(err))