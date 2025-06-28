from flask_restful import Resource

from ..Model.Request.SecuModel import *
from ..Components.SecuComponent import *
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found, response_unauthorize
# from ..Components.jwt_component import JwtComponent
from ...utils.smpt.smpt_officeUG import send_password_recovery_email
from ..Components.TokenComponent import TokenComponent
from flask import request

class PersonGenre(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar Usuario")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = PersonGenreComponent.getAllGenres()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

#====================================================================
# PERSON   
#====================================================================   
class PersonGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = PersonComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PersonCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            # print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PersonReq()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'per_identification':rq_json['per_identification'],
                'per_names':rq_json['per_names'],
                'per_surnames':rq_json['per_surnames'],
                'per_genre_id':rq_json['per_genre_id'],
                'per_marital_status_id':rq_json['per_marital_status_id'],
                'per_country':rq_json['per_country'],
                'per_city':rq_json['per_city'],
                'per_address':rq_json['per_address'],
                'per_phone':rq_json['per_phone'],
                'per_mail':rq_json['per_mail'],
                'per_birth_date':rq_json['per_birth_date'],
            }
            resultado = PersonComponent.createPer(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PersonUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Actualizar")
            # Obtener el request
            rq_json = request.get_json()

            # print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PersonIdReq()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'per_id':rq_json['per_id'],
                'per_identification':rq_json['per_identification'],
                'per_names':rq_json['per_names'],
                'per_surnames':rq_json['per_surnames'],
                'per_genre_id':rq_json['per_genre_id'],
                'per_marital_status_id':rq_json['per_marital_status_id'],
                'per_country':rq_json['per_country'],
                'per_city':rq_json['per_city'],
                'per_address':rq_json['per_address'],
                'per_phone':rq_json['per_phone'],
                'per_mail':rq_json['per_mail'],
                'per_birth_date':rq_json['per_birth_date'],
            }
            resultado = PersonComponent.updatePer(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PersonLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PersonDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'per_id':rq_json['per_id'],
                'per_state':rq_json['per_state'],
            }
            resultado = PersonComponent.logicDeletePer(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#====================================================================
# Rol   
#====================================================================

class RolGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = RolComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class RolCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = RolReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'rol_name':rq_json['rol_name'],
                'rol_description':rq_json['rol_description'],
                'is_admin_rol':rq_json['is_admin_rol'],
            }
            resultado = RolComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class RolUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = RolIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'rol_id':rq_json['rol_id'],
                'rol_name':rq_json['rol_name'],
                'rol_description':rq_json['rol_description'],
                'is_admin_rol':rq_json['is_admin_rol'],
            }
            resultado = RolComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class RolLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = RolDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'rol_id':rq_json['rol_id'],
                'rol_state':rq_json['rol_state'],
            }
            resultado = RolComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#====================================================================
# User   
#====================================================================

class UserGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = UserComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class UserCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = UserReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'user_person_id':rq_json['user_person_id'],
                'user_mail':rq_json['user_mail'],
                'user_password':rq_json['user_password'],
            }
            resultado = UserComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class UserUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = UserIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'user_id':rq_json['user_id'],
                'user_person_id':rq_json['user_person_id'],
                'user_mail':rq_json['user_mail'],
                'user_password':rq_json['user_password'],
                'user_locked':rq_json['user_locked']
            }
            resultado = UserComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class UserLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = UserDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'user_id':rq_json['user_id'],
                'user_state':rq_json['user_state'],
            }
            resultado = UserComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

#====================================================================
# User_Rol  
#====================================================================
class UserRolGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = UserRolComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class UserRolCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = UserRolReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'id_user':rq_json['id_user'],
                'id_rol':rq_json['id_rol'],
            }
            resultado = UserRolComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

class UserRolLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = UserRolDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'id_user_rol':rq_json['id_user_rol'],
                'state':rq_json['state'],
            }
            resultado = UserRolComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class LoginService(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Iniciando servicio de Login")
            rq_json = request.get_json()

            # Validar el request
            new_request = LoginRequest()
            error = new_request.validate(rq_json)
            if error:
                return response_error("Error al Validar el Request -> " + str(error))

            # Verificar credenciales usando el componente
            login_result = UserComponent.login(rq_json['login_user'], rq_json['login_password'])

            if not login_result['result']:
                # Si el login falla (contraseña incorrecta, usuario inactivo, etc.)
                return response_unauthorize()

            # Si el login es exitoso, generar el token
            user_info = login_result['data']
            token = TokenComponent.Token_Generate(user_info) # Generamos el token con la info del usuario
            
            # Devolver el token y los datos del usuario
            return response_success({
                "token": token,
                "user": user_info
            })

        except Exception as err:
            error_msg = f"Error inesperado en el servicio de Login: {err.__str__()}"
            HandleLogs.write_error(error_msg)
            return response_error(error_msg)

class PasswordRecovery(Resource):
    @staticmethod
    def patch():
        try:
            HandleLogs.write_log("Ejecutando servicio de Recuperación de Contraseña")
            rq_json = request.get_json() 

            # Validar la solicitud utilizando el esquema
            new_request = SendEmailPasswordReq()
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)

            user_mail = rq_json['user_mail']
            resultado = send_password_recovery_email(user_mail)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class EmailPasswordUpdate(Resource):
    @staticmethod
    def patch():
        try:
            HandleLogs.write_log("Iniciando servicio: Actualizar Password Por Email")
            rq_json = request.get_json()

            # Validar el request (ahora sin user_id)
            new_request = UpdatePasswordSchema()
            error = new_request.validate(rq_json)
            if error:
                error_message = "Error al Validar el Request -> " + str(error)
                HandleLogs.write_error(error_message)
                return response_error(error_message)
            
            # Validar el token y obtener el correo electrónico
            mail_user = TokenComponent.Token_Validate_ResetPassword(rq_json["token_temp"])
            if mail_user is None:
                return response_error("Error: Token inválido o expirado.")

            # Llamar al componente para actualizar la contraseña (ahora sin user_id)
            answer = UserComponent.UsePasswordUpdateMail(
                rq_json["new_password"],
                mail_user
            )
            
            if answer['result']:
                return response_success(answer['message'])
            else:
                return response_error(answer['message'])

        except Exception as err:
            error_msg = f"Error inesperado en el servicio: {err.__str__()}"
            HandleLogs.write_error(error_msg)
            return response_error(error_msg)


#=====================================================================
#SERVICIO CUSTOM 1
#Permite insertar misma informacion en multiples tablas
#Inserta persona, obtiene id y lo inserta en Usuario_Rol, Rol permite saber si es ese mismo idPersona lo mando a la tabla medicoStaff, Cliente o Paciente.
#Si es cliente no se le crea el usuario_rol, 
#=====================================================================

class Custom1Create(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = Custom1Req() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'per_identification':rq_json['per_identification'],
                'per_names':rq_json['per_names'],
                'per_surnames':rq_json['per_surnames'],
                'per_genre_id':rq_json['per_genre_id'],
                'per_marital_status_id':rq_json['per_marital_status_id'],
                'per_country':rq_json['per_country'],
                'per_city':rq_json['per_city'],
                'per_address':rq_json['per_address'],
                'per_phone':rq_json['per_phone'],
                'per_mail':rq_json['per_mail'],
                'per_birth_date':rq_json['per_birth_date'],
                'id_rol':rq_json['id_rol'],
            }
            resultado = Custom1Component.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#====================================================================
# Type Medic  
#====================================================================

class TypeMedicGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = MedicPersonTypeComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TypeMedicCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TypeMedicReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'mpt_name':rq_json['mpt_name'],
                'mpt_description':rq_json['mpt_description'],
            }
            resultado = MedicPersonTypeComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TypeMedicUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TypeMedicIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'mpt_id':rq_json['mpt_id'],
                'mpt_name':rq_json['mpt_name'],
                'mpt_description':rq_json['mpt_description'],
            }
            resultado = MedicPersonTypeComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TypeMedicLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TypeMedicDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'mpt_id':rq_json['mpt_id'],
                'mpt_state':rq_json['mpt_state'],
            }
            resultado = MedicPersonTypeComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#=====================================================================
#Tabla personal medico
#=====================================================================

class MedicGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = MedicalStaffComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedicCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedicReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'med_person_id':rq_json['med_person_id'],
                'med_type_id':rq_json['med_type_id'],
                'med_specialty':rq_json['med_specialty'],
            }
            resultado = MedicalStaffComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedicUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedicIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'med_id':rq_json['med_id'],
                'med_type_id':rq_json['med_type_id'],
                'med_specialty':rq_json['med_specialty'],
            }
            resultado = MedicalStaffComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedicLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedicDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'med_id':rq_json['med_id'],
                'med_state':rq_json['med_state'],
            }
            resultado = MedicalStaffComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#=====================================================================
#Tabla paciente
#=====================================================================

class PatientGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = PatientComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PatientCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PatientReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pat_person_id':rq_json['pat_person_id'],
                'pat_medical_conditions':rq_json['pat_medical_conditions'],
                'pat_allergies':rq_json['pat_allergies'],
                'pat_blood_type':rq_json['pat_blood_type'],
                'pat_emergency_contact_name':rq_json['pat_emergency_contact_name'],
                'pat_emergency_contact_phone':rq_json['pat_emergency_contact_phone'],
            }
            resultado = PatientComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PatientUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PatientIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pat_id':rq_json['pat_id'],
                'pat_medical_conditions':rq_json['pat_medical_conditions'],
                'pat_allergies':rq_json['pat_allergies'],
                'pat_blood_type':rq_json['pat_blood_type'],
                'pat_emergency_contact_name':rq_json['pat_emergency_contact_name'],
                'pat_emergency_contact_phone':rq_json['pat_emergency_contact_phone'],
            }
            resultado = PatientComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class PatientLogicDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = PatientDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pat_id':rq_json['pat_id'],
                'pat_state':rq_json['pat_state'],
            }
            resultado = PatientComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

