import base64
import os
from app import app, bcrypt
from flask import render_template, request, redirect, url_for, flash, session
from .forms import SignupForm, AddClass, LoginForm, EditProfile, EditRate, RateClass
from . import avaliacoes, denuncias
from . import turmas, usuarios
from app.models import cursor, avaliacao_dao, usuario_dao, view_dao
from app.models import denuncia_dao, turma_dao


def convertImageToBinary(img):
    with open(os.path.dirname(os.path.abspath(__file__)) + img, "rb") as f_img:
        binary = f_img.read()
    return binary

foto = convertImageToBinary("/../../images/generic_user.png")
user = usuarios.Usuario()
rate = avaliacoes.Avaliacao()


def logged_in(user):
    session["logged_in"] = True
    session["user_id"] = user.matricula
    session["name"] = user.nome
    session["email"] = user.email
    session["privilegio"] = user.privilegio
    return True


def manual_logout():
    session.pop("logged_in", None) 
    session.pop("user_id", None) 
    session.pop("name", None) 
    session.pop("email", None)
    session.pop("privilegio", None)


def is_logged_in():
    return session.get("logged_in", False)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = usuarios.Usuario().get_usr(matricula=form.matricula.data)
        if user and user.valida_senha(form.senha.data):
            logged_in(user)
            flash(f"Você está logado! Bem-vindo(a), {user.nome.title()}", category="success")
            return redirect(url_for("profile"))
        flash("Matrícula e senha inválida! Tente novamente", category="danger")
    return render_template("login.html", form=form)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        foto_bin = convertImageToBinary("/../../images/generic_user.png")
        if form.foto.data:
            foto = form.foto.data
            foto_bin = foto.read()
        senha = bcrypt.generate_password_hash(form.senha.data).decode("utf-8")
        user = usuarios.Usuario(matricula=form.matricula.data,
                                nome=form.nome.data,
                                email=form.email.data,
                                senha=senha,
                                curso=form.curso.data,
                                privilegio="COMUM",
                                dataNascimento=form.data_nascimento.data)
        create_user = usuario_dao.UsuarioDAO()
        create_user.create(cursor, user, foto_bin)
        logged_in(user)
        return redirect(url_for("profile"))
    if form.errors != {}:
        for error_msg in form.errors.values():
            flash(f"Ocorreu um erro {error_msg}", category="danger")
            
    return render_template("signup.html", form=form)


@app.route("/logout")
def logout():
    manual_logout()
    return redirect(url_for("index"))


@app.route("/profile", methods=["GET", "POST"])
def profile():
    denuncias = []
    if session["privilegio"] == "ADM":
        denuncia = denuncia_dao.DenunciaDAO()
        denuncias = denuncia.getNaoAvaliado(cursor)
        for den in denuncias:
            den.setAvaliacao()
            den.setDenunciado()

    user_logged = user.get_usr(matricula=session["user_id"])
    avaliacao = avaliacao_dao.AvaliacaoDAO()
    avaliacoes = avaliacao.getMy(cursor, user_logged.matricula)
    
    for avalia in avaliacoes:
        avalia.setProfessor()
        avalia.setDisciplina()
    
    base64_data = base64.b64encode(user_logged.foto).decode('utf-8')
    return render_template("profile.html", user=user_logged, base64_data=base64_data,
                           avaliacoes=avaliacoes, denuncias=denuncias)


@app.route("/edit_profile", methods=["GET", "POST"])
def edit_profile():
    form = EditProfile()
    user_logged = usuarios.Usuario().get_usr(matricula=session["user_id"])
    base64_data = base64.b64encode(user_logged.foto).decode('utf-8')
    if form.validate_on_submit():
        if form.submit.data:
            user_logged.nome = form.nome.data
            user_logged.email = form.email.data
            user_logged.curso = form.curso.data
            if form.foto.data:
                foto = form.foto.data
                foto_bin = foto.read()
                user_logged.foto = foto_bin
            usuario_dao.UsuarioDAO().update(cursor, user_logged, user_logged.foto)
            flash("Perfil atualizado.", category="success")
            return redirect(url_for("profile"))
        
        manual_logout()
        usuario_dao.UsuarioDAO().delete(cursor, user_logged.matricula)
        flash("Sua conta foi excluída com sucesso.", category="info")
        return redirect(url_for("index"))
        
    return render_template("edit_profile.html", form=form, user=user_logged,
                           base64_data=base64_data)


@app.route("/delete_account/user_denounced=<int:user_denounced>", methods=["POST", "GET"])
def delete_account(user_denounced):
    usuario_dao.UsuarioDAO().delete(cursor, user_denounced)
    return redirect(url_for("profile"))


@app.route("/ignore_report/denuncia_id=<int:denuncia_id>", methods=["POST", "GET"])
def ignore_report(denuncia_id):
    denuncia = {"avaliado": "AVALIADA", "idDenuncia": denuncia_id}
    update_denuncia = denuncia_dao.DenunciaDAO()
    update_denuncia.update(cursor, denuncia)
    return redirect(url_for("profile"))

