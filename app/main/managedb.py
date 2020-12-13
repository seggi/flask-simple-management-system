# from app.dbs import sqliteconn as mysqlconn
from app.dbs import mysqlconn


# Works with python 3.8< 
class Database:
    @staticmethod
    def queryManyDic(querystring=None, conn=mysqlconn):
        cursor = conn.cursor()
        cursor.execute(querystring)
        colnames = [desc[0] for desc in cursor.description]
        rowdicts = []
        for row in cursor.fetchall():
            newdict = {}
            for x, y in zip(colnames, row):
                newdict[x] = y  
            rowdicts.append(newdict)
        return rowdicts
    
    @staticmethod
    def querySelManyDic(querystring=None, tups=None, conn=mysqlconn):
        cursor = conn.cursor()
        cursor.execute(querystring, (tups))
        conn.commit()
        colnames = [desc[0] for desc in cursor.description]
        rowdicts = []
        for row in cursor.fetchall():
            newdict = {}
            for x, y in zip(colnames, row):
                newdict[x] = y  
            rowdicts.append(newdict)
        return rowdicts

    @staticmethod
    def querySelLikeManyDic(querystring=None, tups=None, conn=mysqlconn):
        cursor = conn.cursor()
        cursor.execute(querystring.tups)
        conn.commit()
        colnames = [desc[0] for desc in cursor.description]
        rowdicts = []
        for row in cursor.fetchall():
            newdict = {}
            for x, y in zip(colnames, row):
                newdict[x] = y  
            rowdicts.append(newdict)
        return rowdicts

    @staticmethod
    def queryInsertData(querystring=None, tups=None, conn=mysqlconn):
        cursor = conn.cursor()
        cursor.execute(querystring, tups)
        conn.commit()

    @staticmethod
    def queryDeleteData(querystring=None, tups=None, conn=mysqlconn):
        cursor = conn.cursor()
        cursor.execute(querystring, tups)
        conn.commit()







def selectProducttoUpdate(id):
    getselected = Database.querySelManyDic("""
        SELECT nk_physical_product.id as product_id, nk_physical_product.product_name as product_name, 
        nk_physical_product.description as description, nk_physical_product.unit_price as unit_price, 
        nk_physical_product.tot_price as tot_price, nk_physical_product.quantity as quantity, 
        nk_physical_product.date as date, nk_currency.currency_type, nk_currency.id as currency_id 
        FROM nk_physical_product LEFT JOIN nk_currency
        ON nk_currency.id = nk_physical_product.currency WHERE nk_physical_product.id=%s
        """,id)
    return getselected

def getProduct():
    getproduct = Database.queryManyDic(querystring="""
            SELECT nk_physical_product.id as product_id, nk_physical_product.product_name as product_name, 
            nk_physical_product.description as description, nk_physical_product.unit_price as unit_price, 
            nk_physical_product.tot_price as tot_price, nk_physical_product.quantity as quantity, 
            nk_physical_product.date as date, nk_currency.currency_type, nk_currency.id as currency_id 
            FROM nk_physical_product LEFT JOIN nk_currency
            ON nk_currency.id = nk_physical_product.currency 
            """)
    return getproduct

def updateProduct(*pargs):
    Database.queryInsertData(
        """UPDATE nk_physical_product SET product_name=%s,description=%s, 
        unit_price=%s,tot_price=%s,quantity=%s, currency=%s WHERE nk_physical_product.id=%s""",
        pargs)
    updatedata = getProduct()
    return updatedata

def insertProduct(*pargs):
    Database.queryInsertData( 
        """INSERT INTO nk_physical_product(product_name, description, unit_price,
         tot_price, quantity, admin_id, date, currency) 
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", pargs
    )
    insertdata = getProduct()
    return insertdata



# Worker sesssion

def getWorker():
    getworker = Database.queryManyDic(
        querystring= """
           SELECT nk_employee.id, nk_employee.name, nk_employee.lastname, nk_employee.gender,
           nk_currency.currency_type as currency_type, nk_employee.address, nk_employee.date, 
           nk_employee.contacts,  nk_employee.salary FROM nk_employee 
           LEFT JOIN nk_currency ON nk_currency.id = nk_employee.currency_id
        """
     )
    return getworker

def insertWorker(*pargs):
    Database.queryInsertData(
        """INSERT INTO nk_employee(name, lastname, gender,address, admin_id, date, contacts, salary, currency_id) 
         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    ,pargs)
    insertdata = getWorker()
    return insertdata

def selectWorktoUpdate(id):
    getselected = Database.querySelManyDic(
        """
           SELECT nk_employee.id, nk_employee.name, nk_employee.lastname, nk_employee.gender,
           nk_currency.currency_type as currency_type, nk_employee.address, nk_employee.date, 
           nk_employee.contacts, nk_employee.salary FROM nk_employee 
           LEFT JOIN nk_currency ON nk_currency.id = nk_employee.currency_id WHERE nk_employee.id=%s
        """, id
    )
    return getselected

def updateWorker(*pargs):
    Database.queryInsertData(
        """ UPDATE nk_employee SET name=%s,lastname=%s,gender=%s,address=%s,
        contacts=%s,salary=%s,currency_id=%s WHERE nk_employee.id=%s""", pargs
    )
    updatedata = getWorker()
    return updatedata

def removeWorker(id):
    Database.queryDeleteData(
        """
            DELETE FROM nk_employee WHERE id=%s
        """, id
    )
    remainingwork = getWorker()
    return remainingwork


