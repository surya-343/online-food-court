"""
this is foodcourt app realse 2
Added welcome page to online foodcourt application in this 
"""

# --------------------
# Create App (Object) for our website
# --------------------
import flask
foodcourt_app = flask.Flask("foodcourt_app")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@foodcourt_app.route('/')
def my_index_page():
    return "Welcome to online foodcourt"
# --------------------

# --------------------
# Run the server
# --------------------
foodcourt_app.run()
# --------------------
