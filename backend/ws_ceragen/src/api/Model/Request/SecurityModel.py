from datetime import datetime
from typing import Optional
from .BaseModel import BaseModel

class Module(BaseModel):
    def __init__(self):
        super().__init__()
        self.mod_id: Optional[int] = None
        self.mod_name: Optional[str] = None
        self.mod_description: Optional[str] = None
        self.mod_order: Optional[int] = None
        self.mod_icon_name: Optional[str] = None
        self.mod_text_name: Optional[str] = None

class Role(BaseModel):
    def __init__(self):
        super().__init__()
        self.rol_id: Optional[int] = None
        self.rol_name: Optional[str] = None
        self.rol_description: Optional[str] = None
        self.is_admin_rol: bool = False

class Menu(BaseModel):
    def __init__(self):
        super().__init__()
        self.menu_id: Optional[int] = None
        self.menu_name: Optional[str] = None
        self.menu_order: Optional[int] = None
        self.menu_module_id: Optional[int] = None
        self.menu_parent_id: Optional[int] = None
        self.menu_icon_name: Optional[str] = None
        self.menu_href: Optional[str] = None
        self.menu_url: Optional[str] = None
        self.menu_key: Optional[str] = None

class MenuRole(BaseModel):
    def __init__(self):
        super().__init__()
        self.mr_id: Optional[int] = None
        self.mr_menu_id: Optional[int] = None
        self.mr_rol_id: Optional[int] = None

class User(BaseModel):
    def __init__(self):
        super().__init__()
        self.user_id: Optional[int] = None
        self.user_person_id: Optional[int] = None
        self.user_login_id: Optional[str] = None
        self.user_mail: Optional[str] = None
        self.user_password: Optional[str] = None
        self.user_locked: bool = False
        self.user_last_login: Optional[datetime] = None
        self.login_attempts: int = 0
        self.twofa_enabled: bool = False

class UserRole(BaseModel):
    def __init__(self):
        super().__init__()
        self.id_user_rol: Optional[int] = None
        self.id_user: Optional[int] = None
        self.id_rol: Optional[int] = None
        self.state: Optional[bool] = None

class UserNotification(BaseModel):
    def __init__(self):
        super().__init__()
        self.sun_id: Optional[int] = None
        self.sun_user_source_id: Optional[int] = None
        self.sun_user_destination_id: Optional[int] = None
        self.sun_title_notification: Optional[str] = None
        self.sun_text_notification: Optional[str] = None
        self.sun_date_notification: Optional[datetime] = None
        self.sun_state_notification: bool = True
        self.sun_isread_notification: bool = False
        self.sun_date_read_notification: Optional[datetime] = None

class Login(BaseModel):
    def __init__(self):
        super().__init__()
        self.slo_id: Optional[int] = None
        self.slo_user_id: Optional[int] = None
        self.slo_token: Optional[str] = None
        self.slo_origin_ip: Optional[str] = None
        self.slo_host_name: Optional[str] = None
        self.slo_date_start_connection: Optional[datetime] = None
        self.slo_date_end_connection: Optional[datetime] = None