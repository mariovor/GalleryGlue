import os
from flask import Flask
from configparser import ConfigParser

# Create the Flask app
app = Flask(__name__)

# Prepare Paths
PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))
GALLERY_GLUE_PATH = os.environ.get('GALLERY_GLUE_PATH', PACKAGE_PATH)

# Load Config
app.settings = ConfigParser()
app.settings.read(os.path.join(GALLERY_GLUE_PATH, 'config.ini'))

# Extract Adapter
ADAPTER = app.settings['General']['Adapter']

# Normalize Paths
for key in app.settings['Paths']:
    os.path.normpath(app.settings['Paths'][key])

# Analyze General Settingss
# Galleries Folder Name
if 'GalleriesFolderName' not in app.settings['General']:
    app.settings['General']['GalleriesFolderName'] = 'Galleries'

# Galleries Path
GALLERIES_PATH = os.path.join(GALLERY_GLUE_PATH, app.settings['General']['GalleriesFolderName'])
if app.settings['General']['GalleriesOnDifferentPath'] == 'yes':
    GALLERIES_PATH = os.path.join(GALLERY_GLUE_PATH, app.settings['Paths']['Galleries'], app.settings['General']['GalleriesFolderName'])

# Load views
from .views import *  # noqa
