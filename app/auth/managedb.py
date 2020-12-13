# from app.dbs import sqliteconn as mysqlconn
from app.dbs import mysqlconn

# Login session

class AdminLoginPage:
    def __init__(self, username, password, conn=mysqlconn.cursor()):
        self.username = username
        self.password = password
        self.cursor = conn

    def sendRequest(self):
        self.cursor.execute("""SELECT id, username, password_hash FROM nk_register
         WHERE username = %s AND password_hash = %s""", (self.username, self.password))
        self.cursor.commit()
        columns = [desc[0] for desc in self.cursor.description]
        rowdicts = []
        for row in self.cursor.fetchall():
            newdict = {}
            for col, val in zip(columns, row):
                newdict[col] =  val
            rowdicts.append(newdict)
        for row in rowdicts: return row
    
