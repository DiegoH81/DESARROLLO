from models.user import User

class UserModel():
    
    @classmethod
    def login(self, user_obj, data_base):
        cursor = data_base.connection.cursor()
        sql = """SELECT id, nombre, user, password, email FROM test_flask.usuarios
                    WHERE user = '{}'""".format(user_obj.user)
        cursor.execute(sql)
        ROW = cursor.fetchone()
        
        print (ROW)
        if ROW != None: #Si existe el usuario
            if (user_obj.password == ROW[3]): #comparo contraseñas
                new_user = User(ROW[0], ROW[1], ROW[2], True, ROW[4]) #Si son iguales, asigna true
            else:
                new_user = User(ROW[0], ROW[1], ROW[2], False, ROW[4]) #Si son diferentes, asigna false
            return new_user
        else:
            return None
    @classmethod
    def register(self, user_obj, data_base):
        cursor = data_base.connection.cursor()
        sql_check_user = """SELECT user FROM test_flask.usuarios
                    WHERE user = '{}'""".format(user_obj.user)
        cursor.execute(sql_check_user)
        ROW = cursor.fetchone()
        
        if ROW != None: #Si existe el usuario
            return False
        else: #Si no existe
            sql_insert_user = """INSERT INTO test_flask.usuarios (nombre, user, password, email)
                                 VALUES ('{}', '{}', '{}', '{}')""".format(user_obj.nombre, user_obj.user, user_obj.password, user_obj.email)
            cursor.execute(sql_insert_user)
            data_base.connection.commit()
            return True
    @classmethod
    def update_profile(self, user_obj, data_base):
        cursor = data_base.connection.cursor()
        sql_update = """UPDATE test_flask.usuarios SET nombre = '{}', user = '{}', password = '{}', email = '{}'
                    WHERE id = '{}'""".format(user_obj.nombre, user_obj.user, user_obj.password, user_obj.email, user_obj.id)
        cursor.execute(sql_update)
        data_base.connection.commit()
        return True
    @classmethod
    def get_by_id(self, data_base, id):
        cursor = data_base.connection.cursor()
        sql = "SELECT id, nombre, user, password, email FROM test_flask.usuarios WHERE id = {}".format(id)
        cursor.execute(sql)
        ROW = cursor.fetchone()
        
        print (ROW)
        if ROW != None: #Si existe el usuario
            return User(ROW[0], ROW[1], ROW[2], ROW[3], ROW[4]) #Reotrno el usuario con los datos cargados
        else:
            return None