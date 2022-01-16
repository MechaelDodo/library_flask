from flask import Flask, request, render_template
#from flask_script import Manager
from forms import AuthorizationForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'qwertyuiop'
#manager = Manager(app)


@app.route('/authorization/', methods=['get','post'])
def authorization():
    #msg = ''
    #if request.method == "POST":
    #    login = request.form.get('username')
    #    password = request.form.get('password')
    #    if login == 'admin' and password == 'admin':
    #        msg = 'OK'
    #    else:
    #        msg = 'ERROR'

    #return render_template('authorization.html', message=msg)
    aut_form = AuthorizationForm()
    msg = ''

    if aut_form.validate_on_submit():
        username = aut_form.username.data
        password = aut_form.password.data
        if username == 'admin' and password == 'admin':
            msg = 'OK'
        else:
            msg = 'ERROR'

    aut_form.message.data = msg
    return render_template('authorization.html', form=aut_form)


if __name__=="__main__":
    app.run()