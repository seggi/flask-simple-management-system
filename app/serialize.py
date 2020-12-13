from marshmallow import Schema, fields, post_load , ValidationError

from . models import NkPhysicalProduct, NkRegister, NkCurrencyType
from . import ma

def must_not_be_blank(data):
    if not data:
        raise ValidationError('Data not provided')


class NkRegisterSchame(Schema):
    id = fields.Int(dump_only=True)
    name =  fields.Str()
    username =  fields.Str()
    password_hash =  fields.Str()
    is_admin = fields.Bool()
    is_public = fields.Bool()
    created_date = fields.DateTime(dump_only=True)

class NkCurrencyTypeSchema(Schema):
    id = ma.auto_field()
    currency_type = ma.auto_field()
    currencies = ma.auto_field()

    # id = fields.Int(dump_only=True)
    # currency_type = fields.Str()
    # physical_product= fields.Nested('NkPhysicalProductSchema', many=True, exclude=('currency', ))


class NkPhysicalProductSchema(Schema):
    id = fields.Int(dump_only=True)
    product_name = fields.String(required=True, validate=must_not_be_blank)
    description = fields.String(required=True, validate=must_not_be_blank)
    unit_price = fields.Float(required=True, validate=must_not_be_blank)
    tot_price = fields.Float(required=True, validate=must_not_be_blank)
    quantity = fields.Int(required=True, validate=must_not_be_blank)
    currency = fields.Nested(NkCurrencyTypeSchema(), only=['id', 'currency_type'], validate=must_not_be_blank)
    admin_id = fields.Nested(NkRegisterSchame, validate=must_not_be_blank)
    date = fields.DateTime(dump_only=True)
    


    

nk_registration_schema = NkRegisterSchame(many=True)
nk_currency_schema = NkCurrencyTypeSchema(many=True,)
nk_physicalproduct_schema = NkPhysicalProductSchema()
nk_physicalproducts_schema = NkPhysicalProductSchema(many=True)

