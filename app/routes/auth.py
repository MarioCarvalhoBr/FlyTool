# Importações padrão do Flask
from flask import Blueprint, render_template, redirect, url_for, flash

# Importações de segurança e autenticação
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

# Importações do seu projeto
from app import db
from app.models.models import User
from app.forms.forms import LoginForm, RegistrationForm, SettingsForm

bp = Blueprint('auth', __name__, url_prefix='/auth')
        
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user, remember=True)
            return redirect(url_for('home.index'))
        flash('Invalid email or password')
        
    return render_template('auth/login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            name=form.name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password_hash=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

        
@bp.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    form = SettingsForm(obj=current_user)
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        
        # VErifica se a senha atual está correta
        if not current_user.check_password(form.old_password.data):
            flash('Old Password is incorrect')
            return redirect(url_for('auth.settings'))
        
        # Verifica se o usuário digitou uma nova senha
        if form.new_password.data:
            current_user.password_hash = generate_password_hash(form.new_password.data)
            
        db.session.commit()
        return redirect(url_for('auth.settings'))
    return render_template('auth/settings.html', form=form)
