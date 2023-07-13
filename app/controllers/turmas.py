class Turma():
    def __init__(self, periodo=None, horario=None, local=None, numero=None, 
                 vagasOcupadas=None, totalVagas=None, fk_idProfessor=None):
        self.periodo = periodo
        self.horario = horario
        self.local = local
        self.numero = numero
        self.vagasOcupadas = vagasOcupadas
        self.totalVagas = totalVagas
        self.fk_idProfessor = fk_idProfessor
