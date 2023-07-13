from app import app
from flask import render_template, request, redirect
from . import avaliacoes, denuncias, departamentos, disciplinas, professor_disciplina, professores, turmas, usuarios
from app.models import con, cursor, avaliacao_dao, usuario_dao, professor_disciplina_dao
from app.models import departamente_dao, disciplina_dao, professor_dao, denuncia_dao, turma_dao
import json

user = usuarios.Usuario()
rate = avaliacoes.Avaliacao()


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login(usr=user):
    if request.method == "POST":
        matricula = request.form["matricula"]
        senha = request.form["senha"]
        usr.matricula = matricula
        usr.senha = senha
        if usr.valida_senha(matricula, senha):
            usr = usr.get_usr(matricula)
            user.nome = usr.nome
            user.email = usr.email
            user.senha = usr.senha
            user.curso = usr.curso
            user.privilegio = usr.privilegio
            user.dataNascimento = usr.dataNascimento
            user.idade = usr.idade
            user.foto = usr.foto
            if usr.privilegio == "ADM":
                return redirect("profile_adm")
            return redirect("profile")
        else:
            return render_template("login.html", error="Senha incorreta.")
    else:
        return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup(usr=user):
    if request.method == "POST":
        matricula = request.form["matricula"]
        usr = usr.get_usr(matricula)
        if usr == None:
            usuario = request.form
            foto = request.files["foto"]
            foto_bin = foto.read()
            user.matricula = matricula
            user.nome = usuario["nome"]
            user.email = usuario["email"]
            user.senha = usuario["senha"]
            user.curso = usuario["curso"]
            user.privilegio = usuario["privilegio"]
            user.dataNascimento = usuario["dataNascimento"]
            create_user = usuario_dao.UsuarioDAO()
            create_user.create(cursor, usuario, foto_bin)
            return redirect("profile")
        else:
            return render_template("login.html", error="Usuário já cadastrado.")
    else:
        return render_template("signup.html")

@app.route("/profile", methods=["GET", "POST"])
def profile():  # editar, excluir    
    return render_template("profile.html", user=user)

@app.route("/profile_adm", methods=["GET"])
def profile_adm():  # editar, excluir
    return render_template("profile_adm.html", user=user)
    
@app.route("/profile/update", methods=["GET", "POST"])
def profile_update(usr=user):
    if request.method == "POST":
        usuario = request.form
        update_user = usuario_dao.UsuarioDAO()
        update_user.update(cursor, usuario)
        return redirect("/profile")
    else:
        return render_template("profile_update.html", user=user)

@app.route("/delete-account", methods=["POST"])
def delete_account():
    delete_user = usuario_dao.UsuarioDAO()
    delete_user.delete(cursor, user.matricula)    
    return redirect("/")

@app.route("/classes/")
def classes(): # estudante cria, mas n remove nem edita
    return render_template("classes.html")

@app.route("/classes/update")
def classes_update(): # estudante cria, mas n remove nem edita
    return render_template("classe_update.html")

@app.route("/classes/add")
def classes_add(): # estudante cria, mas n remove nem edita
    return render_template("classes_add.html")

@app.route("/classes/rate", methods=["GET", "POST"])
def classes_rate(usr=user):
    if request.method == "POST":
        professor = professor_dao.ProfessorDAO()
        avaliacao = dict(request.form)
        avaliacao["fk_matricula"] = user.matricula
        rate.comentario = avaliacao["comentario"]
        rate.dificuldade = avaliacao["dificuldade"]
        rate.nota = avaliacao["nota"]
        rate.fk_horario = avaliacao["fk_horario"]
        rate.fk_periodo = avaliacao["fk_periodo"]
        rate.fk_local = avaliacao["fk_local"]
        rate.fk_matricula = user.matricula
        prof = professor.getNomeProf(cursor, avaliacao["fk_idProfessor"].upper())
        rate.fk_idProfessor = prof.idProfessor
        avaliacao["fk_idProfessor"] = prof.idProfessor
        create_rate = avaliacao_dao.AvaliacaoDAO()
        create_rate.create(cursor, avaliacao)
        return redirect("/profile")
        
    return render_template("classes_rate.html")

@app.route("/classes/rate/update")
def classes_rate_update(): # estudante cria, mas n remove nem edita
    return render_template("classes_rate_update.html")

@app.route("/view")
def view():
    return "view"
app.run(host='127.0.0.1', port=4002)
