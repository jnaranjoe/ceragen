from flask_restful import Resource

from ..Model.Request.SecuModel import *
from ..Components.SecuComponent import *
from ...utils.general.logs import HandleLogs
from ...utils.general.response import response_error, response_success, response_not_found, response_unauthorize
# from ..Components.jwt_component import JwtComponent
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