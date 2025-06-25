from datetime import datetime
from typing import Optional
from .BaseModel import BaseModel

class AuditTable(BaseModel):
    def __init__(self):
        super().__init__()
        self.aut_id: Optional[int] = None
        self.aut_table_name: Optional[str] = None
        self.aut_table_descriptiom: Optional[str] = None

class SqlEventsRegister(BaseModel):
    def __init__(self):
        super().__init__()
        self.ser_id: Optional[int] = None
        self.ser_table_id: Optional[int] = None
        self.ser_sql_command_type: Optional[str] = None
        self.ser_new_record_detail: Optional[str] = None
        self.ser_old_record_detail: Optional[str] = None
        self.ser_user_process_id: Optional[int] = None
        self.ser_date_event: Optional[datetime] = None