@app.route("/delete_comment/rate_id=<int:fk_idAvaliacao>", methods=["POST", "GET"])
def delete_comment(fk_idAvaliacao):
    delete_rate = avaliacao_dao.AvaliacaoDAO()
    delete_rate.delete(cursor, fk_idAvaliacao)
    return redirect("/profile")    


@app.route("/classes_search/codigo=<string:cod>")
@app.route("/classes_search/")
def classes_search():
    cod_disciplina = request.args.get("codigo")
    turma = turma_dao.TurmaDAO()
    turmas = turma.getTurmas(cursor, cod_disciplina)
    if turmas:
        for turma in turmas:
            turma.setProf()
            turma.setNomeDisciplina()
        turma.setNomeDisciplina()
        nome_disciplina = turma.nome_disciplina

        return render_template("classes.html", turmas=turmas, nome_disc=nome_disciplina)
    flash("Código inválido.", category="danger")
    return render_template("classes.html")


@app.route("/rate_class/", methods=["POST"])
def rate_class():
    form = RateClass()
    return render_template("rate_class.html", form=form)
    # if request.method == "POST":
    #     info = request.form
    #     avaliacao = avaliacoes.Avaliacao(
    #         id=None, comentario=info["comentario"], nota=info["nota"],
    #         dificuldade=info["dificuldade"], fk_matricula=user.matricula, 
    #         fk_periodo=info["periodo"], fk_local=info["local"], fk_horario=info["horario"]
    #     )
    #     avaliacao.professor = info["professor"]
    #     avaliacao.setIDProfessor()
    #     create_rate = avaliacao_dao.AvaliacaoDAO()
    #     create_rate.create(cursor, avaliacao)
    #     if user.privilegio == "ADM":
    #         return redirect("/profile_adm")
    #     return redirect("/profile")
    # return render_template("classes_rate.html")


@app.route("/classes/rate/update/rate_id=<int:id>", methods=["GET", "POST"])
def classes_rate_update(id):
    update_rate = avaliacao_dao.AvaliacaoDAO()
    avaliacao = update_rate.get(cursor, id)
    return render_template("edit_rate.html", avaliacao=avaliacao)


@app.route("/update_rate/rateid=<int:id>", methods=["GET", "POST"])
def edit_rate(id):
    info = request.form
    update_rate = avaliacao_dao.AvaliacaoDAO()
    avaliacao = avaliacoes.Avaliacao()
    avaliacao.comentario = info["comentario"]
    avaliacao.nota = info["nota"]
    avaliacao.dificuldade = info["dificuldade"]
    avaliacao.id = id
    update_rate.update(cursor, avaliacao)
    return redirect("/profile")


@app.route("/classes_info/", methods=["GET", "POST"])
def classes_info():
    if is_logged_in():
        info = request.args.to_dict()
        turma = turmas.Turma()
        form = RateClass()
        turma.fk_idProfessor = info["idProfessor"]
        turma.setProf()
        turma.periodo = info["periodo"]
        turma.horario = info["horario"]
        turma.local = info["local"]
        if form.validate_on_submit():
            avaliacao = avaliacoes.Avaliacao(comentario=form.comentario.data,
                                             nota=form.nota.data, 
                                             dificuldade=form.dificuldade.data,
                                             fk_matricula=session["user_id"],
                                             fk_idProfessor=turma.fk_idProfessor,
                                             fk_periodo=turma.periodo,
                                             fk_horario=turma.horario,
                                             fk_local=turma.local)
            avaliacao_dao.AvaliacaoDAO().create(cursor, avaliacao)
            flash("Obrigado pela avaliação.", category="success")
            return redirect(f"/rates/?periodo={avaliacao.fk_periodo}&horario={avaliacao.fk_horario}&local={avaliacao.fk_local}&idProfessor={avaliacao.fk_idProfessor}")
        
        return render_template("rate_class.html", form=form, turma=turma)
    flash("Você deve estar logado para avaliar uma turma.", category="danger")
    return redirect(url_for("login"))


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
    denuncia.fk_matricula = session["user_id"]
    denuncia.fk_idAvaliacao = info["id"]
    denuncia.motivo = info["motivo"]
    avaliacao = avaliacao_dao.AvaliacaoDAO().get(cursor, denuncia.fk_idAvaliacao)
    create_denounce.create(cursor, denuncia)
    flash("Denúncia recebida.", category="info")
    return redirect(f"/rates/?periodo={avaliacao.fk_periodo}&horario={avaliacao.fk_horario}&local={avaliacao.fk_local}&idProfessor={avaliacao.fk_idProfessor}")

@app.route("/classes/update")
def classes_update(): # estudante cria, mas n remove nem edita
    return render_template("classe_update.html")


@app.route("/classes/add", methods=["GET", "POST"])
def add_class():
    if is_logged_in():
        form = AddClass()
        return render_template("add_class.html", form=form)
    flash("Você deve estar logado para adicionar uma turma.", category="danger")
    return redirect(url_for("login"))


@app.route("/view")
def view():
    result = view_dao.View()
    # results = result.view(cursor)
    page = request.args.get('page', 1, type=int)
    per_page = 10

    results, total_results = result.view_pages(cursor, page, per_page)

    return render_template("view.html", results=results, total_results=total_results,
                           page=page, per_page=per_page)
