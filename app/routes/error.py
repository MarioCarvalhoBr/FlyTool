from flask import Blueprint, render_template

bp = Blueprint('error', __name__)

# Error 404
@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404