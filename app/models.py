from app import *

# Про ForeignKey можно почитать тут
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/

# TODO: Добавить методы классов во имя Великой Инкапсуляции.

# Таблица откликов пользователей на задачи.
claims = db.Table('claims',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('subtask_id', db.Integer, db.ForeignKey('subtask.id'), primary_key=True),
    db.Column('active', db.Boolean)
)   

# Таблица ролей (тегов) пользователей.
roles = db.Table('roles',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('role_id', db.Integer, db.ForeignKey('role.id'), primary_key=True)
)   

# Таблица тегов задач.
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('task_id', db.Integer, db.ForeignKey('task.id'), primary_key=True)
)   


class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    login = db.Column(db.String(20), nullable=False)
    surname = db.Column(db.String(80), nullable=True)
    level = db.Column(db.Integer)
    active = db.Column(db.Boolean)
    access_lv = db.Column(db.Integer)  # Уровень прав. 0 = User
    roles = db.relationship('Role', secondary=roles, lazy='subquery',
        backref=db.backref('roles', lazy=True))

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=True)
    desc = db.Column(db.String(140), unique=True, nullable=True)
    creator = db.Column(db.Integer, db.ForeignKey('user.id'))
    subtasks = db.relationship('Subtask', backref='master', lazy=True)
    deadline = db.Column(db.DateTime)
    finished = db.Column(db.Boolean)

    # Массив тегов, в начале пишется класс, к которому пробрасывается отношение,
    # затем пишется таблица отношений, после чего backref, который делает симметричные
    # действия с классом Tag и добавляет ему массив по переменной 'tasks'

    tags = db.relationship('Tag', secondary=tags, lazy=True,
        backref=db.backref('tasks', lazy=True))

class Subtask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'))
    title = db.Column(db.String(80), unique=True, nullable=True)
    desc = db.Column(db.String(140), unique=True, nullable=True)
    pool = db.Column(db.Integer)
    deadline = db.Column(db.DateTime)
    finished = db.Column(db.Boolean)
    workers = db.relationship('User', secondary=claims, 
        backref=db.backref('subtasks', lazy=True))  