from app import *
from views import index, login, register, logout, profile, p404


if __name__ == "__main__":
    app.secret_key = '123'
    app.run(debug=True)