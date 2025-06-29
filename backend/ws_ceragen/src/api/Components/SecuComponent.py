from ...utils.database.connection_db import DataBaseHandle
from ...utils.general.logs import HandleLogs
from ...utils.general.response import internal_response
from decimal import Decimal
from datetime import datetime

#====================================================================
#PERSON GENRE
#====================================================================
class PersonGenreComponent:
    @staticmethod
    def getAll():
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
#PERSON_MARITAL_STATUS
#====================================================================
class MaritalStatusComponent:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None
            sql = """
                SELECT ams.id, ams.status_name, ams.state
                FROM ceragen.admin_marital_status ams
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
                SELECT ap.per_id, ap.per_identification, concat(per_names, ' ', per_surnames) as nombre, per_genre_id,
                per_marital_status_id,
                per_country,
                per_city,
                per_address,
                per_phone,
                per_mail,
                per_birth_date
                FROM ceragen.admin_person ap
            """

            resultado = DataBaseHandle.getRecords(sql,0)
            print("Resultado de la consulta: ", resultado['data'])
            if resultado['result']:
                # Convierte per_birth_date a string si es datetime
                for row in resultado['data']:
                    if isinstance(row.get('per_birth_date'), datetime):
                        row['per_birth_date'] = row['per_birth_date'].strftime('%Y-%m-%d')
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
#User
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
                SELECT sur.id_user_rol, sur.id_user,su.user_person_id, ap.per_names, ap.per_surnames,
                ap.per_genre_id,
                apg.genre_name,
                ap.per_marital_status_id,
                ams.status_name,
                ap.per_country,
                ap.per_city,
                ap.per_address,
                ap.per_phone,
                ap.per_mail,
                ap.per_birth_date,
                sur.id_rol, sr.rol_name, sur.state
                FROM ceragen.segu_user_rol sur
                left join ceragen.segu_user su on sur.id_user = su.user_id
                left join ceragen.admin_person ap on su.user_person_id = ap.per_id
                left join ceragen.segu_rol sr on sur.id_rol = sr.rol_id
                left join ceragen.admin_person_genre apg on ap.per_genre_id = apg.id
                left join ceragen.admin_marital_status ams on ap.per_marital_status_id = ams.id;
            """

            resultado = DataBaseHandle.getRecords(sql,0)
            print("Resultado de la consulta: ", resultado['data'])
            if resultado['result']:
                # Convierte per_birth_date a string si es datetime
                for row in resultado['data']:
                    if isinstance(row.get('per_birth_date'), datetime):
                        row['per_birth_date'] = row['per_birth_date'].strftime('%Y-%m-%d')
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
        
    
#=====================================================================
#Componente custom 1
#=====================================================================
class Custom1Component:
    @staticmethod
    def getAll():
        try:
            result = False
            data = None
            message = None

            sql = """
                SELECT sur.id_user_rol, su.user_person_id, concat(ap.per_names, ' ', ap.per_surnames) as nombre, sur.id_user, sur.id_rol, sr.rol_name, sur.state
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
        perId = None
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
            # Ejecutar la inserción en la tabla admin_person
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            if data is None:
                if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    perId = {
                        "id_user": data_NonQuery['data']
                    }
                    result = True
                else:
                    message = "Error al crear persona" + data_NonQuery['message']
            else:
                message="error al ejecutar sql para crear"
                HandleLogs.write_error(message)
            
            print("ID de la persona recién insertada: ", perId)
            #Validar el tipo de rol y ver si es necesario insertar en otra tabla
            if datos['id_rol'] == 1:
                print("Es admin")  # Supongamos que el rol con id 1 es el rol de administrador
            elif datos['id_rol'] == 2:
                print("Es Secretario")
            elif datos['id_rol'] == 3:
                print("Es Medico")
                
                sql = """
                INSERT INTO ceragen.admin_medical_staff (med_person_id)
                VALUES (%s)
                """
                # print("Datos a insertar: ", datos)
                record = (
                    perId['id_user'],  # Asumiendo que el ID de la persona recién insertada es per_id
                )
                data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            elif datos['id_rol'] == 4:
                print("Es cliente")

                sql = """
                INSERT INTO ceragen.admin_client (cli_person_id)
                VALUES (%s)
                """
                # print("Datos a insertar: ", datos)
                record = (
                    perId['id_user'],  # Asumiendo que el ID de la persona recién insertada es per_id
                )
                data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            elif datos['id_rol'] == 5:
                print("Es paciente")
                
                sql = """
                INSERT INTO ceragen.admin_patient (pat_person_id)
                VALUES (%s)
                """
                # print("Datos a insertar: ", datos)
                record = (
                    perId['id_user'],  # Asumiendo que el ID de la persona recién insertada es per_id
                )
                data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)

            if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    result = True
            else:
                message = "Error al asignar a otras tablas" + data_NonQuery['message']
            #Insertar en tabla user
            sql = """
                INSERT INTO ceragen.segu_user (user_person_id,
                user_mail,
                user_password)
                VALUES (%s,%s,%s)
            """
            record = (
                perId['id_user'],
                datos['per_mail'],
                datos['per_identification']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    userId = {
                        "id_user": data_NonQuery['data']
                    }
                    result = True
            else:
                message = "Error al asignar a otras tablas" + data_NonQuery['message']
            # Ahora, insertar en la tabla segu_user_rol

            sql = """
                INSERT INTO ceragen.segu_user_rol (id_user,
                id_rol)
                VALUES (%s,%s)
            """
            # print("Datos a insertar: ", datos)
            record = (
                userId['id_user'],
                datos['id_rol'],
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql,record)
            if data_NonQuery['result']:
                    data = data_NonQuery['data']
                    result = True
            else:
                message = "Error al asignar a otras tablas" + data_NonQuery['message']

        except Exception as err:
            message = "Error al crear" + err.__str__()
            HandleLogs.write_error(message)

        finally:
            return internal_response(result, data, message)

#=====================================================================
#Tabla tipo personal medico
#=====================================================================
class MedicPersonTypeComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT mpt_id, mpt_name, mpt_description, mpt_state
                FROM ceragen.admin_medic_person_type
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            if resultado['result']:
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener tipos de médicos -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.admin_medic_person_type
                (mpt_name, mpt_description)
                VALUES (%s, %s)
            """
            record = (datos['mpt_name'], datos['mpt_description'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear tipo médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_medic_person_type SET
                mpt_name = %s,
                mpt_description = %s,
                WHERE mpt_id = %s
            """
            record = (datos['mpt_name'], datos['mpt_description'], datos['mpt_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar tipo médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_medic_person_type SET mpt_state = %s WHERE mpt_id = %s
            """
            record = (datos['mpt_state'], datos['mpt_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al eliminar tipo médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message) 
#=====================================================================
#Tabla personal medico
#=====================================================================
class MedicalStaffComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT med_id, med_person_id, concat(ap.per_names, ' ', ap.per_surnames) as nombreMedico, med_type_id, ampt.mpt_name, med_specialty, med_state
                FROM ceragen.admin_medical_staff ams
				left join ceragen.admin_person ap on ams.med_person_id = ap.per_id
				left join ceragen.admin_medic_person_type ampt on ams.med_type_id = ampt.mpt_id
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            if resultado['result']:
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener personal médico -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.admin_medical_staff
                (med_person_id, med_type_id, med_specialty)
                VALUES (%s, %s, %s)
            """
            record = (
                datos['med_person_id'],
                datos['med_type_id'],
                datos['med_specialty'],
                datos['med_state']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear personal médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_medical_staff SET
                med_type_id = %s,
                med_specialty = %s
                WHERE med_id = %s
            """
            record = (
                datos['med_type_id'],
                datos['med_specialty'],
                datos['med_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar personal médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_medical_staff SET med_state = %s WHERE med_id = %s
            """
            record = (datos['med_state'], datos['med_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al eliminar personal médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

#=====================================================================
#Tabla paciente
#=====================================================================
class PatientComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT pat_id, pat_person_id, pat_medical_conditions, pat_allergies,
                       pat_blood_type, pat_emergency_contact_name,
                       pat_emergency_contact_phone, pat_state
                FROM ceragen.admin_patient
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            if resultado['result']:
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener pacientes -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.admin_patient
                (pat_person_id, pat_medical_conditions, pat_allergies,
                 pat_blood_type, pat_emergency_contact_name,
                 pat_emergency_contact_phone, pat_state)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            record = (
                datos['pat_person_id'],
                datos['pat_medical_conditions'],
                datos['pat_allergies'],
                datos['pat_blood_type'],
                datos['pat_emergency_contact_name'],
                datos['pat_emergency_contact_phone'],
                datos['pat_state']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear paciente: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_patient SET
                pat_medical_conditions = %s,
                pat_allergies = %s,
                pat_blood_type = %s,
                pat_emergency_contact_name = %s,
                pat_emergency_contact_phone = %s
                WHERE pat_id = %s
            """
            record = (
                datos['pat_medical_conditions'],
                datos['pat_allergies'],
                datos['pat_blood_type'],
                datos['pat_emergency_contact_name'],
                datos['pat_emergency_contact_phone'],
                datos['pat_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar paciente: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_patient SET pat_state = %s WHERE pat_id = %s
            """
            record = (datos['pat_state'], datos['pat_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al eliminar paciente: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

#=====================================================================
#Tabla Historial Medico
#=====================================================================
class MedicalHistoryComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT hist_id, hist_patient_id, hist_primary_complaint,
                       hist_related_trauma, hist_current_treatment, hist_notes
                FROM ceragen.clinic_patient_medical_history
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            if resultado['result']:
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener historiales médicos -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.clinic_patient_medical_history
                (hist_patient_id, hist_primary_complaint,
                 hist_related_trauma, hist_current_treatment, hist_notes)
                VALUES (%s, %s, %s, %s, %s)
            """
            record = (
                datos['hist_patient_id'],
                datos['hist_primary_complaint'],
                datos['hist_related_trauma'],
                datos['hist_current_treatment'],
                datos['hist_notes']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear historial médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.clinic_patient_medical_history SET
                hist_patient_id = %s,
                hist_primary_complaint = %s,
                hist_related_trauma = %s,
                hist_current_treatment = %s,
                hist_notes = %s
                WHERE hist_id = %s
            """
            record = (
                datos['hist_patient_id'],
                datos['hist_primary_complaint'],
                datos['hist_related_trauma'],
                datos['hist_current_treatment'],
                datos['hist_notes'],
                datos['hist_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar historial médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)
    
    @staticmethod
    def delete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                Delete from ceragen.clinic_patient_medical_history
                WHERE hist_id = %s
            """
            record = (
                datos['hist_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar historial médico: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

#=====================================================================
#Tabla Producto
#=====================================================================

class ProductComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT pro_id, pro_name, pro_description, pro_price,
                       pro_total_sessions,
                       pro_therapy_type_id, pro_state
                FROM ceragen.admin_product
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            # Convierte todos los Decimals a float en una lista de diccionarios
            if resultado['result']:
                for prod in resultado['data']:
                    if isinstance(prod.get('pro_price'), Decimal):
                        prod['pro_price'] = float(prod['pro_price'])
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener productos -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.admin_product
                (pro_name, pro_description, pro_price,
                 pro_total_sessions,
                 pro_therapy_type_id)
                VALUES (%s, %s, %s, %s, %s)
            """
            record = (
                datos['pro_name'],
                datos['pro_description'],
                datos['pro_price'],
                datos['pro_total_sessions'],
                datos['pro_therapy_type_id'],
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear producto: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_product SET
                pro_name = %s,
                pro_description = %s,
                pro_price = %s,
                pro_total_sessions = %s,
                pro_therapy_type_id = %s,
                WHERE pro_id = %s
            """
            record = (
                datos['pro_name'],
                datos['pro_description'],
                datos['pro_price'],
                datos['pro_total_sessions'],
                datos['pro_therapy_type_id'],
                datos['pro_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar producto: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_product SET pro_state = %s WHERE pro_id = %s
            """
            record = (datos['pro_state'], datos['pro_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al eliminar producto: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

#=====================================================================
#Tabla TherapyType
#=====================================================================
class TherapyTypeComponent:
    @staticmethod
    def getAll():
        result, data, message = False, None, None
        try:
            sql = """
                SELECT tht_id, tht_name, tht_description, tht_state
                FROM ceragen.admin_therapy_type
            """
            resultado = DataBaseHandle.getRecords(sql, 0)
            if resultado['result']:
                result, data = True, resultado['data']
            else:
                message = 'Error al obtener tipos de terapia -> ' + resultado['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def create(datos):
        result, data, message = False, None, None
        try:
            sql = """
                INSERT INTO ceragen.admin_therapy_type
                (tht_name, tht_description)
                VALUES (%s, %s)
            """
            record = (
                datos['tht_name'],
                datos['tht_description'],
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al crear tipo de terapia: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def update(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_therapy_type SET
                tht_name = %s,
                tht_description = %s,
                WHERE tht_id = %s
            """
            record = (
                datos['tht_name'],
                datos['tht_description'],
                datos['tht_id']
            )
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al actualizar tipo de terapia: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)

    @staticmethod
    def logicDelete(datos):
        result, data, message = False, None, None
        try:
            sql = """
                UPDATE ceragen.admin_therapy_type SET tht_state = %s WHERE tht_id = %s
            """
            record = (datos['tht_state'], datos['tht_id'])
            data_NonQuery = DataBaseHandle.ExecuteNonQuery(sql, record)
            if data_NonQuery['result']:
                result, data = True, data_NonQuery['data']
            else:
                message = "Error al eliminar tipo de terapia: " + data_NonQuery['message']
        except Exception as err:
            message = str(err)
            HandleLogs.write_error(message)
        return internal_response(result, data, message)
