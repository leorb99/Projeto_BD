USE AvaliaUnB;

-- usuario
INSERT INTO usuario VALUES(
    "190119233", "GABRIEL BARBOSA", "gabigol_matador@hotmail.com", "umasenha", "Educação Física", "ADM", "1996-08-30", NULL, NULL
);
INSERT INTO usuario VALUES(
    "190119210", "BRUNO HENRIQUE", "bh27@hotmail.com", "123", "Comunicação", "COMUM", "1990-12-30", NULL, NULL
);
INSERT INTO usuario VALUES(
    "231005138", "SOFIA", "sofia@hotmail.com", "123senha", "Medicina Veterinária", "COMUM", "2013-09-05", NULL, NULL
);

-- departamento
INSERT INTO departamento VALUES(
    "100", "SERIE A"
);
INSERT INTO departamento VALUES(
    "200", "SERIE B"
);
INSERT INTO departamento VALUES(
    "300", "SERIE C"
);

-- disciplina 
INSERT INTO disciplina VALUES(
    "SRA01", "FUTEBOL 1", "100"
);
INSERT INTO disciplina VALUES(
    "SRB01", "FUTEBOL 2", "200"
);
INSERT INTO disciplina VALUES(
    "SRC01", "FUTEBOL 3", "300"
);

-- professor
INSERT INTO professor VALUES(
    3539, "DORIVAL JUNIOR"
);
INSERT INTO professor VALUES(
    3540, "VANDERLEI LUXEMBURGO"
);
INSERT INTO professor VALUES(
    3541, "FERNANDO DINIZ"
);

INSERT INTO departamento_professor VALUES(
    "100", 3539
);
INSERT INTO departamento_professor VALUES(
    "200", 3540
);
INSERT INTO departamento_professor VALUES(
    "300", 3541
);
-- professor_disciplina
INSERT INTO professor_disciplina VALUES(
    "SRA01", 3539
);
INSERT INTO professor_disciplina VALUES(
    "SRB01", 3540
);
INSERT INTO professor_disciplina VALUES(
    "SRC01", 3541
);
INSERT INTO professor_disciplina VALUES(
    "SRC01", 3540
);

-- turma
INSERT INTO turma VALUES(
    "2023.1", "35T45", "PAT AT - 020", "01", 49, 50, 3539, "SRA01"
);
INSERT INTO turma VALUES(
    "2023.1", "35T45", "CENTRO OLIMPICO", "01", 15, 50, 3540, "SRB01"
);
INSERT INTO turma VALUES(
    "2023.1", "35T45", "ICC ANF. 1", "01", 40, 50, 3541, "SRC01"
);

-- avaliacao
INSERT INTO avaliacao VALUES (
    1, "Excelente pofexo", "MIGUÉ", "MUITO FÁCIL", "190119233", 3540, "2023.1", "CENTRO OLIMPICO", "35T45"
);
INSERT INTO avaliacao VALUES (
    2, "Horrivel esse m#$%@", "FOGE", "MUITO DIFÍCIL", "231005138", 3541, "2023.1", "ICC ANF. 1", "35T45"
);
INSERT INTO avaliacao VALUES (
    4, "esse m#$%@", "TRABALHOSO", "MUITO DIFÍCIL", "190119210", 3541, "2023.1", "ICC ANF. 1", "35T45"
);
INSERT INTO avaliacao VALUES (
    3, "Muito bom", "TRANQUILO", "MUITO FÁCIL", "190119210", 3539, "2023.1", "PAT AT - 020", "35T45"
);

-- denuncia
INSERT INTO denuncia VALUES(
    1, "AVALIADA", NULL, "190119210", 1
);
INSERT INTO denuncia VALUES(
    2, "NÃO AVALIADA", "muito agressivo", "190119210", 2
);
INSERT INTO denuncia VALUES(
    3, "NÃO AVALIADA", NULL, "231005138", 4
);


SELECT * FROM turma WHERE fk_codDisciplina="CIC0099"