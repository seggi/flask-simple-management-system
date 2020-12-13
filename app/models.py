import datetime

from flask_login import UserMixin
from sqlalchemy import Column, Integer, DateTime, Boolean, String, Float, Text,\
    ForeignKey
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy import create_engine


from . import db


# engine = create_engine("mysql://root:@127.0.0.1/nk-account")
# Session = sessionmaker(bind=engine)
# session = Session()

class NkRegister(UserMixin, db.Model):
    __tablename__='nk_register'
    id = Column('id', Integer, primary_key=True)
    name =  Column(String(100), unique=True, nullable=False)
    username =  Column(String(20), unique=True,  nullable=False)
    password_hash =  Column(String(100), unique=True, nullable=False)
    is_admin = Column(Boolean())
    is_public = Column(Boolean())
    created_date = Column(DateTime(timezone=True), default=func.now())
    # physical_product = db.relationship('nk_physical_product.id', lazy='joined')
    # virtual_product = db.relationship('nk_virtual_product.id', lazy='joined')
    
    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)



# defautl

class NkLaguage(db.Model):
    __tablename__='nk_laguages'
    id = Column('id', Integer, primary_key=True)
    name = Column(String(200), unique=True, nullable=False)

class NkLaguageContent(db.Model):
    __tablename__='nk_laguage_content'
    id = Column('id', Integer, primary_key=True)
    contentbody = Column(Text())

class NkCurrencyType(db.Model):
    __tablename__='nk_currency'
    id = Column('id', Integer, primary_key=True)
    currency_type = Column(String(10), nullable=True)
    


# Session Admin 

class NkPhysicalProduct(db.Model):
    __tablename__='nk_physical_product'
    id = Column('id', Integer, primary_key=True)
    product_name = Column(String(500), unique=True, nullable=False)
    description = Column(Text())
    unit_price = Column(Float())
    tot_price = Column(Float())
    quantity = Column(Integer, nullable=False)
    currency = Column(Integer, ForeignKey('nk_currency.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())

    currency_id = db.relationship("NkCurrencyType", backref="currencies")

    # physical_product = db.relationship("NkCurrencyType",lazy="select",
    #         backref=db.backref("currencies", lazy="joined",))
    
    # currency_id = relationship("NkCurrencyType", back_populates="physical_product")
   

    def __repr__(self):
        return '<User %r>' % self.product_name

    

class NkVirtualProduct(db.Model):
    __tablename__='nk_virtual_product'
    id = Column('id', Integer, primary_key=True)
    product_name = Column(String(500), unique=True, nullable=False)
    description = Column(Text())
    quantity = Column(Integer, nullable=False)
    value = Column(Float())
    currency= Column(Integer, ForeignKey('nk_currency.id'),nullable=False)
    admin_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username  


class NkExpenses(db.Model):
    __tablename__='nk_expenses'
    id = Column('id', Integer, primary_key=True)
    description = Column(Text())
    amount = Column(Float())
    admin_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())

class NkEmployee(db.Model):
    __tablename__='nk_employee'
    id =  Column('id', Integer, primary_key=True)
    name =  Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    gender = Column(String(10))
    address = Column(String(200))
    contacts = Column(String(200))
    salary = Column(Float())
    currency_id = Column(Integer, ForeignKey('nk_currency.id'), nullable=False)
    admin_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())

# Employee User

class NkSellPhysicalProduct(db.Model):
    __tablename__='nk_sellphysical_product'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    physical_product = Column(Integer, ForeignKey('nk_physical_product.id'), nullable=False)
    description = Column(Text())
    montant = Column(Float())
    sold_quantity = Column(Integer)
    currency_type = Column(Integer, ForeignKey('nk_currency.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())
    itemid = Column(String(500))
    client = Column(String(500))

class NkSellVirtualProduct(db.Model):
    __tablename__='nk_sellvirtual_product'
    id = Column('id', Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('nk_register.id'), nullable=False)
    virtual_product = Column(Integer, ForeignKey('nk_virtual_product.id'), nullable=False)
    description = Column(Text())
    sold_montant = Column(Float())
    remaining_value = Column(Float())
    currency_type = Column(Integer, ForeignKey('nk_currency.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())
    

class NkRepport(db.Model):
    __tablename__='nk_repport'
    id = Column('id', Integer, primary_key=True)
    description = Column(Text())
    debit = Column(Float())
    credit = Column(Float())
    currency_type = Column(Integer, ForeignKey('nk_currency.id'), nullable=False)
    date = Column(DateTime(timezone=True), default=func.now())
    




