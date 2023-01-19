from flask import Blueprint

bp_education = Blueprint('bp_education', __name__, template_folder='templates', static_folder='static')

from .courses import *
from .modules import *
from .topics import *
from .tags import *
from .imageupload import *
