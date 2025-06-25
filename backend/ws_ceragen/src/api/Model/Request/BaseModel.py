from datetime import datetime
from typing import Optional, Dict, Any

class BaseModel:
    """Clase base para todos los modelos"""
    
    def __init__(self):
        self.state: bool = True
        self.user_created: Optional[str] = None
        self.date_created: Optional[datetime] = None
        self.user_modified: Optional[str] = None
        self.date_modified: Optional[datetime] = None
        self.user_deleted: Optional[str] = None
        self.date_deleted: Optional[datetime] = None
    
    def to_dict(self) -> Dict[str, Any]:
        """Convierte el modelo a diccionario"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
        return result
    
    def from_dict(self, data: Dict[str, Any]):
        """Carga datos desde diccionario"""
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self
    
    def set_audit_fields(self, user: str, is_create: bool = True):
        """Establece campos de auditoria"""
        if is_create:
            self.user_created = user
            self.date_created = datetime.now()
        else:
            self.user_modified = user
            self.date_modified = datetime.now()
    
    def set_delete_fields(self, user: str):
        """Establece campos de eliminación lógica"""
        self.state = False
        self.user_deleted = user
        self.date_deleted = datetime.now()