from flask import Blueprint, render_template
import requests

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Display a random cat fact."""
    response = requests.get('https://catfact.ninja/fact', timeout=5)
    data = response.json()
    fact = data.get('fact', 'No fact available.')
    return render_template('index.html', fact=fact)
