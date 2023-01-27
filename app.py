from flask import Flask

import connector
app = Flask(__name__)


@app.route('/')
def hello():
    count = connector.get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)


@app.route('/start')
def start():
    return connector.start()


@app.route('/sleep')
def sleep():
    return 'Soy una puta acción'


@app.route('/vol/<int:volume>')
def vol(volume):
    if volume > 10 or volume < 0:
        return {'status': False}
    return {'status': True}
