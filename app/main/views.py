from datetime import datetime, date


from flask import render_template, session, redirect, url_for, escape, request
from flask_login import login_required, current_user 
from flask import jsonify, make_response
# from sqlalchemy.orm import joinedload, sessionmaker
# from sqlalchemy import create_engine


import json


from . import main 
from .. import db    
from ..models import *
# from ..serialize import *
from app.main.managedb import (getProduct, getcurrency, selectProducttoUpdate, 
        updateProduct, insertProduct,  insertWorker, getWorker, selectWorktoUpdate, updateWorker, 
        removeWorker, inserSoldItem, getSoldItem, getSelSoldItem, updateStock, getRemainStock, 
        getAllExpenses, getEmployee, getSelEmployee, insertExpenses, getTodayExpenses, 
        updateEmployeeSalary, getCashBookTot, getCashBook, insertCashBook)

# from .forms import LoginForm

main.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# ----------------------------------------------------------

now = datetime.datetime.utcnow()
strnow = now.strftime('%Y-%m-%d %H:%M:%S')

# Add Product in DB session

@main.route('/admin', methods=['GET', 'POST'])
@login_required
def adminHome():
   
    context = {
        "currency": getcurrency,
    }
    return render_template('src/admin/adminHome.html', name=current_user.name, context=context)


@main.route('/api/save_physical_product/', methods=['GET','POST'])
@login_required
def addPhysicalProduct():
    admin_id = current_user.id
    displayproduct = getProduct()

    if request.method == 'POST' and 'addphysicalproduct-hidden-form' in request.form:
        print(displayproduct)
        return jsonify({'datas': displayproduct})
    
    # Recod un product 
    if request.method == "POST" and 'physical_product' in request.form: 
        product_name = request.form['product_name']
        description_name = request.form['product_designation']
        unit_price = request.form["unit_price"]
        tot_price = request.form["tot_price"]
        quantity =  request.form["quantity"]
        currency_id = request.form["currency_id"]

        if product_name != None and description_name !=None and unit_price != None\
            and tot_price != None and quantity != None and currency_id:
            get_product_name = NkPhysicalProduct.query.filter_by(product_name=product_name).first()
            if get_product_name:
                return jsonify({'error':"Product name all ready exists", 'datas': displayproduct})
            else:
                displayinserted = insertProduct(product_name, description_name, unit_price, tot_price,quantity, admin_id, strnow, currency_id)
                return jsonify({'datas': displayinserted})
            return jsonify({'datas': displayproduct})

        else: 
            return jsonify(error="You must complete all field,\nor check currency field if you forget to fill it!")
        return jsonify({'datas': displayproduct})

    # Send Request to update product
    elif request.method == 'POST' and "edit-product" in request.form:
        product_id = request.form['edit-product']

        if product_id != None:
            return jsonify(datas=selectProducttoUpdate(id=product_id))

    # Update product 
    elif request.method == 'POST' and "edit_physical_product" in request.form:
        product_id = request.form['edit_physical_product']
        product_name = request.form['product_name_edt']
        description_name = request.form['product_designation_edt']
        unit_price = request.form["unit_price_edt"]
        tot_price = request.form["tot_price_edt"]
        quantity =  request.form["quantity_edt"]
        currency_id = request.form["currencies_id_edt"]
        # id_currencies = request.form["id_currencies"]

        if product_name != None and description_name !=None and unit_price != None\
            and tot_price != None and quantity != None and currency_id != None :
           
            displayupdate = updateProduct(product_name, description_name, float(unit_price), 
                float(tot_price), int(quantity), currency_id, int(product_id))
            return jsonify({'datas': displayupdate})
        else:
            return jsonify({'error': 'Currency must be specify'  ,'datas': displayproduct})
        # return jsonify({'datas': displayproduct})

    return redirect(url_for("main.adminHome"))
    

