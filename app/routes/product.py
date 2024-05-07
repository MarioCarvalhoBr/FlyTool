# Importações padrão do Python
import os

# Importações do Flask e extensões
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename

# Importações do seu projeto
from app import db, UPLOAD_FOLDER
from app.models.models import Product
from app.forms.forms import ProductAddForm, ProductEditForm
from app.utils.helpers import generate_unique_zip_filename


bp = Blueprint('product', __name__, url_prefix='/product')

@bp.route('/')
@login_required
def list():
    products = Product.query.all()
    return render_template('product/list.html', products=products)

@bp.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = ProductAddForm()
    if form.validate_on_submit():

        # Trata o arquivo enviado
        f = request.files['file_data']
        if f:
            filename = secure_filename(generate_unique_zip_filename())
            f.save(os.path.join(UPLOAD_FOLDER, filename))
            
            # Salva o caminho no banco de dados
            product = Product(name=form.name.data, description=form.description.data, file_zip_path=filename, id_user = current_user.id)
            db.session.add(product)
            db.session.commit()
            
            flash('Product added successfully!')
            return redirect(url_for('product.list'))
    return render_template('product/add.html', form=form)

@bp.route('/edit/<id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    product = Product.query.get_or_404(id)
    form = ProductEditForm(obj=product)
    
    if form.validate_on_submit():
        if 'file_data' in request.files:
            f = request.files['file_data']
            if f and f.filename != '':  # Verifica se um arquivo novo foi realmente enviado
                old_file_path = os.path.join(UPLOAD_FOLDER, product.file_zip_path) if product.file_zip_path else None
                filename = secure_filename(generate_unique_zip_filename())  # Gera um nome de arquivo único
                
                print(f"UPLOAD_FOLDER: {UPLOAD_FOLDER} - new filename: {filename}")
                
                f.save(os.path.join(UPLOAD_FOLDER, filename))  # Salva o novo arquivo

                # Se havia um arquivo antigo, remove-o
                if old_file_path and os.path.exists(old_file_path):
                    os.remove(old_file_path)

                # Atualiza o caminho do arquivo no objeto produto
                product.file_zip_path = filename
        
        # Atualiza os outros campos do produto
        product.name = form.name.data
        product.description = form.description.data
        db.session.commit()
        flash('Product updated successfully!', 'success')
        return redirect(url_for('product.list'))

    return render_template('product/edit.html', form=form, product=product)

@bp.route('/delete/<id>', methods=['GET', 'POST'])
@login_required
def delete(id):
    product = Product.query.get_or_404(id)  # Alterado para get_or_404 para melhor manipulação de erros
    if product.file_zip_path:
        file_path = os.path.join(UPLOAD_FOLDER, product.file_zip_path)
        if os.path.exists(file_path):
            try:
                os.remove(file_path)  # Tenta remover o arquivo do sistema
            except Exception as e:
                flash(f'Error deleting the file: {str(e)}', 'error')  # Exibe uma mensagem em caso de erro na exclusão do arquivo

    db.session.delete(product)
    db.session.commit()
    flash('Product deleted successfully!', 'success')
    return redirect(url_for('product.list'))