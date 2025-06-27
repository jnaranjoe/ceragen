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
        