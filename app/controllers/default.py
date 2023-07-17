import base64
import os
from app import app
from flask import render_template, request, redirect
from . import avaliacoes, denuncias, departamentos, disciplinas, professor_disciplina, professores
from . import turmas, usuarios, departamento_professor
from app.models import con, cursor, avaliacao_dao, usuario_dao, professor_disciplina_dao, view_dao
from app.models import departamente_dao, disciplina_dao, professor_dao, denuncia_dao, turma_dao


def convertImageToBinary(img):
    with open(os.path.dirname(os.path.abspath(__file__)) + img, "rb") as f_img:
        binary = f_img.read()
    return binary


foto = convertImageToBinary("/../../images/generic_user.png")
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
        elif usr.get_usr(matricula) is None:
            return render_template("login.html", error="Usuário não cadastrado.")
        else:
            return render_template("login.html", error="Senha incorreta.")
    else:
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup(usr=user):
    if request.method == "POST":
        matricula = request.form["matricula"]
        usr = usr.get_usr(matricula)
        if usr is None:
            usuario = request.form
            foto = request.files["foto"]
            foto_bin = foto.read()
            user.foto = foto_bin
            if not foto:
                user.foto = convertImageToBinary("/../../images/generic_user.png")
            user.matricula = matricula
            user.nome = usuario["nome"]
            user.email = usuario["email"]
            user.senha = usuario["senha"]
            user.curso = usuario["curso"]
            user.privilegio = usuario["privilegio"]
            user.dataNascimento = usuario["dataNascimento"]
            create_user = usuario_dao.UsuarioDAO()
            create_user.create(cursor, user, foto_bin)
            return redirect("profile")
        return render_template("login.html", error="Usuário já cadastrado.")
    else:
        return render_template("signup.html")


@app.route("/profile", methods=["GET", "POST"])
def profile(foto=foto):
    avaliacao = avaliacao_dao.AvaliacaoDAO()
    avaliacoes = avaliacao.getMy(cursor, user.matricula)
    for i in range(len(avaliacoes)):
        avaliacoes[i].setProfessor()
        avaliacoes[i].setDisciplina()
    if not user.foto:
        user.foto = foto
        base64_data = base64.b64encode(foto).decode('utf-8')
        return render_template("profile.html", user=user, base64_data=base64_data,
                               avaliacoes=avaliacoes)
    base64_data = base64.b64encode(user.foto).decode('utf-8')
    return render_template("profile.html", user=user, base64_data=base64_data,
                           avaliacoes=avaliacoes)


@app.route("/profile_adm", methods=["GET", "POST"])
def profile_adm(foto=foto):
    denuncia = denuncia_dao.DenunciaDAO()
    denuncias = denuncia.getNaoAvaliado(cursor)
    for i in range(len(denuncias)):
        denuncias[i].setAvaliacao()
        denuncias[i].setDenunciado()
    avaliacao = avaliacao_dao.AvaliacaoDAO()
    avaliacoes = avaliacao.getMy(cursor, user.matricula)
    for i in range(len(avaliacoes)):
        avaliacoes[i].setProfessor()
        avaliacoes[i].setDisciplina()
    if not user.foto:
        user.foto = foto
        base64_data = base64.b64encode(foto).decode('utf-8')
        return render_template("profile_adm.html", user=user, base64_data=base64_data,
                               denuncias=denuncias, avaliacoes=avaliacoes)
    base64_data = base64.b64encode(user.foto).decode('utf-8')
    return render_template("profile_adm.html", user=user, base64_data=base64_data,
                           denuncias=denuncias, avaliacoes=avaliacoes)


@app.route("/profile/update", methods=["GET", "POST"])
def profile_update(foto=foto):
    base64_data = base64.b64encode(user.foto).decode('utf-8')
    if request.method == "POST":
        if not user.foto:
            base64_data = base64.b64encode(foto).decode('utf-8')
            return render_template("profile_update.html", user=user, base64_data=base64_data)
        return redirect("/profile")
    else:
        return render_template("profile_update.html", user=user, base64_data=base64_data)


@app.route("/profile/update/adm", methods=["GET", "POST"])
def profile_update_adm(foto=foto):
    base64_data = base64.b64encode(user.foto).decode('utf-8')
    if request.method == "POST":
        if not user.foto:
            base64_data = base64.b64encode(foto).decode('utf-8')
            return render_template("profile_update_adm.html", user=user, base64_data=base64_data)
        return redirect("/profile_adm")
    else:
        return render_template("profile_update.html", user=user, base64_data=base64_data)


@app.route("/user/update", methods=["GET", "POST"])
def user_update():
    if request.method == "POST":
        usuario = request.form
        user.nome = usuario["nome"]
        user.email = usuario["email"]
        user.senha = usuario["senha"]
        user.curso = usuario["curso"]
        foto = request.files["foto"]
        foto_bin = foto.read()
        if foto.filename == "":
            foto_bin = user.foto
        user.foto = foto_bin
        update_user = usuario_dao.UsuarioDAO()
        update_user.update(cursor, user, foto_bin)
        if user.privilegio == "ADM":
            return redirect("/profile_adm")
        return redirect("/profile")