# Record Work
@main.route('/api/record_worker/', methods=['GET','POST'])
@login_required
def recordWorker():
    admin_id = current_user.id
    displayworker = getWorker()

    # Display Worker
    if request.method == "POST" and "recordworker-hidden-form" in request.form:
        if len(displayworker) > 0:
            return jsonify({"datas": displayworker})
        return jsonify({"error": "No data to show, please record data first then click 'Display'. "})

    # Record worker
    if request.method == "POST" and "record_worker" in request.form:
        worker_name = request.form['worker_name']
        worker_lastname =  request.form['worker_lastname']
        age =  request.form['age']
        sex = request.form.get('sex')
        salary = request.form['salary']
        currency = request.form.get('currency_id')
        contacts = request.form['contact']
        address = request.form['address']
    
        if worker_name != None and worker_lastname != None and age != None and sex != None\
            and salary != None and currency != None and contacts != None and address != None:
            get_worker_name = NkEmployee.query.filter_by(name=worker_lastname, lastname=worker_lastname).first()
            if get_worker_name:
                return jsonify({'error':"Worker all ready exists", 'datas': displayworker})
            else:
                displayworkerinserted = insertWorker(worker_name, worker_lastname, sex, address, admin_id, 
                strnow, contacts, salary, currency )
                return jsonify({'datas': displayworkerinserted})

        return jsonify({'datas':displayworker })

    # Send request to get worker id

    if request.method == "POST" and "get-worker-hidden" in request.form:
        worker_id = request.form['get-worker-hidden']

        if worker_id != None:
            return jsonify(datas=selectWorktoUpdate(id=worker_id))

    # Update worker

    if request.method == "POST" and "record_worker_updated" in request.form:
        
        worker_id = request.form['record_worker_updated']
        worker_name = request.form['worker_name_edt']
        worker_lastname =  request.form['worker_lastname_edt']
        # age =  request.form['age_edt']
        sex = request.form.get('sex_edt')
        salary = request.form['salary_edt']
        currency = request.form['currency_id_edt1']

        contacts = request.form['contact_edt']
        address = request.form['address_edt']
        
        # print(worker_name , worker_lastname , sex , salary , currency , contacts , address)
        
    
        if worker_name != None and worker_lastname != None and sex != None\
            and salary != None and currency != None and contacts != None and address != None:
    
            displayworkerupdated = updateWorker(worker_name, worker_lastname, sex, address,
             contacts, salary, currency, worker_id)
            return jsonify({'datas': displayworkerupdated})
        else:
            return jsonify(error="You must complete all field,\nor check currency field if you forget to fill it!")
        
        return jsonify({"datas": displayworker})

    if request.method == "POST" and "remove_worker" in request.form:
        worker_id = request.form['remove_worker']
        
        displayworkerremain = removeWorker(worker_id)
        return jsonify({'datas': displayworkerremain})


    return redirect(url_for("main.adminHome"))

# Live Search
@main.route('/api/live_search/', methods=['GET','POST'])
@login_required
def liveSearch():
    admin_id = current_user.id
    # searchbox = request.get_json('text')
    # result = searchProductItems(searchbox['text'])
    today = date.today()
    if request.method == "POST" and "hidden-search-id" in request.form:
        product_id = request.form.get('hidden-search-id')

        if product_id != None:
            displayproductget = selectProducttoUpdate(product_id)
            displayproducthisto = getSelSoldItem(product_id)
            if len(displayproducthisto):
                return jsonify(datas=displayproductget, datas1=displayproducthisto)
            return jsonify({'error': 'Nothing to show!'})
        else:
            return jsonify(error='Please enter something in search field!')
        

    if request.method == "POST" and "product-to-sell_id" in request.form:
        soldproduct_id = request.form.get("product-to-sell_id")
        soldquantity = request.form.get("sold-quantity")
        clientname = request.form.get('client-name')
        currency_id = request.form.get('currency_type')
        productvalue = request.form.get('productvalue')

        if soldproduct_id != None and currency_id != None\
            and productvalue  != None and soldproduct_id != '':

            if soldquantity != None and soldquantity != '':
                createitemid = "#"+str(today)+str(soldproduct_id)
                amount = float(productvalue) * int(soldquantity)
                getitemstock = getRemainStock(soldproduct_id)

                if int(getitemstock[0]['quantity']) > int(soldquantity):
                    designations = "product_id_"+soldproduct_id
                    computestock = int(getitemstock[0]['quantity']) - int(soldquantity)
                    updateStock(computestock, soldproduct_id)

                    insertCashBook(designations, amount, 0, currency_id, strnow)

                    displaysoldproduct = inserSoldItem(admin_id, soldproduct_id, amount,
                    soldquantity, currency_id, strnow, clientname, createitemid)
                    getcurrentstock = selectProducttoUpdate(soldproduct_id)
                    
                    return jsonify(datas=displaysoldproduct, datas1=getcurrentstock)
                return jsonify({"error": "The quantity entrered can't be servered!"})
            return jsonify({'error': 'Please enter quantity!'})
            
        else:
            return jsonify({'error':'Please search product name first!'})

    if request.method =="POST" and "get-sold-product" in request.form:
        displayallsold = getSoldItem()
        if len(displayallsold) > 0:
            return jsonify(datas=displayallsold)
        else:
            return jsonify({'error': 'Nothing to show'})

    getproduct = getProduct()
    return jsonify(getproduct)


