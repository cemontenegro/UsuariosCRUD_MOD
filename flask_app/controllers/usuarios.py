from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.usuario import Usuario


@app.route('/')
def index():
	return redirect('/usuarios')

@app.route("/usuarios")
def usuarios():
	usuarios = Usuario.get_all()
	print(usuarios)
	return render_template("usuarios.html", usuarios=usuarios)

@app.route('/usuario/nuevo', methods=["GET"])
def nuevo_form():
	return render_template("nuevo.html")

@app.route('/usuario/crear', methods=["POST"])
def nuevo():
	data = {
		"nombre": request.form["nombre"],
		"apellido" : request.form["apellido"],
		"email" : request.form["email"]
	}
	usuario_id=Usuario.save(data)
	return redirect('/usuario/vista_usuario/' +  str(usuario_id))

@app.route('/usuario/editar_usuario/<int:id>')
def edit(id):
	data ={ 
		"id":id
	}
	return render_template("editar_usuario.html",one_usuario=Usuario.get_one(data))

@app.route('/usuario/vista_usuario/<int:id>')
def show(id):
	data ={ 
		"id":id
	}
	return render_template("vista_usuario.html",one_usuario=Usuario.get_one(data))

@app.route('/usuario/actualizacion',methods=['POST'])
def update():
	Usuario.update(request.form)
	return redirect('/usuarios')

@app.route('/usuario/destroy/<int:id>')
def destroy(id):
	data ={
		'id': id
	}
	Usuario.destroy(data)
	return redirect('/usuarios')