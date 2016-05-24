from . import app
from . import ADAPTER, GALLERIES_PATH
from flask import render_template

from .adapter.lightroom import Lightroom


@app.route('/')
def index():
    provider = None

    if ADAPTER == 'Lightroom':
        provider = Lightroom(GALLERIES_PATH)

    return render_template('layout.html', galleries=provider.galleries)
