from watchlistapp import app, db
from watchlistapp.models import User, Movie
from flask import render_template, flash, redirect, request, url_for
from flask_login import login_user, logout_user, login_required, current_user

# views   
@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
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

#settings 设置
@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    if request.method == 'POST':
        name = request.form['name']
        if not name or len(name)>20:
            flash('输入错误')
            return redirect(url_for('settings'))
        current_user.name = name
        db.session.commit()
        flash('设置成功')
        return redirect(url_for('index'))
    return render_template('settings.html')