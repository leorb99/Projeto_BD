from app.models import usuario_dao, cursor
from app import bcrypt, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Usuario.get_id(user_id)

class Usuario(UserMixin):
    def __init__(self, matricula=None, nome=None, email=None, senha=None,
                 curso=None, privilegio=None, dataNascimento=None, 
                 idade=None, foto=None):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.senha = senha
        self.curso = curso
        self.privilegio = privilegio
        self.dataNascimento = dataNascimento
        self.idade = idade
        self.foto = foto
        self.usr_dao = usuario_dao.UsuarioDAO()  

    def valida_senha(self, senha):
        return bcrypt.check_password_hash(self.senha, senha)
    
    def get_id(self):
        return self
    
    def get_usr(self, matricula):
        self.usr_dao = usuario_dao.UsuarioDAO()
        Usuario = self.usr_dao.get(cursor, matricula)
        return Usuario

    def get_usr_email(self, email):
        self.usr_dao = usuario_dao.UsuarioDAO()
        Usuario = self.usr_dao.get_email(cursor, email)
        return Usuario