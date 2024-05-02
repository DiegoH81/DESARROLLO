class Product():
    id = 0
    user_id = 0
    nombre = ""
    descripcion = ""
    precio = 0
    
    def __init__(self, in_id, in_user_id, in_nombre, in_descripcion, in_precio):
        self.id = in_id
        self.user_id = in_user_id
        self.nombre = in_nombre
        self.descripcion = in_descripcion
        self.precio = in_precio
        
    