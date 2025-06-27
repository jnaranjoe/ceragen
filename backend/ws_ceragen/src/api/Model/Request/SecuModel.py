from datetime import datetime
from typing import Optional, List
from decimal import Decimal
from marshmallow import Schema, fields


class LoginRequest(Schema):
    login_user = fields.String(required=True)
    login_password = fields.String(required=True)

class PersonGenreReq(Schema):
    person_genre_name = fields.String(required=True)

#==================================================================
# PERSON TABLE
#==================================================================
class PersonReq(Schema):
    per_identification = fields.String(required=True)
    per_names = fields.String(required=True)
    per_surnames = fields.String(required=True)
    per_genre_id = fields.Integer(required=True)
    per_marital_status_id = fields.Integer(required=True)
    per_country = fields.String(required=True)
    per_city = fields.String(required=True)
    per_address = fields.String(required=True)
    per_phone = fields.String(required=True)
    per_mail = fields.String(required=True)
    per_birth_date = fields.String(required=True)
class PersonIdReq(Schema):
    per_id = fields.Integer(required=True)
    per_identification = fields.String(required=True)
    per_names = fields.String(required=True)
    per_surnames = fields.String(required=True)
    per_genre_id = fields.Integer(required=True)
    per_marital_status_id = fields.Integer(required=True)
    per_country = fields.String(required=True)
    per_city = fields.String(required=True)
    per_address = fields.String(required=True)
    per_phone = fields.String(required=True)
    per_mail = fields.String(required=True)
    per_birth_date = fields.String(required=True)
class PersonDeleteReq(Schema):
    per_id = fields.Integer(required=True)
    per_state = fields.Boolean(required=True)
    
#==================================================================
# ROL TABLE
#==================================================================
class RolReq(Schema):
    rol_name = fields.String(required=True)
    rol_description = fields.String(required=True)
    is_admin_rol = fields.Boolean(required=True)
class RolIdReq(Schema):
    rol_id = fields.Integer(required=True)
    rol_name = fields.String(required=True)
    rol_description = fields.String(required=True)
    is_admin_rol = fields.Boolean(required=True)
class RolDeleteReq(Schema):
    rol_id = fields.Integer(required=True)
    rol_state = fields.Boolean(required=True)

#==================================================================
# USER TABLE
#==================================================================
class UserReq(Schema):
    user_person_id = fields.Integer(required=True)
    user_mail = fields.String(required=True)
    user_password = fields.String(required=True)
class UserIdReq(Schema):
    user_id = fields.Integer(required=True)
    user_person_id = fields.Integer(required=True)
    user_mail = fields.String(required=True)
    user_password = fields.String(required=True)
    user_locked = fields.Boolean(required=True)
class UserDeleteReq(Schema):
    user_id = fields.Integer(required=True)
    user_state = fields.Boolean(required=True)

#====================================================================
# User_Rol  
#====================================================================
class UserRolReq(Schema):
    id_user = fields.Integer(required=True)
    id_rol = fields.Integer(required=True)
class UserRolIdReq(Schema):
    id_user_rol = fields.Integer(required=True)
    id_user = fields.Integer(required=True)
    id_rol = fields.Integer(required=True)
class UserRolDeleteReq(Schema):
    id_user_rol = fields.Integer(required=True)
    state = fields.Boolean(required=True)

class SendEmailPasswordReq(Schema):
    user_mail = fields.String(required=True)

class UpdatePasswordSchema(Schema):
    new_password = fields.String(required=True)
    token_temp = fields.String(required=True)
