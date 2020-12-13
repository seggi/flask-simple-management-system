# sqlite connction
import sqlite3
from . import mysqldb as mysql

sqliteconn = sqlite3.connect('nk-account.sqlite')

# mysql connection

mysqlconn = mysql.connect()