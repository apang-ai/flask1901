import os
import sys

from flask import Flask, render_template, flash, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy   #导入扩展类
import click
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

WIN = sys.platform.startswith('win')

if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
# # Linux中
# app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path, 'data.db')

# windows中
app.config['SQLALCHEMY_DATABASE_URI'] = prefix+os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关闭了对模型的监控
app.config['SECRET_KEY'] = 'watchlist_dev'


db = SQLAlchemy(app)  # 初始化扩展类， 传入程序实例app
login_manager = LoginManager(app) # 实例化登录拓展类
@login_manager.user_loader
def load_user(user_id):
    user = User.query.get(int(user_id))
    return user

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    username = db.Column(db.String(20))
    password_hash = db.Column(db.String(128))

    def set_password(self, password):

        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):

        return check_password_hash(self.password_hash, password)

class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

# 模板上下文处理函数
@app.context_processor
def common_user():

    user = User.query.first()

    return dict(user=user)

 # views   
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        # request再请求触发的时候才会包含数据
        get_title = request.form.get('title')
        get_year = request.form.get('year')

        # 验证数据是否符合要求
        if not get_title or not get_year or len(get_year)>4 or len(get_title)>60:
            flash('不能为空，或超过最大长度')
            return redirect(url_for('index'))
        # 保存表单数据
        movie = Movie(title=get_title, year=get_year)
        db.session.add(movie)
        db.session.commit()
        flash('创建成功！')
        return redirect(url_for('index'))

    # user = User.query.first()
    movies = Movie.query.all()

    return render_template('index.html', movies=movies)


# 更新电影信息
@app.route('/movie/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):

    movie = Movie.query.get_or_404(movie_id)

    if request.method == 'POST':
        get_title = request.form['title']
        get_year = request.form['year']

        if not get_title or not get_year or len(get_year)>4 or len(get_title)>60:
            flash('不能为空，或超过最大长度')
            return render_template('edit.html', movie=movie)

        movie.title = get_title
        movie.year = get_year
        db.session.commit()
        flash('数据库更新成功')
        return redirect(url_for('index'))

    return render_template('edit.html', movie=movie)


# 删除电影信息
@app.route('/movie/delete/<int:movie_id>', methods=['GET', 'POST'])
@login_required
def delete(movie_id):
    
    movie = Movie.query.get_or_404(movie_id)
            
    db.session.delete(movie)
    db.session.commit()
    flash('数据删除成功！')
    
    return redirect(url_for('index'))



# 登录
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # request再请求触发的时候才会包含数据
        get_username = request.form.get('username')
        get_password = request.form.get('password')

        # 验证数据是否符合要求
        if not get_username or not get_password:
            flash('输入错误')
            return redirect(url_for('login'))

        # 查询用户表
        user = User.query.first()
        if user.username == get_username and user.validate_password(get_password):
            login_user(user)
            flash('登陆成功')
            return redirect(url_for('index'))

        flash('用户名密码错误')

        return redirect(url_for('login'))
    
    return render_template('login.html')

# 登出
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('拜拜')

    return redirect(url_for('index'))


# 自定义指令
# 新建data.db初始化命令
@app.cli.command()  # 装饰器 注册命令
@click.option('--drop', is_flag=True, help='删除之后在创建')
def initdb(drop):
    if drop:
        
        db.drop_all()
    
    db.create_all()

    click.echo('初始化数据库完成')

# 向data.db中写入数据
@app.cli.command()

def forge():

    # name = 'Apang'

    movies = [
        {"title":"大赢家","year":"2020"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"速度与激情8","year":"2012"},
        {"title":"我的父亲母亲","year":"1995"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"},
        {"title":"囧妈","year":"2020"},
        {"title":"战狼","year":"2020"},
        {"title":"心花路放","year":"2018"}
    ]

    # user = User(name=name)
    # db.session.add(user)
    for i in movies:

        movie1 = Movie(title=i['title'], year=i['year'])
        db.session.add(movie1)
     
    db.session.commit()    
    click.echo('插入数据完成')


# 生成管理员账号
@app.cli.command()
@click.option('--username', prompt=True, help='管理员账号')
@click.option('--password', prompt=True, help='管理员密码', hide_input=True, confirmation_prompt=True)
def admin(username, password):
    db.create_all()
    user = User.query.first()
    if user is not None:
        click.echo('更新用户信息')
        user.username = username
        user.set_password(password)
    else:
        click.echo('创建用户信息')
        user = User(username=username, name='Admin')
        user.set_password(password)
        db.session.add(user)

    db.session.commit()
    click.echo('管理员创建完成')

# 错误处理函数
@app.errorhandler(404)
def page_not_found(e):

    # user = User.query.first()

    return render_template('404.html'), 404



