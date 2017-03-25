import web

db_host = 'if0ck476y7axojpg.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name = 'cpdun07s8clcw9v' 
db_user = 'eckpupvq89eivm37'
db_pw   = 'jdfrm2kky75l0hub'

db = web.database(
			dbn='mysql',
			host=db_host,
			db=db_name,
			user=db_user,
			pw=db_pw
			)

def get_productos():
	try:
		return db.select('productoss')
	except:
		return None

def get_producto(id_producto):
	try:
		return db.select('productoss',where ='id_producto=$id_producto',vars = locals())
	except:
		return None

def new_producto(producto,descripcion,existencias,precio_compra,precio_venta,imagen_producto):
    db.insert('productoss',
    producto=producto,
    descripcion= descripcion,
    existencias = existencias, 
    precio_compra= precio_compra,
    precio_venta= precio_venta, 
    imagen_producto= imagen_producto)

def update_producto(id, producto, descripcion, existencias, precio_compra, precio_venta,imagen_producto):
    db.update('productoss', where="id_producto=$id", vars=locals(),
        producto=producto,
        descripcion=descripcion,
        existencias = existencias,
        precio_compra=precio_compra,
        precio_venta=precio_venta,
        imagen_producto = imagen_producto
        )

def delete_producto(id):
    db.delete('productoss', where="id_producto=$id", vars=locals())