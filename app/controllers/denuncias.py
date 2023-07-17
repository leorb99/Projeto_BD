from app.models import avaliacao_dao, usuario_dao
from app.models import cursor


class Denuncia():
    def __init__(self, idDenuncia=None, avaliado=None, motivo=None,
                 fk_matricula=None, fk_idAvaliacao=None):
        self.idDenuncia = idDenuncia
        self.avaliado = avaliado
        self.motivo = motivo
        self.fk_matricula = fk_matricula
        self.fk_idAvaliacao = fk_idAvaliacao
        self.comentario = ""
        self.denunciado = ""
        
    def setAvaliacao(self):
        avaliacao = avaliacao_dao.AvaliacaoDAO()
        self.comentario = avaliacao.get(cursor, self.fk_idAvaliacao).comentario

    def setDenunciado(self):
        avaliacao = avaliacao_dao.AvaliacaoDAO()
        self.denunciado = avaliacao.get(cursor, self.fk_idAvaliacao).fk_matricula