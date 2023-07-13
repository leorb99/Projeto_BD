class Avaliacao():
    def __init__(self, id=None, comentario=None, nota=None, 
                 dificuldade=None, fk_matricula=None, fk_idProfessor=None,
                 fk_periodo=None, fk_local=None, fk_horario=None):
        self.id = id
        self.comentario = comentario
        self.nota = nota
        self.dificuldade = dificuldade
        self.fk_matricula = fk_matricula
        self.fk_idProfessor = fk_idProfessor
        self.fk_periodo = fk_periodo
        self.fk_local = fk_local
        self.fk_horario = fk_horario
        