@app.route("/delete_account/user_denounced=<int:user_denounced>", methods=["POST", "GET"])
@app.route("/delete_account", defaults={"user_denounced": None}, methods=["POST", "GET"])
def delete_account(user_denounced):
    delete_user = usuario_dao.UsuarioDAO()
    if user_denounced:
        user.matricula = user_denounced
        delete_user.delete(cursor, user.matricula)
        return redirect("/profile_adm")
    delete_user.delete(cursor, user.matricula)
    return redirect("/")


@app.route("/ignore_report/denuncia_id=<int:denuncia_id>", methods=["POST", "GET"])
def ignore_report(denuncia_id):
    denuncia = {"avaliado": "AVALIADA", "idDenuncia": denuncia_id}
    update_denuncia = denuncia_dao.DenunciaDAO()
    update_denuncia.update(cursor, denuncia)
    return redirect("/profile_adm")

@app.route("/delete_comment/rate_id=<int:fk_idAvaliacao>", methods=["POST", "GET"])
# @app.route("/delete_comment", defaults={"fk_idAvaliacao": None}, methods=["POST", "GET"])
def delete_comment(fk_idAvaliacao):
    delete_rate = avaliacao_dao.AvaliacaoDAO()
    # if fk_idAvaliacao:
    delete_rate.delete(cursor, fk_idAvaliacao)
    if user.privilegio == "ADM":
        return redirect("/profile_adm")
    return redirect("/profile")    


@app.route("/classes/")
def classes(): 
    return render_template("classes.html")


@app.route("/classes_search/")
def classes_search():
    cod_disciplina = request.args.get("codigo")
    turma = turma_dao.TurmaDAO()
    turmas = turma.getTurmas(cursor, cod_disciplina)
    for turma in turmas:
        turma.setProf()
    turma.setNomeDisciplina()
    nome_disciplina = turma.nome_disciplina
    return render_template("classes.html", turmas=turmas, nome_disciplina=nome_disciplina)


@app.route("/classes_rate/", methods=["POST"])
def classes_rate():
    if request.method == "POST":
        info = request.form
        avaliacao = avaliacoes.Avaliacao(
            id=None, comentario=info["comentario"], nota=info["nota"],
            dificuldade=info["dificuldade"], fk_matricula=user.matricula, 
            fk_periodo=info["periodo"], fk_local=info["local"], fk_horario=info["horario"]
        )
        avaliacao.professor = info["professor"]
        avaliacao.setIDProfessor()
        create_rate = avaliacao_dao.AvaliacaoDAO()
        create_rate.create(cursor, avaliacao)
        return redirect("/profile")
    return render_template("classes_rate.html")


@app.route("/classes/rate/update/rate_id=<int:id>", methods=["GET", "POST"])
def classes_rate_update(id):
    update_rate = avaliacao_dao.AvaliacaoDAO()
    avaliacao = update_rate.get(cursor, id)
    return render_template("classes_rate_update.html", avaliacao=avaliacao)


@app.route("/update_rate/rateid=<int:id>", methods=["GET", "POST"])
def update_rate(id):
    info = request.form
    update_rate = avaliacao_dao.AvaliacaoDAO()
    avaliacao = avaliacoes.Avaliacao()
    avaliacao.comentario = info["comentario"]
    avaliacao.nota = info["nota"]
    avaliacao.dificuldade = info["dificuldade"]
    avaliacao.id = id
    update_rate.update(cursor, avaliacao)
    if user.privilegio == "ADM":
        return redirect("/profile_adm")
    return redirect("/profile")


@app.route("/classes_info/", methods=["GET", "POST"])
def classes_info():
    info = request.args.to_dict()
    turma = turmas.Turma()
    turma.periodo = info["periodo"]
    turma.horario = info["horario"]
    turma.local = info["local"]
    turma.fk_idProfessor = info["idProfessor"]
    turma.setProf()
    return render_template("classes_rate.html", turma=turma)

@app.route("/rates/", methods=["GET", "POST"])
def rates():
    info = request.args.to_dict()
    avaliacao = avaliacoes.Avaliacao()
    avaliacao.fk_horario = info["horario"]
    avaliacao.fk_idProfessor = info["idProfessor"]
    avaliacao.fk_local = info["local"]
    avaliacao.fk_periodo = info["periodo"]
    show_rates = avaliacao_dao.AvaliacaoDAO()
    rates = show_rates.getTurmas(cursor, avaliacao)
    for rate in rates:
        rate.setDisciplina()
        rate.setProfessor()
    return render_template("rates.html", avaliacoes=rates, privilegio=user.privilegio)


@app.route("/denounce", methods=["GET", "POST"])
def denounce():
    info = request.form
    create_denounce = denuncia_dao.DenunciaDAO()
    denuncia = denuncias.Denuncia()
    denuncia.fk_matricula = user.matricula
    denuncia.fk_idAvaliacao = info["id"]
    denuncia.motivo = info["motivo"]
    create_denounce.create(cursor, denuncia)
    return redirect("/classes")

@app.route("/classes/update")
def classes_update(): # estudante cria, mas n remove nem edita
    return render_template("classe_update.html")


@app.route("/classes/add")
def classes_add(): # estudante cria, mas n remove nem edita
    return render_template("classes_add.html")


@app.route("/view")
def view():
    result = view_dao.View()
    results = result.view(cursor)
    return render_template("view.html", results=results)


app.run(host='127.0.0.1', port=4002)
