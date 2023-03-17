from flask_login import UserMixin, LoginManager, login_user, login_required, logout_user, current_user
from flask import Flask, render_template, url_for, request, redirect, flash
import os
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shop.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = '12345'
db = SQLAlchemy(app)
manager = LoginManager(app)


class Goods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    kind = db.Column(db.Text)
    model = db.Column(db.Text)
    name = db.Column(db.String(20), nullable=False)
    info = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    image = db.Column(db.Text, nullable=False)
    shortname = db.Column(db.Text)
    color = db.Column(db.Text)

    def __repr__(self):
        return [self.name, self.id, self.model, self.kind, self.info, self.price, self.image, self.shortname,
                self.color]


class Iphone14pm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.Text)
    memory = db.Column(db.Text)
    color = db.Column(db.Text)
    cpu = db.Column(db.Text)
    diagonal = db.Column(db.Text)
    resolution = db.Column(db.Text)
    brightness = db.Column(db.Text)
    contrast = db.Column(db.Text)
    pixel_density = db.Column(db.Text)
    display_type = db.Column(db.Text)
    display_technologies = db.Column(db.Text)

    def __repr__(self):
        return [self.series, self.id, self.memory, self.color, self.cpu, self.diagonal, self.resolution,
                self.brightness, self.contrast, self.pixel_density, self.display_type, self.display_technologies]


class Iphone13(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.Text)
    memory = db.Column(db.Text)
    color = db.Column(db.Text)
    cpu = db.Column(db.Text)
    diagonal = db.Column(db.Text)
    resolution = db.Column(db.Text)
    brightness = db.Column(db.Text)
    contrast = db.Column(db.Text)
    pixel_density = db.Column(db.Text)
    display_type = db.Column(db.Text)
    display_technologies = db.Column(db.Text)

    def __repr__(self):
        return [self.series, self.id, self.memory, self.color, self.cpu, self.diagonal, self.resolution,
                self.brightness, self.contrast, self.pixel_density, self.display_type, self.display_technologies]


class Ipad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.Text)
    memory = db.Column(db.Text)
    color = db.Column(db.Text)
    cpu = db.Column(db.Text)
    diagonal = db.Column(db.Text)
    resolution = db.Column(db.Text)
    brightness = db.Column(db.Text)
    contrast = db.Column(db.Text)
    pixel_density = db.Column(db.Text)
    display_type = db.Column(db.Text)
    display_technologies = db.Column(db.Text)

    def __repr__(self):
        return [self.series, self.id, self.memory, self.color, self.cpu, self.diagonal, self.resolution,
                self.brightness, self.contrast, self.pixel_density, self.display_type, self.display_technologies]


class Mac(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    series = db.Column(db.Text)
    memory = db.Column(db.Text)
    color = db.Column(db.Text)
    cpu = db.Column(db.Text)
    ram = db.Column(db.Text)
    cpu_cores = db.Column(db.Text)
    gpu_cores = db.Column(db.Text)
    ram_type = db.Column(db.Text)
    ram_max = db.Column(db.Text)

    def __repr__(self):
        return [self.series, self.id, self.memory, self.color, self.cpu, self.ram, self.cpu_cores, self.gpu_cores,
                self.ram_type, self.ram_max]


class Airpods(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.Text)
    noise = db.Column(db.Text)
    bluetooth = db.Column(db.Text)
    hours = db.Column(db.Text)

    def __repr__(self):
        return [self.id, self.type, self.noise, self.bluetooth, self.hours]


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    login = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.String, default='False')


@manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)


@app.route('/')
def index():
    goods = Goods().query.order_by(Goods.name).all()
    users = Users().query.order_by(Users.login).all()
    return render_template("index.html", data=goods, users=users)


@app.route('/katalog')
def katalog():
    return render_template("katalog.html")


@app.route('/tradein')
def trade():
    return render_template("tradein.html")


@app.route('/info')
def info():
    return render_template("info.html")


@app.route('/cart')
@login_required
def cart():
    return render_template('cart.html')


@app.route('/order', methods=['GET', 'POST'])
@login_required
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        surname = request.form.get('surname')
        mobile = request.form.get('mobile')
        email = request.form.get('email')
        adress = request.form.get('adress')
        house = request.form.get('house')
        if not (name and surname and mobile and email and adress and house):
            flash('Заполните все поля')
            return redirect('/order')
        else:
            return redirect('/success')
    return render_template("order.html")


