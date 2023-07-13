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
/* INSERT INTO disciplina VALUES(
    "MAT0029", "CÁLCULO 4", "518"
);
INSERT INTO disciplina VALUES(
    "CIC0100", "ORGANIZAÇÃO E ARQUITETURA DE COMPUTADORES 2", "508"
);
INSERT INTO disciplina VALUES(
    "CIC0098", "BANDO DE DADOS", "508"
); */
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
    1, "DORIVAL JUNIOR", "100"
);
INSERT INTO professor VALUES(
    2, "VANDERLEI LUXEMBURGO", "200"
);
INSERT INTO professor VALUES(
    3, "FERNANDO DINIZ", "300"
);

-- professor_disciplina
INSERT INTO professor_disciplina VALUES(
    "SRA01", 1
);
INSERT INTO professor_disciplina VALUES(
    "SRB01", 2
);
INSERT INTO professor_disciplina VALUES(
    "SRC01", 3
);
INSERT INTO professor_disciplina VALUES(
    "SRC01", 2
);

-- turma
INSERT INTO turma VALUES(
    "2023.1", "35T45", "PAT AT - 020", "01", 49, 50, 1, "SRA01"
);
INSERT INTO turma VALUES(
    "2023.1", "35T45", "CENTRO OLIMPICO", "01", 15, 50, 2, "SRB01"
);
INSERT INTO turma VALUES(
    "2023.1", "35T45", "ICC ANF. 1", "01", 40, 50, 3, "SRC01"
);

-- avaliacao
INSERT INTO avaliacao VALUES (
    1, "Excelente pofexo", "MIGUÉ", "MUITO FÁCIL", "190119233", "2", "2023.1", "CENTRO OLIMPICO", "35T45"
);
INSERT INTO avaliacao VALUES (
    2, "Horrivel esse m#$%@", "FOGE", "MUITO DIFÍCIL", "231005138", "3", "2023.1", "ICC ANF. 1", "35T45"
);
INSERT INTO avaliacao VALUES (
    4, "esse m#$%@", "TRABALHOSO", "MUITO DIFÍCIL", "190119210", "3", "2023.1", "ICC ANF. 1", "35T45"
);
INSERT INTO avaliacao VALUES (
    3, "Muito bom", "TRANQUILO", "MUITO FÁCIL", "190119210", "1", "2023.1", "PAT AT - 020", "35T45"
);

-- denuncia
INSERT INTO denuncia VALUES(
    1, "AVALIADA", NULL, "190119210", 1
);
INSERT INTO denuncia VALUES(
    2, "NÃO AVALIADA", "muito agressivo", "190119233", 2
);
INSERT INTO denuncia VALUES(
    3, "NÃO AVALIADA", NULL, "190119210", 4
);



INSERT INTO usuario (matricula, nome, email, senha, curso, privilegio, dataNascimento, foto)
VALUES ('12345', 'João', 'joao@example.com', '123456', 'CIC', 'COMUM', '1999-09-01', X'89504E470D0A1A0A0000000D49484452000000800000008008060')
