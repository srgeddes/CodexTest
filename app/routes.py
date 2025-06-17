from flask import Blueprint, render_template, jsonify

from .utils import get_random_fact, get_random_image

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """Display the homepage with a random turtle fact and image."""
    fact = get_random_fact()
    image = get_random_image()
    return render_template('index.html', fact=fact, image=image)


@main_bp.route('/fact')
def fact():
    """Return a new random turtle fact and image as JSON."""
    data = {
        'fact': get_random_fact(),
        'image': get_random_image(),
    }
    return jsonify(data)