@app.route('/success')
@login_required
def success():
    return render_template("success.html")


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        rm = True if request.form.get('remember-me') else False

        if login and password:
            user = Users.query.filter_by(login=login).first()

            if user and check_password_hash(user.password, password):
                login_user(user, remember=rm)

                return redirect('/')
            else:
                flash('Неверный логин или пароль')
        else:
            flash('Проверьте заполнение всех полей')

    return render_template("login.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    login = request.form.get('login')
    password = request.form.get('password')
    password2 = request.form.get('password2')

    if request.method == 'POST':
        if not (login and password and password2):
            flash('Заполните все поля')
        elif password != password2:
            flash('Пароли не совпадают')
        elif Users.query.filter_by(login=login).first():
            flash('Такой логин уже занят')
        else:
            hash = generate_password_hash(password)
            new_user = Users(login=login, password=hash, is_admin='False')
            db.session.add(new_user)
            db.session.commit()

            return redirect('/login')

    return render_template('register.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.after_request
def redirect_to_signin(response):
    if response.status_code == 401:
        return redirect(url_for('login_page') + '?next=' + request.url)

    return response


@app.route('/goods/<good_type>/')
def good_similar_type(good_type):
    good = Goods().query.filter_by(kind=good_type).all()
    return render_template("good_type.html", data=good, good_type=good_type)


@app.route('/profile')
@login_required
def user():
    users = Users().query.order_by(Users.login).all()
    return render_template('user.html', users=users)


@app.route('/login_change/<login>', methods=['GET', 'POST'])
@login_required
def loginChange(login):
    old = current_user
    if request.method == 'POST':
        old.login = request.form.get('login')
        if Users.query.filter_by(login=login).first():
            flash('Такой логин уже занят')
        else:
            db.session.commit()
            flash('Вы успешно сменили логин!')

    return render_template('login_change.html')


@app.route('/password_change/', methods=['GET', 'POST'])
@login_required
def psw_change():
    curr = current_user
    login = request.form.get('login')
    password_old = request.form.get('password_old')
    password_new = request.form.get('password_new')

    if request.method == 'POST':
        if not (login and password_old and password_new):
            flash('Заполните все поля')
        elif password_old != password_new:
            flash('Пароли не совпадают')
        elif not Users.query.filter_by(login=login).first():
            flash('Такого логина не существует')
        else:
            hash = generate_password_hash(password_new)
            new_user = Users(login=login, password=hash, is_admin='False')
            db.session.delete(curr)
            db.session.add(new_user)
            db.session.commit()

    return render_template('password_change.html')


@app.route('/goods/<good_type>/<shortname>/')  # '/goods/<good_type>/<model>/<shortname>/'
def view_good(good_type, shortname):  # (good_type, model, shortname)
    iphone14pm = Iphone14pm().query.first()
    iphone13 = Iphone13().query.first()
    ipad = Ipad().query.first()
    mac = Mac().query.first()
    airpods = Airpods().query.first()
    good = Goods().query.filter_by(shortname=shortname).first()
    other_goods = Goods().query.filter(Goods.shortname.startswith(good.shortname.split('_')[0])).all()  # other colors
    if '[' in good.image:
        img = eval(good.image)
    else:
        img = [good.image]
    return render_template("index_goods.html", dats=good, dats_image=img, other_goods=other_goods,
                           Iphone14pm=iphone14pm, Iphone13=iphone13, Ipad=ipad, Mac=mac, Airpods=airpods)


@app.route('/<int:id>/del/')
@login_required
def good_del(id):
    shrname = Goods.query.get(id)

    try:
        db.session.delete(shrname)
        print('delete')
        db.session.commit()
        return redirect('/')
    except:
        return "Ошибка"


@app.route('/delete')
@login_required
def de():
    return render_template("delete.html")

@app.route('/delete/confirm')
@login_required
def dels():
    crus = current_user

    try:
        db.session.delete(crus)
        db.session.commit()
        return redirect('/')
    except:
        return "Ошбика"


@app.route('/create', methods=['POST', 'GET'])
@login_required
def create():
    image = Goods().query.all()
    if request.method == "POST":
        id = request.form['id']
        name = request.form['name']
        model = request.form['model']
        price = request.form['price']
        kind = request.form['kind']
        color = request.form['color']
        shortname = request.form['shortname']
        info = request.form['info']
        image = request.form['image']

        goods = Goods(name=name, id=id, color=color, model=model, shortname=shortname, kind=kind, price=price,
                      info=info, image=image)

        try:
            db.session.add(goods)
            db.session.commit()
            return redirect('/')
        except Exception as err:
            print(f"db.create error: {err}")
            return "Ошибка"
    else:
        return render_template("create.html")


if __name__ == '__main__':
    app.run(debug=True)