# Selling Items to be managed
# ++++++++++++++++++++++++++++++++++++++++++++++++++
def searchProductItems(searchproductname):
    getselected = Database.querySelManyDic(
        querystring= """
                SELECT nk_physical_product.product_name, nk_physical_product.description, nk_physical_product,
                nk_physical_product.unit_price, nk_physical_product.quantity, nk_currency.currency_type 
                FROM nk_physical_product LEFT JOIN nk_currency ON nk_currency.id = nk_physical_product.currency
                WHERE nk_physical_product.product_name LIkE '{}%' ORDER BY nk_physical_product.product_name
            """,
        tups=format(searchproductname)
    )
    return getselected
#++++++++++++++++++++++++++++++++++++++++++++++++++
def getSoldItem():
    getproduct = Database.queryManyDic(
        querystring=
        """  
            SELECT  nk_sellphysical_product.description, nk_sellphysical_product.montant, 
            nk_sellphysical_product.sold_quantity, nk_sellphysical_product.date, 
            nk_sellphysical_product.itemid, nk_sellphysical_product.client, 
            nk_sellphysical_product.id as solditemid, nk_physical_product.product_name,
            nk_currency.currency_type as currency
            FROM nk_sellphysical_product 
            LEFT JOIN nk_physical_product ON nk_physical_product.id = nk_sellphysical_product.physical_product
            LEFT JOIN nk_currency ON nk_currency.id = nk_sellphysical_product.currency_type
            ORDER BY nk_sellphysical_product.date
        """
        )
    return getproduct

def getSelSoldItem(id):
    getproduct = Database.querySelManyDic(
        querystring=
        """  
            SELECT  nk_sellphysical_product.description, nk_sellphysical_product.montant, 
            nk_sellphysical_product.sold_quantity, nk_sellphysical_product.date, 
            nk_sellphysical_product.itemid, nk_sellphysical_product.client, 
            nk_sellphysical_product.id as solditemid, nk_physical_product.product_name,
            nk_currency.currency_type as currency
            FROM nk_sellphysical_product 
            LEFT JOIN nk_physical_product ON nk_physical_product.id = nk_sellphysical_product.physical_product
            LEFT JOIN nk_currency ON nk_currency.id = nk_sellphysical_product.currency_type
            WHERE nk_sellphysical_product.physical_product = %s
            ORDER BY nk_sellphysical_product.date
        """, tups=id
        )
    return getproduct

def inserSoldItem(*pargs):
    Database.queryInsertData(
        """
            INSERT INTO `nk_sellphysical_product`(user_id, physical_product,
            montant, sold_quantity, currency_type, date, client, itemid) VALUES (%s,%s,%s,%s,%s,%s,%s, %s)
        """, pargs
    )
    getsolditem = getSelSoldItem(pargs[1])
    print(getsolditem)
    return getsolditem

def getRemainStock(id):
    getstock = Database.querySelManyDic(
        querystring="""
            SELECT quantity FROM nk_physical_product WHERE id = %s
        """, tups=id
    )
    return getstock

def updateStock(*pargs):
    Database.queryInsertData(
        """UPDATE nk_physical_product SET quantity=%s WHERE nk_physical_product.id=%s""",
        pargs)
    updatedata = getSoldItem()
    return updatedata
    

# Stock session

def getAllExpenses():
    getallexpenses = Database.queryManyDic(
        "SELECT * FROM nk_expenses"
    )
    return getallexpenses

def getTodayExpenses(today):
    getallexpenses = Database.querySelManyDic(
        "SELECT * FROM nk_expenses WHERE DATE(date)=%s", today
    )
    return getallexpenses


def getEmployee():
    getallemployee = Database.queryManyDic(
        querystring="""SELECT * FROM nk_employee 
        LEFT JOIN nk_currency ON nk_currency.id = nk_employee.currency_id"""
    )
    return getallemployee

def getSelEmployee(id):
    getemployee = Database.querySelManyDic(
        querystring="SELECT * FROM nk_employee WHERE id=%s",
        tups=id
    )
    return getemployee


def insertExpenses(*pargs, today):
    Database.queryInsertData(
        querystring=
        """
            INSERT INTO nk_expenses(description, amount, admin_id, date) 
            VALUES (%s,%s,%s,%s)
        """, tups=pargs
    )
    gettodaydata = getTodayExpenses(today)
    return gettodaydata

def updateEmployeeSalary(*pargs):
    Database.queryInsertData(
        """UPDATE nk_employee SET salary=%s WHERE nk_employee.id=%s""",
        pargs)
    gettodaydata = getSelEmployee(pargs[1])
    return gettodaydata


# Cash out session

def getCashBookTot():
    getcashbooktot = Database.queryManyDic(
        """
            SELECT SUM(nk_repport.debit) as debit, SUM(nk_repport.credit) as credit,
            nk_currency.currency_type
            FROM nk_repport LEFT JOIN nk_currency ON nk_currency.id = nk_repport.currency_type
        """
    )
    return getcashbooktot

def getCashBook():
    getcashbook = Database.queryManyDic(
        """
            SELECT nk_repport.id, nk_repport.description, nk_repport.debit, nk_repport.credit,
            nk_repport.date,  nk_currency.currency_type 
            FROM nk_repport LEFT JOIN nk_currency ON nk_currency.id = nk_repport.currency_type
            ORDER BY nk_repport.date
        """
    )
    return getcashbook

def insertCashBook(*pargs):
    Database.queryInsertData(
        querystring="""
            INSERT INTO nk_repport(description, debit, credit, currency_type, date) 
            VALUES (%s,%s,%s,%s,%s)
        """, tups=pargs
    )

getcurrency = Database.queryManyDic(querystring="""SELECT * FROM nk_currency""")









