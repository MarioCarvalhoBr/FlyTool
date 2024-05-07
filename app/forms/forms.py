# Importações de extensões Flask
from flask_login import current_user
from flask_wtf import FlaskForm

# Importações do WTForms
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, FileField, ValidationError, HiddenField
from wtforms.validators import DataRequired, Email, EqualTo, Length

# Importações do seu projeto
from app.models.models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(message='Email is required'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required'), Length(min=6)])
    errors = HiddenField("Errors")
    submit = SubmitField('Login')
    valid = True

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            self.valid = False
    
    def validate_password(self, password):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(password.data):
            self.valid = False
    def validate_errors(self, errors):
        if not self.valid:
            raise ValidationError('Email or password is incorrect')

class RegistrationForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(message='First Name is required')])
    last_name = StringField('Last Name', validators=[DataRequired(message='Last Name is required')])
    email = StringField('Email', validators=[DataRequired(message='Email is required'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Password is required'), Length(min=6)])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(message='Confirm password is required'), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered')

class SettingsForm(FlaskForm):
    name = StringField('First Name', validators=[DataRequired(message='First Name is required')])
    last_name = StringField('Last Name', validators=[DataRequired(message='Last Name is required')])
    email = StringField('Email', validators=[DataRequired(message='Email is required'), Email()])
    old_password = PasswordField('Old Password', validators=[DataRequired(message='Password is required'), Length(min=6)])
    new_password = PasswordField('New Password', validators=[])
    confirm_password = PasswordField('Confirm New Password', validators=[EqualTo('new_password', message='Passwords must match')])
    submit = SubmitField('Save')

    # Validar se a senha digitada corresponde a senha do usuário
    def validate_old_password(self, old_password):
        if not current_user.check_password(old_password.data):
            raise ValidationError('Old Password is incorrect')
    
    # Caso o usuário tenha digitado uma nova senha: Validar se as senhas são iguais
    def validate_confirm_password(self, confirm_password):
        if self.new_password.data != confirm_password.data:
            raise ValidationError('Passwords must match')
        
    # Validar se o email já está cadastrado
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user and user.id != current_user.id:
            raise ValidationError('Email already registered')
   
class ProductAddForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Name is required')])
    description = TextAreaField('Description', validators=[DataRequired(message='Description is required')])
    file_data = FileField('Upload ZIP File', validators=[DataRequired(message='ZIP File is required')])
    submit = SubmitField('Add')

    # Validar se o arquivo é um ZIP
    def validate_file_data(self, file_data):
        if not file_data.data.filename.endswith('.zip'):
            raise ValidationError('File must be a ZIP file')

class ProductEditForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(message='Name is required')])
    description = TextAreaField('Description', validators=[DataRequired(message='Description is required')])
    file_zip_path = StringField('File Zip Path')

    file_data = FileField('Upload new ZIP File?')
    submit = SubmitField('Save')
