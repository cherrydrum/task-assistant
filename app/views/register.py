from models import User
import hashlib
from app import *


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('profile', login = current_user.login))

    if request.method == 'POST':
        login = request.form['login']

        if bool(User.query.filter_by(login = login).first()):
            flash('Аккаунт уже существует', 'danger')
            
        elif len(login) < 2:
            flash('Логин слишком короткий', 'danger')

        else:
            password = request.form['password']
            confirm_password = request.form['confirm_password']

            if len(password) < 2:
                flash('Пароль слишком короткий', 'danger')

            elif password != confirm_password:
                flash('Пароли не совпадают', 'danger')
            
            else:
                password = hashlib.sha224(password.encode('utf-8')).hexdigest()
                # Здесь фляга падает — не обозначен __init__ у User
                new_user = User(login, password)
                db.session.add(new_user)
                db.session.commit()
                
                user = User.query.filter_by(login = login).first()
                login_user(user, remember=True)
                flash('Успешно', 'success')
                return redirect(url_for('profile', login = login))
    else:
        login = request.args.get('login')
        
    return render_template('register.html', login = login)