# Expens session

@main.route('/api/expenses/', methods=['GET','POST'])
@login_required
def manageExpenses():
    admin_id = current_user.id  

    if request.method == "POST" and "get-all-expenses-form" in request.form:
        if len(getAllExpenses()) > 0:
            return jsonify(datas=getAllExpenses())
        else:
            return jsonify({'error': "Nothing to show!"})
    
    getemplyee = getEmployee()
    return jsonify(getemplyee)

@main.route('/api/expenses/payment/', methods=['GET','POST'])
@login_required
def employeeLiveSearch():
    admin_id = current_user.id 
    # today = date.today()

    if request.method == "POST" and "hidden-esearch-id" in request.form:
        employee_id = request.form.get('hidden-esearch-id')
        employeesalary = request.form.get('hdn-employeesalary')
        employeepayment = request.form.get('employee-amount')
        designation = request.form.get('designation')
        fullname = request.form.get('hdn-employeefullname')
        currency_type = request.form.get("currency_type")

        # print(employee_id, employeesalary, employeepayment, designation, fullname)
        
        if employee_id != None and employee_id != '' and employeesalary != None and employeesalary != ''\
            and employeepayment != None and employeepayment != '' and designation != '' and designation != None\
                and fullname != None and fullname != '':

            if float(employeepayment) < float(employeesalary):
                paydayadvance = fullname+" payday advance \n"+designation 
                insertCashBook(paydayadvance, 0, employeepayment, currency_type, strnow)
                displaytodayexpense = insertExpenses(paydayadvance, employeepayment, admin_id, strnow, today=now.strftime('%Y-%m-%d'))
                # getupdatedsalary = updateEmployeeSalary(calulation, employee_id)
                return jsonify(datas=displaytodayexpense)

            elif  float(employeepayment) == float(employeesalary):
                salarydesignation = fullname+" salary \n"+designation
                # calulation = float(employeesalary) - float(employeepayment)
                # getupdatedsalary = updateEmployeeSalary(calulation, employee_id)
                insertCashBook(paydayadvance, 0, employeepayment, currency_type, strnow)
                displaytodayexpense = insertExpenses(salarydesignation, employeepayment, 
                                admin_id, strnow, today=now.strftime('%Y-%m-%d'))
                return jsonify(datas=displaytodayexpense)

            else:
                return jsonify({'error': 'The amount entred is superior to His salary'})
               
        else:
            return jsonify({'error': "You have to specify the name first."})

    if request.method == "POST" and "record_otherexpenses" in request.form:
        otherexpensesamount = request.form.get("eamount")
        otherexpensesdesignation = request.form.get("edesignation")

        print(otherexpensesamount, otherexpensesdesignation)

        if otherexpensesamount != None and otherexpensesamount != "" and \
            otherexpensesdesignation != None and otherexpensesdesignation != "":
            displaytodayexpense = insertExpenses(otherexpensesdesignation, otherexpensesamount, 
                                    admin_id, strnow, today=now.strftime('%Y-%m-%d'))
            return jsonify(datas=displaytodayexpense)

        else:
            return jsonify({'error': 'You must fill all field'})

    getemplyee = getEmployee()
    print(getemplyee)
    return jsonify(getemplyee)

@main.route('/api/cash_book/', methods=['GET','POST'])
@login_required
def cashBook():
    admin_id = current_user.id 

    # if request.method == "POST" and "hidden-cashout-form" in request.form:
    gettotcash = getCashBookTot()
    getallcashdetail = getCashBook()
    print(gettotcash)
    return jsonify(datas=getallcashdetail, datas1=gettotcash)
        
