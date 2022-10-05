from flask_app.config.mysqlconnection import connectToMySQL

class Usuario:
	def __init__( self , data ):
		self.id = data['id']
		self.nombre = data['nombre']
		self.apellido = data['apellido']
		self.email = data['email']
		self.created_at = data['created_at']
		self.updated_at = data['updated_at']

	def full_name(self):
		return f"{self.nombre} {self.apellido}"

	@classmethod
	def get_all(cls):
		query = "SELECT * FROM users_schema;"
		results = connectToMySQL('usuarios').query_db(query)
		usuarios = []
		for usuario in results:
			usuarios.append( cls(usuario) )
		return usuarios

	@classmethod
	def save(cls, data ):
		query = "INSERT INTO users_schema ( nombre , apellido , email , created_at, updated_at ) VALUES ( %(nombre)s , %(apellido)s , %(email)s , NOW() , NOW() );"
		return connectToMySQL('usuarios').query_db( query, data )

	@classmethod
	def get_one(cls,data):
		query  = "SELECT * FROM users_schema WHERE id = %(id)s";
		result = connectToMySQL('usuarios').query_db(query,data)
		return cls(result[0])

	@classmethod
	def update(cls,data):
		query = "UPDATE users_schema SET nombre=%(nombre)s,apellido=%(apellido)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
		return connectToMySQL('usuarios').query_db(query,data)

	@classmethod
	def destroy(cls,data):
		query  = "DELETE FROM users_schema WHERE id = %(id)s;"
		return connectToMySQL('usuarios').query_db(query,data)