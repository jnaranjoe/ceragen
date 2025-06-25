from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response


class PersonGenreComponent:
    @staticmethod
    def getAllGenres():
        try:
            result = False
            data = None
            message = None
            sql = """
                SELECT apg.id, apg.genre_name, apg.state
                FROM ceragen.admin_person_genre apg
            """

            resultado = DataBaseHandle.getRecords(sql,0)
            print("Resultado de la consulta: ", resultado['data'])
            if resultado['result']:
                result = True
                data = resultado['data']
            else:
                message = 'Error al Obtener datos de usuarios -> ' + resultado['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

#====================================================================
#PERSON
#====================================================================
class PersonComponent:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None

            sql = """
                SELECT ap.per_id, ap.per_identification, concat(per_names, ' ', per_surnames) as nombre
                FROM ceragen.admin_person ap
            """

            resultado = DataBaseHandle.getRecords(sql,0)
            print("Resultado de la consulta: ", resultado['data'])
            if resultado['result']:
                result = True
                data = resultado['data']
            else:
                message = 'Error al Obtener datos -> ' + resultado['message']
        except Exception as err:
            message = err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)
    
    @staticmethod
    def createPer(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                INSERT INTO ceragen.admin_person (per_identification,
                per_names,
                per_surnames,
                per_genre_id,
                per_marital_status_id,
                per_country,
                per_city,
                per_address,
                per_phone,
                per_mail,
                per_birth_date)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """
            # print("Datos a insertar: ", datos)
            record = (
                datos['per_identification'],
                datos['per_names'],
                datos['per_surnames'],
                datos['per_genre_id'],
                datos['per_marital_status_id'],
                datos['per_country'],
                datos['per_city'],
                datos['per_address'],
                datos['per_phone'],
                datos['per_mail'],
                datos['per_birth_date'],
            )

            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            if data is None:
                if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    result = True
                else:
                    message = "Error al crear" + data_NonQuery['message']
            else:
                message="error al ejecutar sql para crear"
                HandleLogs.write_error(message)
                
        except Exception as err:
            message = "Error al crear" + err.__str__()
            HandleLogs.write_error(message)

        finally:
            return internal_response(result, data, message)
    
    @staticmethod
    def updatePer(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                UPDATE ceragen.admin_person SET
                    per_identification = %s,
                    per_names = %s,
                    per_surnames = %s,
                    per_genre_id = %s,
                    per_marital_status_id = %s,
                    per_country = %s,
                    per_city = %s,
                    per_address = %s,
                    per_phone = %s,
                    per_mail = %s,
                    per_birth_date = %s
                WHERE per_id = %s
            """
            record = (
                datos['per_identification'],
                datos['per_names'],
                datos['per_surnames'],
                datos['per_genre_id'],
                datos['per_marital_status_id'],
                datos['per_country'],
                datos['per_city'],
                datos['per_address'],
                datos['per_phone'],
                datos['per_mail'],
                datos['per_birth_date'],
                datos['per_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result = True
                data = data_NonQuery['data']
            else:
                message = "Error al actualizar: " + data_NonQuery['message']
        except Exception as err:
            message = "Error al actualizar: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)
    
    @staticmethod
    def logicDeletePer(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                UPDATE ceragen.admin_person SET
                    per_state = %s
                WHERE per_id = %s
            """
            record = (
                datos['per_state'],
                datos['per_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result = True
                data = data_NonQuery['data']
            else:
                message = "Error al eliminar: " + data_NonQuery['message']
        except Exception as err:
            message = "Error al eliminar: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)


#====================================================================
#ROL
#====================================================================

class RolComponent:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None

            sql = """
                SELECT sr.rol_id, sr.rol_name, sr.rol_description, sr.is_admin_rol
	            FROM ceragen.segu_rol sr;
            """

            resultado = DataBaseHandle.getRecords(sql,0)
            print("Resultado de la consulta: ", resultado['data'])
            if resultado['result']:
                result = True
                data = resultado['data']
            else:
                message = 'Error al Obtener datos -> ' + resultado['message']
        except Exception as err:
            message = err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                INSERT INTO ceragen.segu_rol (rol_name,
                rol_description,
                is_admin_rol)
                VALUES (%s,%s,%s)
            """
            # print("Datos a insertar: ", datos)
            record = (
                datos['rol_name'],
                datos['rol_description'],
                datos['is_admin_rol'],
            )

            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            if data is None:
                if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    result = True
                else:
                    message = "Error al crear" + data_NonQuery['message']
            else:
                message="error al ejecutar sql para crear"
                HandleLogs.write_error(message)
                
        except Exception as err:
            message = "Error al crear" + err.__str__()
            HandleLogs.write_error(message)

        finally:
            return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                UPDATE ceragen.segu_rol SET
                    rol_name = %s,
                    rol_description = %s,
                    is_admin_rol = %s
                WHERE rol_id = %s
            """
            record = (
                datos['rol_name'],
                datos['rol_description'],
                datos['is_admin_rol'],
                datos['rol_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result = True
                data = data_NonQuery['data']
            else:
                message = "Error al actualizar: " + data_NonQuery['message']
        except Exception as err:
            message = "Error al actualizar: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                UPDATE ceragen.segu_rol SET
                    per_state = %s
                WHERE per_id = %s
            """
            record = (
                datos['per_state'],
                datos['per_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result = True
                data = data_NonQuery['data']
            else:
                message = "Error al eliminar: " + data_NonQuery['message']
        except Exception as err:
            message = "Error al eliminar: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)