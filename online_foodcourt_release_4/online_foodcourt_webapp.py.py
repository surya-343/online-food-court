"""
added about.html
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
# END POINT - 2 : http://127.0.0.1:5000/about URL MAPPED to '/about'
# --------------------
@foodcourt_app.route('/about')
def my_about_page():
    return flask.render_template('about.html')
# --------------------

# --------------------
# Run the server
# --------------------
foodcourt_app.run()
# --------------------
