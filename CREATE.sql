-- Active: 1689032669311@@127.0.0.1@3306@AvaliaUnB
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
    FOREIGN KEY (fk_codDpto) REFERENCES departamento(codigo) ON DELETE CASCADE
);

CREATE TABLE professor(
    idProfessor BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    nome VARCHAR(70) NOT NULL
);

CREATE TABLE departamento_professor(
    fk_codDpto VARCHAR(4) NOT NULL,
    fk_idProfessor BIGINT NOT NULL,
    FOREIGN KEY (fk_codDpto) REFERENCES departamento(codigo) ON DELETE CASCADE,
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor) ON DELETE CASCADE,
    PRIMARY KEY (fk_codDpto, fk_idProfessor)
);

CREATE TABLE professor_disciplina(
    fk_codDisciplina VARCHAR(15) NOT NULL,
    fk_idProfessor BIGINT NOT NULL,
    FOREIGN KEY (fk_codDisciplina) REFERENCES disciplina(codigo) ON DELETE CASCADE,
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor) ON DELETE CASCADE,
    PRIMARY KEY (fk_codDisciplina, fk_idProfessor) 
);

CREATE TABLE turma(
	periodo VARCHAR(6) NOT NULL,
    horario VARCHAR(200) NOT NULL,
    local VARCHAR(60) NOT NULL,
    numero VARCHAR(10) NOT NULL,
    vagasOcupadas INT NULL,
    totalVagas INT NULL,
    fk_idProfessor BIGINT NOT NULL,
    fk_codDisciplina VARCHAR(15) NOT NULL,
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor) ON DELETE CASCADE, 
    FOREIGN KEY (fk_codDisciplina) REFERENCES disciplina(codigo) ON DELETE CASCADE,
    PRIMARY KEY (periodo, horario, local, fk_idProfessor)
);

CREATE TABLE avaliacao(
    idAvaliacao BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    comentario VARCHAR(240),
    nota ENUM("MIGUÉ", "TRANQUILO", "MÉDIO", "TRABALHOSO", "FOGE") NOT NULL,
    dificuldade ENUM("MUITO FÁCIL", "FÁCIL", "MÉDIO", "DIFÍCIL", "MUITO DIFÍCIL") NOT NULL,
    fk_matricula VARCHAR(9) NOT NULL,
    fk_idProfessor BIGINT NOT NULL,
    fk_periodo VARCHAR(6) NOT NULL,
    fk_local VARCHAR(60) NOT NULL,
	fk_horario VARCHAR(200) NOT NULL,
    FOREIGN KEY (fk_matricula) REFERENCES usuario(matricula) ON DELETE CASCADE,
    FOREIGN KEY (fk_idProfessor) REFERENCES professor(idProfessor),
    FOREIGN KEY (fk_periodo, fk_horario, fk_local) REFERENCES turma(periodo, horario, local) ON DELETE CASCADE
);

CREATE TABLE denuncia(
    idDenuncia BIGINT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    avaliado ENUM("AVALIADA", "NÃO AVALIADA") NOT NULL,
    motivo VARCHAR(240),
    fk_matricula VARCHAR(9) NOT NULL,
    fk_idAvaliacao BIGINT NOT NULL,
    FOREIGN KEY (fk_matricula) REFERENCES usuario(matricula) ON DELETE CASCADE,
    FOREIGN KEY (fk_idAvaliacao) REFERENCES avaliacao(idAvaliacao) ON DELETE CASCADE
);

-- view
-- Active: 1689032669311@@127.0.0.1@3306@AvaliaUnB
CREATE VIEW view_turmas_avaliadas
AS
SELECT professor.nome AS nome, 
       avaliacao.nota AS nota,
       disciplina.nome AS nome_disciplina,
       turma.horario AS horario,
       turma.local AS local,
       turma.fk_codDisciplina AS disciplina
FROM turma
INNER JOIN disciplina ON turma.fk_codDisciplina = disciplina.codigo
INNER JOIN avaliacao ON turma.fk_idProfessor = avaliacao.fk_idProfessor
INNER JOIN professor ON turma.fk_idProfessor = professor.idProfessor;

-- procedure
DELIMITER //
CREATE PROCEDURE pr_disciplinasDoProfessor (IN nome VARCHAR(70))
BEGIN
        SELECT professor.nome, disciplina.nome
        FROM professor, disciplina, professor_disciplina
        WHERE professor.idProfessor = professor_disciplina.fk_idProfessor 
        AND disciplina.codigo = professor_disciplina.fk_codDisciplina
        AND professor.nome = nome;
END//
DELIMITER;

/* DROP DATABASE AvaliaUnB; */