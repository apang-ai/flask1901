import os
import sys

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy   #导入扩展类
import click

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

db = SQLAlchemy(app)  # 初始化扩展类， 传入程序实例app

class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class Movie(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    year = db.Column(db.String(4))

@app.route('/')

def index():

    

    user = User.query.first()
    movies = Movie.query.all()

    return render_template('index.html', user=user, movies=movies)



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




