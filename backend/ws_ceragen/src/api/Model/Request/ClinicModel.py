from datetime import datetime
from typing import Optional
from .BaseModel import BaseModel

class BloodType(BaseModel):
    def __init__(self):
        super().__init__()
        self.btp_id: Optional[int] = None
        self.btp_type: Optional[str] = None
        self.btp_description: Optional[str] = None

class AllergyCatalog(BaseModel):
    def __init__(self):
        super().__init__()
        self.al_id: Optional[int] = None
        self.al_name: Optional[str] = None
        self.al_description: Optional[str] = None

class DiseaseType(BaseModel):
    def __init__(self):
        super().__init__()
        self.dst_id: Optional[int] = None
        self.dst_name: Optional[str] = None
        self.dst_description: Optional[str] = None

class DiseaseCatalog(BaseModel):
    def __init__(self):
        super().__init__()
        self.dis_id: Optional[int] = None
        self.dis_name: Optional[str] = None
        self.dis_description: Optional[str] = None
        self.dis_type_id: Optional[int] = None

class PatientAllergy(BaseModel):
    def __init__(self):
        super().__init__()
        self.pa_id: Optional[int] = None
        self.pa_patient_id: Optional[int] = None
        self.pa_allergy_id: Optional[int] = None
        self.pa_reaction_description: Optional[str] = None

class PatientDisease(BaseModel):
    def __init__(self):
        super().__init__()
        self.pd_id: Optional[int] = None
        self.pd_patient_id: Optional[int] = None
        self.pd_disease_id: Optional[int] = None
        self.pd_is_current: bool = True
        self.pd_notes: Optional[str] = None

class PatientMedicalHistory(BaseModel):
    def __init__(self):
        super().__init__()
        self.hist_id: Optional[int] = None
        self.hist_patient_id: Optional[int] = None
        self.hist_primary_complaint: Optional[str] = None
        self.hist_onset_date: Optional[datetime] = None
        self.hist_related_trauma: Optional[bool] = None
        self.hist_current_treatment: Optional[str] = None
        self.hist_notes: Optional[str] = None

class SessionControl(BaseModel):
    def __init__(self):
        super().__init__()
        self.sec_id: Optional[int] = None
        self.sec_inv_id: Optional[int] = None
        self.sec_pro_id: Optional[int] = None
        self.sec_ses_number: Optional[int] = None
        self.sec_ses_agend_date: Optional[datetime] = None
        self.sec_ses_exec_date: Optional[datetime] = None
        self.sec_typ_id: Optional[int] = None
        self.sec_med_staff_id: Optional[int] = None
        self.ses_consumed: bool = False
        self.ses_state: bool = True

class ConsentRecord(BaseModel):
    def __init__(self):
        super().__init__()
        self.con_id: Optional[int] = None
        self.con_patient_id: Optional[int] = None
        self.con_type: Optional[str] = None
        self.con_signed_by: Optional[str] = None
        self.con_signed_date: Optional[datetime] = None
        self.con_relationship: Optional[str] = None
        self.con_notes: Optional[str] = None