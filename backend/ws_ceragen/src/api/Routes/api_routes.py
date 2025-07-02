from ..Services.SecuService import *

def load_routes(api):
    #metodo para el login
    api.add_resource(LoginService, '/security/login')
    
    #===================================================================
    #PERSONGENRE
    #===================================================================
    #metodo para listar los generos de las personas
    api.add_resource(PersonGenreGet, '/security/PersonGenre/list')

    #===================================================================
    #PERSONMARITALSTATUS
    #===================================================================
    #metodo para listar los generos de las personas
    api.add_resource(MaritalStatusGet, '/security/MaritalStatus/list')
    
    #===================================================================
    #PERSON_BlOOD_TYPE
    #===================================================================
    #metodo para listar los generos de las personas
    api.add_resource(BloodTypeGet, '/security/BloodType/list')

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
    #metodo para recuperacion de contraseña
    api.add_resource(PasswordRecovery, '/security/recover-password')
    # Metodo para actualizar la contraseña desde el correo
    api.add_resource(EmailPasswordUpdate, '/security/change-password')

    #===================================================================
    #User_Rol
    #===================================================================
    #metodo para listar
    api.add_resource(UserRolGet, '/security/UserRol/list')
    #metodo para crear
    api.add_resource(UserRolCreate, '/security/UserRol/create')
    #metodo para actualizar
    api.add_resource(UserRolUpdate, '/security/UserRol/update')
    #metodo para Eliminar Logicamente
    api.add_resource(UserRolLogicDelete, '/security/UserRol/delete')
    
    #===================================================================
    #Custom
    #===================================================================
    #metodo para listar
    # api.add_resource(UserRolGet, '/security/UserRol/list')
    #metodo para crear Persona, User, Rol y su tabla de (paciente, cliente, medico)
    api.add_resource(Custom1Create, '/security/custom1/create')

    #=====================================================================
    #Tabla tipo personal medico
    #=====================================================================
    #metodo para listar
    api.add_resource(TypeMedicGet, '/security/TypeMedic/list')
    #metodo para crear
    api.add_resource(TypeMedicCreate, '/security/TypeMedic/create')
    #metodo para actualizar
    api.add_resource(TypeMedicUpdate, '/security/TypeMedic/update')
    #metodo para Eliminar Logicamente
    api.add_resource(TypeMedicLogicDelete, '/security/TypeMedic/delete')
    
    #=====================================================================
    #Tabla personal medico
    #=====================================================================
    #metodo para listar
    api.add_resource(MedicGet, '/security/Medic/list')
    #metodo para crear
    # api.add_resource(MedicCreate, '/security/Medic/create')
    #metodo para actualizar
    api.add_resource(MedicUpdate, '/security/Medic/update')
    #metodo para Eliminar Logicamente
    api.add_resource(MedicLogicDelete, '/security/Medic/delete')

    #=====================================================================
    #Tabla paciente
    #=====================================================================
    #metodo para listar
    api.add_resource(PatientGet, '/security/Patient/list')
    #metodo para crear
    # api.add_resource(PatientCreate, '/security/Patient/create')
    #metodo para actualizar
    api.add_resource(PatientUpdate, '/security/Patient/update')
    #metodo para Eliminar Logicamente
    api.add_resource(PatientLogicDelete, '/security/Patient/delete')
    
    #=====================================================================
    #Tabla Historial Medico
    #=====================================================================
    #metodo para listar
    api.add_resource(MedHistoryGet, '/security/MedHistory/list')
    #metodo para crear
    api.add_resource(MedHistoryCreate, '/security/MedHistory/create')
    #metodo para actualizar
    api.add_resource(MedHistoryUpdate, '/security/MedHistory/update')
    #metodo para Eliminar Logicamente
    api.add_resource(MedHistoryDelete, '/security/MedHistory/delete')
    
    #=====================================================================
    #Tabla Producto
    #=====================================================================
    #metodo para listar
    api.add_resource(ProductGet, '/security/Product/list')
    #metodo para crear
    api.add_resource(ProductCreate, '/security/Product/create')
    #metodo para actualizar
    api.add_resource(ProductUpdate, '/security/Product/update')
    #metodo para Eliminar Logicamente
    api.add_resource(ProductDelete, '/security/Product/delete')

    #=====================================================================
    #Tabla Therapy Type
    #=====================================================================
    #metodo para listar
    api.add_resource(TherapyTypeGet, '/security/TherapyType/list')
    #metodo para crear
    api.add_resource(TherapyTypeCreate, '/security/TherapyType/create')
    #metodo para actualizar
    api.add_resource(TherapyTypeUpdate, '/security/TherapyType/update')
    #metodo para Eliminar Logicamente
    api.add_resource(TherapyTypeDelete, '/security/TherapyType/delete')