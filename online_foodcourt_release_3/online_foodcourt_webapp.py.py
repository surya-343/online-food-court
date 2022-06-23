"""
call index.html
"""

# --------------------

# Create App (Object) for our website
# --------------------
import flask
foodcourt_app = flask.Flask("foodcourtApp")
# --------------------

# --------------------
# END POINT - 1 : http://127.0.0.1:5000/ URL MAPPED to '/'
# --------------------
@foodcourt_app.route('/')
def my_index_page():
    return flask.render_template('index.html')
# --------------------

# --------------------
# Run the server
# --------------------
foodcourt_app.run()
# --------------------
