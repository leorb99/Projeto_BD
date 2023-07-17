from app.models import professor_dao, turma_dao, disciplina_dao, cursor

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
        self.professor = ""
        self.disciplina = ""
        
    def setProfessor(self):
        prof = professor_dao.ProfessorDAO()
        self.professor = prof.get(cursor, self.fk_idProfessor).nome
        
    def setDisciplina(self):
        turma = turma_dao.TurmaDAO()
        disciplina = disciplina_dao.DisciplinaDAO()
        codDisciplina = turma.getDisciplina(cursor, self.fk_idProfessor,
                                              self.fk_horario, self.fk_local,
                                              self.fk_periodo)
        self.disciplina = disciplina.getNome(cursor, codDisciplina)[0]
        
    def setIDProfessor(self):
        prof = professor_dao.ProfessorDAO()
        self.fk_idProfessor = prof.getID(cursor, self.professor).idProfessor