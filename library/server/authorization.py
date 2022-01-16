from flask import Flask, request, render_template
#from flask_script import Manager

app = Flask(__name__)
app.debug = True
#manager = Manager(app)

@app.route('/authorization/', methods=['get','post'])
def authorization():
    msg = ''
    if request.method == "POST":
        login = request.form.get('username')
        password = request.form.get('password')
        if login == 'admin' and password == 'admin':
            msg = 'OK'
        else:
            msg = 'ERROR'

    return render_template('authorization.html', message=msg)

if __name__=="__main__":
    app.run()