#=====================================================================
#Tabla Historial Medico
#=====================================================================

class MedHistoryGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = MedicalHistoryComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedHistoryCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedHistoryReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'hist_patient_id':rq_json['hist_patient_id'],
                'hist_primary_complaint':rq_json['hist_primary_complaint'],
                'hist_related_trauma':rq_json['hist_related_trauma'],
                'hist_current_treatment':rq_json['hist_current_treatment'],
                'hist_notes':rq_json['hist_notes'],
            }
            resultado = MedicalHistoryComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedHistoryUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedHistoryIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'hist_id':rq_json['hist_id'],
                'hist_patient_id':rq_json['hist_patient_id'],
                'hist_primary_complaint':rq_json['hist_primary_complaint'],
                'hist_related_trauma':rq_json['hist_related_trauma'],
                'hist_current_treatment':rq_json['hist_current_treatment'],
                'hist_notes':rq_json['hist_notes'],
            }
            resultado = MedicalHistoryComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class MedHistoryDelete(Resource):
    @staticmethod
    def delete():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = MedHistoryDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'hist_id':rq_json['hist_id'],
            }
            resultado = MedicalHistoryComponent.delete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
#=====================================================================
#Tabla Producto
#=====================================================================
class ProductGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = ProductComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class ProductCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = ProductReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pro_name':rq_json['pro_name'],
                'pro_description':rq_json['pro_description'],
                'pro_price':rq_json['pro_price'],
                'pro_total_sessions':rq_json['pro_total_sessions'],
                'pro_therapy_type_id':rq_json['pro_therapy_type_id'],
            }
            resultado = ProductComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class ProductUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = ProductIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pro_name':rq_json['pro_name'],
                'pro_description':rq_json['pro_description'],
                'pro_price':rq_json['pro_price'],
                'pro_total_sessions':rq_json['pro_total_sessions'],
                'pro_therapy_type_id':rq_json['pro_therapy_type_id'],
                'pro_id':rq_json['pro_id'],
            }
            resultado = ProductComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class ProductDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = ProductDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'pro_id':rq_json['pro_id'],
                'pro_state':rq_json['pro_state'],
            }
            resultado = ProductComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())

#=====================================================================
#Tabla TherapyType
#=====================================================================
class TherapyTypeGet(Resource):
    @staticmethod
    def get():
        try:
            HandleLogs.write_log("Ejecutando servicio de Listar")
            # #Validar que el token sea correcto
            # token = request.headers['tokenapp']
            # if not JwtComponent.token_validate(token):
            #     return response_unauthorize()

            resultado = TherapyTypeComponent.getAll()
            # print("Resultado de la consulta: ", resultado)
            if resultado['result']:
                if resultado['data'].__len__() > 0:
                    return response_success(resultado['data'])
                else:
                    return response_not_found()
            else:
                return response_error(resultado['message'])
            # return response_success(resultado['data'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TherapyTypeCreate(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TherapyTypeReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'tht_name':rq_json['tht_name'],
                'tht_description':rq_json['tht_description'],
            }
            resultado = TherapyTypeComponent.create(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TherapyTypeUpdate(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Crear")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TherapyTypeIdReq() 
            error_en_validacion = new_request.validate(rq_json)
            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'tht_name':rq_json['tht_name'],
                'tht_description':rq_json['tht_description'],
                'tht_id':rq_json['tht_id'],
            }
            resultado = TherapyTypeComponent.update(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())
        
class TherapyTypeDelete(Resource):
    @staticmethod
    def put():
        try:
            HandleLogs.write_log("Ejecutando servicio de Eliminar Lógicamente")
            # Obtener el request
            rq_json = request.get_json()

            print("Datos del request: ", rq_json)
            # Validar ese request sea compatible con el modelo
            new_request = TherapyTypeDeleteReq()
            error_en_validacion = new_request.validate(rq_json)

            if error_en_validacion:
                message = "Error al validar el request -> " + str(error_en_validacion)
                HandleLogs.write_error(message)
                return response_error(message)
            
            payload = {
                'tht_id':rq_json['tht_id'],
                'tht_state':rq_json['tht_state'],
            }
            resultado = TherapyTypeComponent.logicDelete(payload)

            if resultado['result']:
                return response_success(resultado['data'])
            else:
                return response_error(resultado['message'])

        except Exception as err:
            HandleLogs.write_error(err)
            return response_error("Error en el método: " + err.__str__())