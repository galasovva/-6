from flask import *  # (в терминале) pip install flask
from flask_sqlalchemy import *
from sqlalchemy import *
import  random
from jinja2 import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///athletes.db'
db = SQLAlchemy(app)

class Athletes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    gender = db.Column(db.String(2))
    age = db.Column(db.Integer)
    place = db.Column(db.String(80))
    sport = db.Column(db.String(80))
    use = db.Column(db.Integer)

    def __init__(self,name_t,gender_t,age_t,place_t,sport_t,use_t):
        self.name = name_t
        self.gender = gender_t
        self.age = age_t
        self.place = place_t
        self.sport = sport_t
        self.use = use_t

class Trener(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    age = db.Column(db.Integer)
    stage = db.Column(db.String(80))
    sport = db.Column(db.String(80))

    def __init__(self,name_t,age_t,stage_t,sport_t):
        self.name = name_t
        self.age = age_t
        self.stage = stage_t
        self.sport = sport_t


with app.app_context():
    db.create_all()

    # ath01 = Athletes('Равиль Второй','m',4,'Санкт-Петербург','Easy gaming',random.randint(0, 1)) # это добавление новых записей
    # ath02 = Athletes('Иван Одинадцатый','m',33,'Москва','Shopping',random.randint(0, 1))
    # db.session.add_all([ath01, ath02])

    # t01 = Trener('Иван Иванов',29,4,'Shopping') # это добавление новых записей
    # t02 = Trener('Петр Петров',36,6,'Gaming')
    # t03 = Trener('Николай Николаев',41,10,'Fishing')
    # t04 = Trener('Семен Семенов',31,5,'Working')
    # db.session.add_all([t01, t02, t03, t04])

    db.session.commit()


    min_age = db.session.query(func.min(Athletes.age)).scalar()
    max_age = db.session.query(func.max(Athletes.age)).scalar()
    print("Минимальный возраст спортсмена: ", min_age)
    print("Максимальный возраст спортсмена: ", max_age)
    all = db.session.query(Athletes).count()
    print('В базе данных',all,'спортсмена(-ов)')

    # users = db.session.execute(db.select(Athletes)).scalars() # это вывод всех данных о спортсменах
    # vyvod = Athletes.query.all()
    # for i in vyvod:
    #     print(f'Данные спортсмена {i.name}: ID - {i.id}; '
    #           f'пол - {i.gender}; регион - {i.place}; '
    #           f'возраст - {i.age}; вид спорта - {i.sport}')
    db.session.close()

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

@app.route('/athletes/')
def athletes():
    members = Athletes.query.all()
    masters = Trener.query.all()
    return render_template('athletes.html',users=members,teachers=masters)

if __name__ == '__main__':
    app.run(debug=True)