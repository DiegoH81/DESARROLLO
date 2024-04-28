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
