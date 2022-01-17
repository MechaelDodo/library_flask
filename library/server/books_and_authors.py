from flask import Flask, render_template
from forms import DetailListForm
#from flask_script import Manager

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'qwertyuiop'
#manager = Manager(app)


@app.route('/books_and_authors/', methods=["get", "post"])
def books_and_authors():
    form = DetailListForm()
    #use db in future
    books = ['Гарри Поттер', 'Мастер и Маргарита', 'Мертвые души', 'Война и Мир', 'Словарь']
    authors = ['Гоголь', 'Пушкин', 'Лев Толстой', 'Есенин', 'Блок']
    form.books_list.choices = books
    form.authors_list.choices = authors
    return render_template('books_and_authors.html', form=form)


if __name__=="__main__":
    app.run()
