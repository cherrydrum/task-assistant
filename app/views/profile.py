from models import *
from app import *

@app.route('/profile/<login>', methods = ['GET', 'POST'])
def profile(login):

    if bool(User.query.filter_by(login = login).first()):
        user_obj = User.query.filter_by(login = login).first()
        return render_template('profile.html', user_obj = user_obj)

    else:
        return redirect(url_for('p404'))