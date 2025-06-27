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
                    rol_state = %s
                WHERE rol_id = %s
            """
            record = (
                datos['rol_state'],
                datos['rol_id']
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

class UserComponent:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None

            sql = """
                SELECT su.user_id, su.user_person_id, concat(ap.per_names, ' ', ap.per_surnames) as nombre, su.user_mail, su.user_password, su.user_locked, su.user_state
                FROM ceragen.segu_user su
                left join ceragen.admin_person ap on su.user_person_id = ap.per_id;
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
                INSERT INTO ceragen.segu_user (user_person_id,
                user_mail,
                user_password)
                VALUES (%s,%s,%s)
            """
            # print("Datos a insertar: ", datos)
            record = (
                datos['user_person_id'],
                datos['user_mail'],
                datos['user_password'],
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
                UPDATE ceragen.segu_user SET
                    user_person_id = %s,
                    user_mail = %s,
                    user_password = %s,
                    user_locked = %s
                WHERE user_id = %s
            """
            record = (
                datos['user_id'],
                datos['user_person_id'],
                datos['user_mail'],
                datos['user_password'],
                datos['user_locked']
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
                UPDATE ceragen.segu_user SET
                    user_state = %s
                WHERE user_id = %s
            """
            record = (
                datos['user_state'],
                datos['user_id']
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

    @staticmethod
    def login(email, password):
        result = False
        data = None
        message = None
        try:
            # 1. Buscar al usuario por su correo electrónico
            sql = """
                SELECT user_id, user_person_id, user_mail, user_password, user_locked, user_state
                FROM ceragen.segu_user 
                WHERE user_mail = %s
            """
            record = (email,)
            user_data_result = DataBaseHandle.getRecords(sql, 1, record)

            if not user_data_result['result'] or not user_data_result['data']:
                message = "Usuario o contraseña incorrectos."
                return internal_response(result, data, message)

            user = user_data_result['data']

            if user['user_password'] == password:
                # 3. Verificar si la cuenta está activa y no bloqueada
                if not user['user_state']:
                    message = "La cuenta de usuario está inactiva."
                elif user['user_locked']:
                    message = "La cuenta de usuario está bloqueada."
                else:
                    # Si todo está bien, preparamos los datos del usuario para devolverlos
                    result = True
                    data = {
                        "user_id": user['user_id'],
                        "user_person_id": user['user_person_id'],
                        "user_mail": user['user_mail']
                    }
                    message = "Login exitoso."
            else:
                message = "Usuario o contraseña incorrectos."

        except Exception as err:
            message = "Error en el proceso de login: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def getUserByEmail(email):
        try:
            result = False
            data = None
            message = None
            sql = """
                SELECT su.user_id, su.user_mail, concat(ap.per_names, ' ', ap.per_surnames) as nombre
                FROM ceragen.segu_user su
                LEFT JOIN ceragen.admin_person ap ON su.user_person_id = ap.per_id
                WHERE su.user_mail = %s
            """
            record = (email,)
            
            # Usamos el método getRecords con tamaño 1 para obtener solo un registro
            resultado = DataBaseHandle.getRecords(sql, 1, record)
            
            if resultado['result']:
                result = True
                data = resultado['data']
            else:
                message = 'Error al obtener datos del usuario -> ' + resultado['message']
        except Exception as err:
            HandleLogs.write_error(err)
            message = err.__str__()
        finally:
            return internal_response(result, data, message)

    @staticmethod
    def UsePasswordUpdateMail(new_password, mail_user):
        result = False
        data = None
        message = None
        try:
            
            sql = """
                UPDATE ceragen.segu_user SET
                    user_password = %s
                WHERE user_mail = %s
            """
            record = (new_password, mail_user)
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            
            if data_NonQuery['result']:
                result = True
                data = {"updated_user_with_mail": mail_user}
                message = "Contraseña actualizada correctamente."
            else:
                # Esto podría ocurrir si el email no se encuentra, aunque el token sea válido.
                message = "Error al ejecutar la actualización en la base de datos: " + data_NonQuery['message']
                result = False

        except Exception as err:
            message = "Error en el proceso de actualización: " + err.__str__()
            HandleLogs.write_error(message)
        finally:
            return internal_response(result, data, message)

#====================================================================
# User_Rol  
#====================================================================
class UserRolComponent:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None

            sql = """
                SELECT sur.id_user_rol, concat(ap.per_names, ' ', ap.per_surnames) as nombre, sur.id_user, sur.id_rol, sr.rol_name, sur.state
                FROM ceragen.segu_user_rol sur
                left join ceragen.segu_user su on sur.id_user = su.user_id
                left join ceragen.admin_person ap on su.user_person_id = ap.per_id
                left join ceragen.segu_rol sr on sur.id_rol = sr.rol_id;
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
                INSERT INTO ceragen.segu_user_rol (id_user,
                id_rol)
                VALUES (%s,%s)
            """
            # print("Datos a insertar: ", datos)
            record = (
                datos['id_user'],
                datos['id_rol'],
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
    def logicDelete(datos):
        result = False
        data = None
        message = None
        try:
            sql = """
                UPDATE ceragen.segu_user_rol SET
                    state = %s
                WHERE id_user_rol = %s
            """
            record = (
                datos['state'],
                datos['id_user_rol']
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
        
    
