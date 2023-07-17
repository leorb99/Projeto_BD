from app.models import professor_dao, disciplina_dao, cursor

class Turma():
    def __init__(self, periodo=None, horario=None, local=None, numero=None, 
                 vagasOcupadas=None, totalVagas=None, fk_idProfessor=None,
                 fk_codDisciplina=None):
        self.periodo = periodo
        self.horario = horario
        self.local = local
        self.numero = numero
        self.vagasOcupadas = vagasOcupadas
        self.totalVagas = totalVagas
        self.fk_idProfessor = fk_idProfessor
        self.fk_codDisciplina = fk_codDisciplina
        self.professor = ""
        self.nome_disciplina = ""
        
    def setProf(self):
        prof = professor_dao.ProfessorDAO()
        self.professor = prof.get(cursor, self.fk_idProfessor).nome
        
    def setNomeDisciplina(self):
        nome_disciplina = disciplina_dao.DisciplinaDAO()
        self.nome_disciplina = nome_disciplina.get(cursor, self.fk_codDisciplina).nome