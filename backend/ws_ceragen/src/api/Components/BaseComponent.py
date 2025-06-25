from typing import List, Optional, Dict, Any, Tuple
from ...utils.database.connection_db import DataBaseHandle
import logging

class BaseComponent:
    """Clase base para todos los componentes de acceso a datos"""
    
    def __init__(self, schema: str = "ceragen"):
        self.schema = schema
        self.db = DataBaseHandle()
        self.logger = logging.getLogger(__name__)
    
    def _build_where_clause(self, filters: Dict[str, Any]) -> Tuple[str, List]:
        """Construye la cláusula WHERE y parámetros"""
        if not filters:
            return "", []
        
        conditions = []
        params = []
        
        for key, value in filters.items():
            if value is not None:
                if isinstance(value, str) and '%' in value:
                    conditions.append(f"{key} LIKE %s")
                else:
                    conditions.append(f"{key} = %s")
                params.append(value)
        
        where_clause = " WHERE " + " AND ".join(conditions) if conditions else ""
        return where_clause, params
    
    def _build_insert_query(self, table_name: str, data: Dict[str, Any]) -> Tuple[str, List]:
        """Construye query INSERT"""
        columns = list(data.keys())
        placeholders = ["%s"] * len(columns)
        
        query = f"""
        INSERT INTO {self.schema}.{table_name} 
        ({', '.join(columns)}) 
        VALUES ({', '.join(placeholders)})
        RETURNING *
        """
        
        return query, list(data.values())
    
    def _build_update_query(self, table_name: str, data: Dict[str, Any], id_field: str, id_value: Any) -> Tuple[str, List]:
        """Construye query UPDATE"""
        set_clauses = [f"{key} = %s" for key in data.keys()]
        params = list(data.values())
        params.append(id_value)
        
        query = f"""
        UPDATE {self.schema}.{table_name} 
        SET {', '.join(set_clauses)} 
        WHERE {id_field} = %s
        RETURNING *
        """
        
        return query, params
    
    def _execute_query(self, query: str, params: List = None) -> List[Dict[str, Any]]:
        """Ejecuta una consulta y retorna resultados"""
        try:
            if params:
                return self.db.get(query, params)
            else:
                return self.db.get(query)
        except Exception as e:
            self.logger.error(f"Error executing query: {query}, params: {params}, error: {str(e)}")
            raise
    
    def _execute_command(self, query: str, params: List = None) -> int:
        """Ejecuta un comando (INSERT, UPDATE, DELETE) y retorna filas afectadas"""
        try:
            return self.db.execute(query, params)
        except Exception as e:
            self.logger.error(f"Error executing command: {query}, params: {params}, error: {str(e)}")
            raise
    
    def find_all(self, table_name: str, filters: Dict[str, Any] = None, order_by: str = None, limit: int = None) -> List[Dict[str, Any]]:
        """Obtiene todos los registros de una tabla"""
        where_clause, params = self._build_where_clause(filters)
        
        query = f"SELECT * FROM {self.schema}.{table_name}{where_clause}"
        
        if order_by:
            query += f" ORDER BY {order_by}"
        
        if limit:
            query += f" LIMIT {limit}"
        
        return self._execute_query(query, params)
    
    def find_by_id(self, table_name: str, id_field: str, id_value: Any) -> Optional[Dict[str, Any]]:
        """Obtiene un registro por ID"""
        query = f"SELECT * FROM {self.schema}.{table_name} WHERE {id_field} = %s"
        results = self._execute_query(query, [id_value])
        return results[0] if results else None
    
    def create(self, table_name: str, data: Dict[str, Any]) -> Dict[str, Any]:
        """Crea un nuevo registro"""
        query, params = self._build_insert_query(table_name, data)
        results = self._execute_query(query, params)
        return results[0] if results else None
    
    def update(self, table_name: str, data: Dict[str, Any], id_field: str, id_value: Any) -> Dict[str, Any]:
        """Actualiza un registro existente"""
        query, params = self._build_update_query(table_name, data, id_field, id_value)
        results = self._execute_query(query, params)
        return results[0] if results else None
    
    def delete(self, table_name: str, id_field: str, id_value: Any) -> int:
        """Elimina un registro (eliminación física)"""
        query = f"DELETE FROM {self.schema}.{table_name} WHERE {id_field} = %s"
        return self._execute_command(query, [id_value])
    
    def soft_delete(self, table_name: str, id_field: str, id_value: Any, user: str) -> Dict[str, Any]:
        """Elimina un registro (eliminación lógica)"""
        data = {
            'state': False,
            'user_deleted': user,
            'date_deleted': 'NOW()'
        }
        return self.update(table_name, data, id_field, id_value)
    
    def count(self, table_name: str, filters: Dict[str, Any] = None) -> int:
        """Cuenta registros en una tabla"""
        where_clause, params = self._build_where_clause(filters)
        query = f"SELECT COUNT(*) as total FROM {self.schema}.{table_name}{where_clause}"
        result = self._execute_query(query, params)
        return result[0]['total'] if result else 0
    
    def exists(self, table_name: str, id_field: str, id_value: Any) -> bool:
        """Verifica si existe un registro"""
        query = f"SELECT 1 FROM {self.schema}.{table_name} WHERE {id_field} = %s LIMIT 1"
        result = self._execute_query(query, [id_value])
        return len(result) > 0