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
        return (senha == senha_correta[0]) if senha_correta else None
    
    def get_usr(self, matricula):
        self.usr_dao = usuario_dao.UsuarioDAO()
        Usuario = self.usr_dao.get(cursor, matricula)
        return Usuario

    def __json__(self):
        return {
            "matricula": self.matricula,
            "nome": self.nome,
            "email":self.email,
            "senha":self.senha,
            "curso":self.curso,
            "privilegio":self.privilegio,
            "dataNascimento":self.dataNascimento,
            "idade":self.idade,
            "foto":self.foto
        }