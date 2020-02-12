from app import *

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')