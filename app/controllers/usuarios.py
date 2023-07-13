from app.models import usuario_dao, cursor

class Usuario():
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

    def valida_senha(self, matricula, senha):
        self.usr_dao = usuario_dao.UsuarioDAO()
        senha_correta = self.usr_dao.get_pass(cursor, matricula)
        return senha == senha_correta[0]
    
    def get_usr(self, matricula):
        self.usr_dao = usuario_dao.UsuarioDAO()
        Usuario = self.usr_dao.get(cursor, matricula)
        return Usuario
    
    def to_dict(self):
            return self.__dict__