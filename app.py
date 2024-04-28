from flask import Flask, render_template, url_for, request, redirect, flash
from flask_mysqldb import MySQL
from flask_login import LoginManager, login_user, logout_user, login_required

#MODELOS
from models.UserModel import UserModel
#ENTIDADES
from models.user import User


MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'test_flask'

app = Flask (__name__)
app.secret_key = 'adasdasdasdasdasdasdasd'
data_base = MySQL(app)
login_manager_app =  LoginManager(app)

current_user_id = 0

@login_manager_app.user_loader
def load_user(id):
    return UserModel.get_by_id(data_base, id)

@app.route('/')
def index():
    return redirect(url_for('login'))

#LOGIN
@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, '', (request.form['user']), (request.form['password']), '')
        logged_user = UserModel.login(user, data_base)
        global current_user_id
        if logged_user != None:
            if logged_user.password == True:
                current_user_id = logged_user.id
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña invalida")
                return render_template('login.html')    
        else:
            flash("Usuario no encontrado")
            return render_template('login.html')
    else:
        return render_template('login.html')
#REGISTER
@app.route('/register', methods = ['GET', 'POST'])
def registro():
    if request.method == 'POST':
        user = User (0, request.form['nombre'], request.form['user'], request.form['contrasena'], request.form['e_mail'])
        if UserModel.register(user, data_base):
            return redirect(url_for('login'))
        else:
            flash('El usuario ya existe!')
            return render_template('register.html')    
    else:
        return render_template('register.html')
    

#PERFIL
@app.route('/my_profile', methods = ['GET', 'POST'])
@login_required
def my_profile():
    if request.method == 'POST':
        print("Id actual PERFIL: ", current_user_id)
        user = User (current_user_id, request.form['nombre'], request.form['usuario'], request.form['password'], request.form['e-mail'])
        if UserModel.update_profile(user, data_base):
            return redirect(url_for('login'))
    else:
        return render_template('my_profile.html')
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.errorhandler(404)
def pagina_no_encontrada(error):
    return render_template('404.html'), 404

@app.errorhandler(401)
def error_401(error):
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug = True)