# This is whre you can start you python file for your week1 web app
# Name: Amaka Atoyebi

import flask
import settings


#Views
from main import Main
from login import Login
from remote import Remote
from music import Music

app = flask.Flask(__name__)

app.secret_key = settings.secret_key

#Routes
main_view_func = Main.as_view('main')

app.add_url_rule('/',
             view_func=main_view_func,
             methods=["GET"])

app.add_url_rule('/<page>/',
             view_func=main_view_func,
             methods=["GET"])

app.add_url_rule('/login/', 
				view_func=Login.as_view('login'),
				methods = ['GET', 'POST'])

app.add_url_rule('/remote/',
 				view_func = Remote.as_view('remote'),
  				methods = ['GET', 'POST'])

app.add_url_rule('/music/',
 				view_func = Music.as_view('music'),
  				methods = ['GET'])

@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

app.debug = True
app.run()