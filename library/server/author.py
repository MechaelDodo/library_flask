from flask import Flask, request, render_template
#from flask_script import Manager
from forms import AuthorForm

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'qwertyuiop'


@app.route('/author/<int:id>/', methods=['get', 'post'])
def author_page(id):
    form = AuthorForm()

    #use db in future
    author_name = 'Lev Tolsoi'
    biography = 'Hello. Authors name is Lev Tolstoi. He was born in 1910... '

    form.author_name.description = author_name
    form.biography.description = biography
    return render_template('author_page.html', form=form)


if __name__=="__main__":
    app.run()