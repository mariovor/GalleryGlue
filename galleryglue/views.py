from . import app
from . import GALLERIES_PATH

from .adapter.lightroom import lightroom


@app.route('/')
def index():
    lightroom(GALLERIES_PATH)

    return app.settings['Paths']['Galleries']
