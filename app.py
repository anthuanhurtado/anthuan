import web
import model

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View',
    '/new', 'New',
    '/delete/(\d+)', 'Delete',
    '/edit/(\d+)', 'Edit',
)

t_globals = {
    'datestr': web.datestr
}

render = web.template.render('templates', base='base', globals=t_globals)


class Index:
    def GET(self):
        productos = model.get_productos()       
        return render.index(productos)

class View:
    def GET(self, id):
        id_producto = int(id)
        producto = model.get_producto(id_producto)
        return render.view(producto)

class New:
    form = web.form.Form(
        web.form.Textbox('producto', web.form.notnull, 
            size=30, description="Producto"),
        web.form.Textbox('descripcion', web.form.notnull, 
            size=30, description="Descripcion"),
        web.form.Textbox('existencias', web.form.notnull, 
            size=30, description="Existencias"),
        web.form.Textbox('precio_compra', web.form.notnull, 
            size=30, description="Precio Compra"),
        web.form.Textbox('precio_venta', web.form.notnull, 
            size=30, description="Precio Compra"),
        web.form.File('imagen_producto', web.form.notnull,
            size=30, description="Imagen del producto:"),
        web.form.Button('Registrar'),
    )

    def GET(self):
        form = self.form()
        return render.new(form)

    def POST(self):

        form = self.form()
        form =web.input()
        imagen = web.input(imagen_producto={})

        filedir  ='static/files'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]

        fout = open(filedir +'/'+ filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename

        if not form.validates():
            return render.new_producto(form)
        model.new_producto(
        form['producto'],
        form['descripcion'],
        form['existencias'],
        form['precio_compra'],
        form['precio_venta'],
        form['imagen_producto']
        )
        raise web.seeother('/')

class Delete:
    def GET(self, id):
    	id_producto = int(id)
        producto = model.get_producto(id_producto)
        model.del_producto(id_producto)
        raise web.seeother('/')

class Edit:
    def GET(self, id):
        post = model.get_producto(int(id))
        form = New.form()
        form.fill(post)
        return render.edit(post, form)
        
    def POST(self, id):
        form = New.form()
        imagen = web.input(imagen_producto={})
        filedir = 'static/images'
        filepath = imagen.imagen_producto.filename.replace('\\','/')
        filename = filepath.split('/')[-1]
#copiar archivo al servidor
        fout= open(filedir+'/'+filename,'w')
        fout.write(imagen.imagen_producto.file.read())
        fout.close()
        imagen_producto = filename
        post = model.get_producto(int(id))
        if not form.validates():
            return render.edit(post, form)
        model.update_producto(int(id), form.d.producto, form.d.descripcion, form.d.existencias, form.d.precio_compra, form.d.precio_venta, imagen_producto)
        raise web.seeother('/')

class Borrar:
    def GET(self, id):
        post = model.get_producto(int(id))
        return render.delete(post)
    
    def POST(self, id):
        model.delete_producto(int(id))
        raise web.seeother('/')

app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()