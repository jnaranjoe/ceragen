from datetime import datetime
from typing import Optional, List
from decimal import Decimal
from .BaseModel import BaseModel
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

# class MaritalStatus(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.id: Optional[int] = None
#         self.status_name: Optional[str] = None

# class Person(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.per_id: Optional[int] = None
#         self.per_identification: Optional[str] = None
#         self.per_names: Optional[str] = None
#         self.per_surnames: Optional[str] = None
#         self.per_genre_id: Optional[int] = None
#         self.per_marital_status_id: Optional[int] = None
#         self.per_country: Optional[str] = None
#         self.per_city: Optional[str] = None
#         self.per_address: Optional[str] = None
#         self.per_phone: Optional[str] = None
#         self.per_mail: Optional[str] = None
#         self.per_birth_date: Optional[datetime] = None

# class Client(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.cli_id: Optional[int] = None
#         self.cli_person_id: Optional[int] = None
#         self.cli_identification: Optional[str] = None
#         self.cli_name: Optional[str] = None
#         self.cli_address_bill: Optional[str] = None
#         self.cli_mail_bill: Optional[str] = None

# class Patient(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.pat_id: Optional[int] = None
#         self.pat_person_id: Optional[int] = None
#         self.pat_client_id: Optional[int] = None
#         self.pat_code: Optional[str] = None
#         self.pat_medical_conditions: Optional[str] = None
#         self.pat_allergies: Optional[str] = None
#         self.pat_blood_type: Optional[int] = None
#         self.pat_emergency_contact_name: Optional[str] = None
#         self.pat_emergency_contact_phone: Optional[str] = None

# class MedicPersonType(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.mpt_id: Optional[int] = None
#         self.mpt_name: Optional[str] = None
#         self.mpt_description: Optional[str] = None

# class MedicalStaff(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.med_id: Optional[int] = None
#         self.med_person_id: Optional[int] = None
#         self.med_type_id: Optional[int] = None
#         self.med_registration_number: Optional[str] = None
#         self.med_specialty: Optional[str] = None

# class TherapyType(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.tht_id: Optional[int] = None
#         self.tht_name: Optional[str] = None
#         self.tht_description: Optional[str] = None

# class Product(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.pro_id: Optional[int] = None
#         self.pro_code: Optional[str] = None
#         self.pro_name: Optional[str] = None
#         self.pro_description: Optional[str] = None
#         self.pro_price: Optional[Decimal] = None
#         self.pro_total_sessions: Optional[int] = None
#         self.pro_duration_days: Optional[int] = None
#         self.pro_image_url: Optional[str] = None
#         self.pro_therapy_type_id: Optional[int] = None

# class ProductPromotion(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.ppr_id: Optional[int] = None
#         self.ppr_product_id: Optional[int] = None
#         self.ppr_name: Optional[str] = None
#         self.ppr_description: Optional[str] = None
#         self.ppr_discount_percent: Optional[Decimal] = None
#         self.ppr_extra_sessions: Optional[int] = None
#         self.ppr_start_date: Optional[datetime] = None
#         self.ppr_end_date: Optional[datetime] = None

# class PaymentMethod(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.pme_id: Optional[int] = None
#         self.pme_name: Optional[str] = None
#         self.pme_description: Optional[str] = None
#         self.pme_require_references: bool = False
#         self.pme_require_picture_proff: bool = False

# class ExpenseType(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.ext_id: Optional[int] = None
#         self.ext_name: Optional[str] = None
#         self.ext_description: Optional[str] = None

# class Expense(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.exp_id: Optional[int] = None
#         self.exp_type_id: Optional[int] = None
#         self.exp_payment_method_id: Optional[int] = None
#         self.exp_date: Optional[datetime] = None
#         self.exp_amount: Optional[Decimal] = None
#         self.exp_description: Optional[str] = None
#         self.exp_receipt_number: Optional[str] = None

# class Tax(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.tax_id: Optional[int] = None
#         self.tax_name: Optional[str] = None
#         self.tax_percentage: Optional[Decimal] = None
#         self.tax_description: Optional[str] = None

# class Invoice(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.inv_id: Optional[int] = None
#         self.inv_number: Optional[str] = None
#         self.inv_date: Optional[datetime] = None
#         self.inv_client_id: Optional[int] = None
#         self.inv_patient_id: Optional[int] = None
#         self.inv_subtotal: Optional[Decimal] = None
#         self.inv_discount: Optional[Decimal] = None
#         self.inv_tax: Optional[Decimal] = None
#         self.inv_grand_total: Optional[Decimal] = None

# class InvoiceDetail(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.ind_id: Optional[int] = None
#         self.ind_invoice_id: Optional[int] = None
#         self.ind_product_id: Optional[int] = None
#         self.ind_quantity: Optional[int] = None
#         self.ind_unit_price: Optional[Decimal] = None
#         self.ind_total: Optional[Decimal] = None

# class InvoicePayment(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.inp_id: Optional[int] = None
#         self.inp_invoice_id: Optional[int] = None
#         self.inp_payment_method_id: Optional[int] = None
#         self.inp_amount: Optional[Decimal] = None
#         self.inp_reference: Optional[str] = None
#         self.inp_proof_image_path: Optional[str] = None

# class InvoiceTax(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.int_id: Optional[int] = None
#         self.int_invoice_id: Optional[int] = None
#         self.int_tax_id: Optional[int] = None
#         self.int_tax_amount: Optional[Decimal] = None

# class ParameterList(BaseModel):
#     def __init__(self):
#         super().__init__()
#         self.pli_id: Optional[int] = None
#         self.pli_code_parameter: Optional[str] = None
#         self.pli_is_numeric_return_value: bool = True
#         self.pli_string_value_return: Optional[str] = None
#         self.pli_numeric_value_return: Optional[Decimal] = None