from ..Services.SecuService import *

def load_routes(api):
    #metodo para el login
    api.add_resource(LoginService, '/security/login')
    
    
    #metodo para listar los generos de las personas
    api.add_resource(PersonGenre, '/security/PersonGenre/list')
    
    
    #===================================================================
    #PERSON
    #===================================================================
    #metodo para listar
    api.add_resource(PersonGet, '/security/Person/list')
    #metodo para crear
    api.add_resource(PersonCreate, '/security/Person/create')
    #metodo para actualizar
    api.add_resource(PersonUpdate, '/security/Person/update')
    #metodo para Eliminar Logicamente
    api.add_resource(PersonLogicDelete, '/security/Person/delete')

    #===================================================================
    #Rol
    #===================================================================
    #metodo para listar
    api.add_resource(RolGet, '/security/Rol/list')
    #metodo para crear
    api.add_resource(RolCreate, '/security/Rol/create')
    #metodo para actualizar
    api.add_resource(RolUpdate, '/security/Rol/update')
    #metodo para Eliminar Logicamente
    api.add_resource(RolLogicDelete, '/security/Rol/delete')
    
    #===================================================================
    #User
    #===================================================================
    #metodo para listar
    api.add_resource(UserGet, '/security/User/list')
    #metodo para crear
    api.add_resource(UserCreate, '/security/User/create')
    #metodo para actualizar
    api.add_resource(UserUpdate, '/security/User/update')
    #metodo para Eliminar Logicamente
    api.add_resource(UserLogicDelete, '/security/User/delete')

    #===================================================================
    #User_Rol
    #===================================================================
    #metodo para listar
    api.add_resource(UserRolGet, '/security/UserRol/list')
    #metodo para crear
    api.add_resource(UserRolCreate, '/security/UserRol/create')
    #metodo para actualizar
    # api.add_resource(RolUpdate, '/security/UserRol/update')
    #metodo para Eliminar Logicamente
    api.add_resource(UserRolLogicDelete, '/security/UserRol/delete')
    
    #metodo para recuperacion de contraseña
    api.add_resource(PasswordRecovery, '/security/recover-password')
    # Metodo para actualizar la contraseña desde el correo
    api.add_resource(EmailPasswordUpdate, '/security/change-password')