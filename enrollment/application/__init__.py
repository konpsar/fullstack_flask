from flask import Flask


app = Flask(__name__)


# I import that in the end in order not to circulate, 
# because routes.py imports app as well
from application import routes