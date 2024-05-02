from models.producto import Product
class ProductModel():
    #Crear producto
    @classmethod
    def create_product(self, data_base, product_obj):
        cursor = data_base.connection.cursor()
        sql_insert_product = """INSERT INTO test_flask.productos (id_usuario, nombre_producto, decripcion, precio, foto)
                                 VALUES ('{}', '{}', '{}', '{}', '{}')""".format(product_obj.user_id, product_obj.nombre, product_obj.descripcion, product_obj.precio, product_obj.product_pic)
        cursor.execute(sql_insert_product)
        data_base.connection.commit()
        return True
    
    @classmethod
    def get_by_id(self, data_base, id):
        cursor = data_base.connection.cursor()
        sql_get_id = "SELECT id, id_usuario, nombre_producto, decripcion, precio, foto FROM test_flask.productos WHERE id = {}".format(id)
        cursor.execute(sql_get_id)
        ROW = cursor.fetchone()
        
        if ROW != None: #Si existe el producto
            return Product(ROW[0], ROW[1], ROW[2], ROW[3], ROW[4], ROW[5]) #Reotrno el producto con los datos cargados
        else:
            return None
    
    #Actualizar
    @classmethod
    def update_product(self, data_base, product_obj):
        cursor = data_base.connection.cursor()
        sql_update = """UPDATE test_flask.productos SET nombre_producto = '{}', descripcion = '{}', precio = {}
                        WHERE id = '{}'""".format(product_obj.nombre, product_obj.descripcion, product_obj.precio, product_obj.id)
        cursor.execute(sql_update)
        data_base.connection.commit()
        return True

    #Borrar
    @classmethod
    def delete_product(self, data_base, id):
        cursor = data_base.connection.cursor()
        sql_delete = "DELETE FROM test_flask.productos WHERE id = {}".format(id)
        cursor.execute(sql_delete)
        data_base.connection.commit()
        return True