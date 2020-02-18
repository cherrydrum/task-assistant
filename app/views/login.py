from models import User
import hashlib
from app import *
import time

@login_manager.user_loader
def load_user(login):
    return User.query.get(login)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile', login = current_user.login))

    if request.method == 'POST':

        login = request.form['login']
        
        if bool(User.query.filter_by(login=login).first()):

            if User.query.filter_by(login = login).first().password != None:
                user = User.query.filter_by(login=login).first()
            else:
                return redirect(url_for('register', login = login))

            try:
                password = hashlib.sha224(request.form['password'].encode('utf-8')).hexdigest()
                if password == user.password: 
                    login_user(user, remember=True)
                    flash('Успешно', 'success')
                    return redirect(url_for('profile', login = login))
                else:  
                    flash('Неверный пароль', 'danger')
                    return render_template('login.html', login = login)
            except:
                pass
            
            return render_template('login.html', login = login)        
        else:
            return redirect(url_for('register', login = login))
            
    return render_template('login.html')