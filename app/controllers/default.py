from app import app

@app.route("/")
def homepage():
    return "Hello new world!"

@app.route("/signup")
def signup():
    return "signup"

@app.route("/login")
def login_page():
    return "Login"

@app.route("/profile")
def profile():  # editar, excluir
    return "profile"

@app.route("/profile/update")
def profile_update():
    return "profile update"

@app.route("/classes/")
def classes(): # estudante cria, mas n remove nem edita
    return "classes"

@app.route("/classes/update")
def classes_update(): # estudante cria, mas n remove nem edita
    return "classes update"

@app.route("/classes/add")
def classes_add(): # estudante cria, mas n remove nem edita
    return "classes add"

@app.route("/classes/rate")
def classes_rate(): # estudante cria, mas n remove nem edita
    return "classes rate"

@app.route("/classes/rate/update")
def classes_rate_update(): # estudante cria, mas n remove nem edita
    return "classes rate update"

@app.route("/view")
def view():
    return "view"
app.run(host='127.0.0.1', port=4444)
