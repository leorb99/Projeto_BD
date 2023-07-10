CREATE DATABASE AvaliaUnB;

USE AvaliaUnB;
CREATE TABLE usuario(
    matricula CHAR(9) NOT NULL PRIMARY KEY,
    nome VARCHAR(70) NOT NULL,
    email VARCHAR(70) NOT NULL,
    senha VARCHAR(45) NOT NULL,
    curso VARCHAR(70) NOT NULL,
    privilegio ENUM("ADM", "COMUM") NOT NULL,
    dataNascimento DATE NOT NULL,
    idade INT NULL,
    foto BLOB NULL
);
CREATE TRIGGER tr_idade BEFORE INSERT
ON usuario
FOR EACH ROW
SET NEW.idade = FLOOR(DATEDIFF(CURDATE(), NEW.dataNascimento) / 365);



CREATE TABLE departamento(
    codigo VARCHAR(4) NOT NULL PRIMARY KEY,
    nome VARCHAR(145) NOT NULL
);

CREATE TABLE disciplina(
    codigo VARCHAR(15) NOT NULL PRIMARY KEY,
    nome VARCHAR(125) NOT NULL,
    fk_codDpto VARCHAR(4) NOT NULL,
    FOREIGN KEY (fk_codDpto) REFERENCES departamento(codigo)
);

CREATE TABLE professor(
    idProfessor BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(70) NOT NULL,
    fk_codDpto VARCHAR(4) NOT NULL,
    fk_codDisciplina VARCHAR(15) NULL,
    FOREIGN KEY (fk_codDpto) REFERENCES departamento(codigo),
    FOREIGN KEY (fk_codDisciplina) REFERENCES disciplina(codigo)
);

CREATE TABLE turma(
	periodo VARCHAR(6) NOT NULL,
    horario VARCHAR(105) NOT NULL,
    local VARCHAR(60) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    vagasOcupadas INT NULL,
    totalVagas INT NULL,
    fk_idProfessor BIGINT NOT NULL,
    fk_codDisciplina VARCHAR(10) NOT NULL,
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor),
    FOREIGN KEY (fk_codDisciplina) REFERENCES disciplina(codigo),
    PRIMARY KEY (periodo, horario, local, fk_idProfessor)
);

CREATE TABLE avaliacao(
    idAvaliacao BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    comentario VARCHAR(240),
    nota ENUM("MINGUÉ", "TRANQUILO", "MÉDIO", "TRABALHOSO", "FOGE") NOT NULL,
    dificuldade ENUM("MUITO FÁCIL", "FÁCIL", "MÉDIO", "DIFÍCIL", "MUITO DIFÍCIL") NOT NULL,
    fk_matricula VARCHAR(9) NOT NULL,
    fk_idProfessor BIGINT NOT NULL,
    fk_periodo VARCHAR(6) NOT NULL,
    fk_local VARCHAR(60) NOT NULL,
	fk_horario VARCHAR(105) NOT NULL,
    FOREIGN KEY (fk_matricula) REFERENCES usuario(matricula),
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor),
    FOREIGN KEY (fk_periodo, fk_horario, fk_local) REFERENCES turma(periodo, horario, local)
);

CREATE TABLE denuncia(
    idDenuncia BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    avaliado ENUM("AVALIADA", "NÃO AVALIADA") NOT NULL,
    motivo VARCHAR(240),
    fk_matricula VARCHAR(9) NOT NULL,
    fk_idAvaliacao BIGINT NOT NULL,
    FOREIGN KEY (fk_matricula) REFERENCES usuario(matricula),
    FOREIGN KEY (fk_idAvaliacao) REFERENCES avaliacao(idAvaliacao)
);

