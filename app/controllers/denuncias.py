class Denuncia():
    def __init__(self, idDenuncia=None, avaliado=None, motivo=None,
                 fk_matricula=None, fk_idAvaliacao=None):
        self.idDenuncia = idDenuncia
        self.avaliado = avaliado
        self.motivo = motivo
        self.fk_matricula = fk_matricula
        self.fk_idAvaliacao = fk_idAvaliacao