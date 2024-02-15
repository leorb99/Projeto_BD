from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, EmailField, FileField, TextAreaField, SelectField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from . import usuarios
cursos = [
    "Administração",
    "Agronomia",
    "Arquitetura e Urbanismo",
    "Arquivologia",
    "Artes Cênicas",
    "Artes Visuais",
    "Biblioteconomia",
    "Biotecnologia",
    "Ciência da Computação (bacharelado)",
    "Ciência Política",
    "Ciências Ambientais",
    "Ciências Biológicas",
    "Ciências Contábeis",
    "Ciências Econômicas",
    "Ciências Farmacêuticas",
    "Ciências Sociais",
    "Computação (licenciatura)",
    "Comunicação Organizacional",
    "Comunicação Social - Publicidade e Propaganda",
    "Comunicação Social - Audiovisual",
    "Design",
    "Direito",
    "Educação Física",
    "Enfermagem e Obstetrícia",
    "Engenharia Ambiental",
    "Engenharia Civil",
    "Engenharia de Computação",
    "Engenharia de Redes de Comunicação",
    "Engenharia de Produção",
    "Engenharia Elétrica",
    "Engenharia Florestal",
    "Engenharia Mecânica",
    "Engenharia Mecatrônica",
    "Engenharia Química",
    "Estatística",
    "Filosofia",
    "Física",
    "Geofísica",
    "Geografia",
    "Geologia",
    "Gestão de Políticas Públicas",
    "Gestão de Agronegócio",
    "História",
    "Jornalismo",
    "Letras",
    "Matemática",
    "Medicina",
    "Medicina Veterinária",
    "Museologia",
    "Música",
    "Nutrição",
    "Odontologia",
    "Pedagogia",
    "Psicologia",
    "Química",
    "Química Tecnológica",
    "Relações Internacionais",
    "Saúde Coletiva",
    "Serviço Social",
    "Teoria, Crítica e História da Arte",
    "Turismo",
    "Enfermagem - CEIILÂNDIA",
    "Farmácia - CEIILÂNDIA",
    "Fisioterapia - CEIILÂNDIA",
    "Fonoaudiologia - CEIILÂNDIA",
    "Saúde Coletiva - CEIILÂNDIA",
    "Terapia Ocupacional - CEIILÂNDIA",
    "Engenharia Aeroespacial - GAMA",
    "Engenharia Automotiva - GAMA",
    "Engenharia de Energia - GAMA",
    "Engenharia de Software - GAMA",
    "Engenharia Eletrônica - GAMA",
    "Ciências Naturais - PLANALTINA",
    "Educação do Campo - PLANALTINA",
    "Gestão Ambiental - PLANALTINA",
    "Gestão do Agronegócio - PLANALTINA"
]
notas = ["MIGUÉ", "TRANQUILO", "MÉDIO", "TRABALHOSO", "FOGE"]
niveis_dificuldade = ["MUITO FÁCIL", "FÁCIL", "MÉDIO", "DIFÍCIL", "MUITO DIFÍCIL"]

class LoginForm(FlaskForm):
    matricula = StringField(label="Matrícula:", validators=[DataRequired()])
    senha = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    submit = SubmitField(label="Entrar")
    
class SignupForm(FlaskForm):
    
    def validate_matricula(self, matricula_verificada):
        matricula = usuarios.Usuario().get_usr(matricula_verificada.data)
        if matricula:
            raise ValidationError("Matrícula já está cadastrada")
    
    def validate_email(self, email_verificado):
        email = usuarios.Usuario().get_usr_email(email_verificado.data)
        if email:
            raise ValidationError("Email já está cadastrado")
        
    matricula = StringField(label="Matrícula:", validators=[DataRequired()])
    nome = StringField(label="Nome:", validators=[DataRequired()])
    email = EmailField(label="Email:", validators=[Email(), DataRequired()])
    senha = PasswordField(label="Senha:", validators=[Length(min=6), DataRequired()])
    senha_confirmada = PasswordField(label="Confirmar Senha:", validators=[EqualTo("senha"), DataRequired()])
    curso = SelectField(label="Curso:", choices=cursos, validators=[DataRequired()]) 
    data_nascimento = DateField(label="Data de nascimento:", validators=[DataRequired()])
    foto = FileField(label="Foto:")
    submit = SubmitField(label="Cadastrar")
    
class AddClass(FlaskForm):
    periodo = StringField(label="Período:", validators=[DataRequired()])
    horario = StringField(label="Horário:", validators=[DataRequired()])
    local = StringField(label="Local:", validators=[DataRequired()])
    numero = StringField(label="Número:", validators=[DataRequired()])
    professor = StringField(label="Nome do(a) Professor(a):", validators=[DataRequired()])
    cod_disciplina = StringField(label="Código da Disciplina:", validators=[DataRequired()])
    submit = SubmitField(label="Adicionar Turma")
    
class RateClass(FlaskForm):
    comentario = TextAreaField(label="Comentário:")
    nota = SelectField(label="Nota:", choices=notas, validators=[DataRequired()])
    dificuldade = SelectField(label="Dificuldade:", choices=niveis_dificuldade, validators=[DataRequired()])
    nome_professor = StringField(label="Nome do(a) Professor(a):", validators=[DataRequired()])
    periodo = StringField(label="Período:", validators=[DataRequired()])
    horario = StringField(label="Horário:", validators=[DataRequired()])
    local = StringField(label="Local:", validators=[DataRequired()])
    submit = SubmitField(label="Enviar Avaliação")
 
class EditRate(FlaskForm):
    comentario = TextAreaField(label="Comentário:")
    nota = SelectField(label="Nota:", choices=notas, validators=[DataRequired()])
    dificuldade = SelectField(label="Dificuldade:", choices=niveis_dificuldade, validators=[DataRequired()])
    submit = SubmitField(label="Editar Avaliação")

class EditProfile(FlaskForm):
    matricula = StringField(label="Matrícula:", validators=[DataRequired()])
    nome = StringField(label="Nome:", validators=[DataRequired()])
    email = EmailField(label="Email:")
    curso = SelectField(label="Curso:", choices=cursos, validators=[DataRequired()])
    foto = FileField(label="Foto:")
    submit = SubmitField(label="Atualizar Perfil")
    delete = SubmitField(label="Excluir Conta")