from flask import Flask, render_template, request, redirect,url_for
from clientform import ClientForm
# Setting up the application
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

nama = ''
# making route
@app.route('/')
def home():
    variabel= nama
    return render_template('index.html', variabel=variabel)

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method =='POST':
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route('/wtform', methods=['GET', 'POST'])
def wtform():
    name = None
    form = ClientForm()
    if form.validate_on_submit():
        name = form.fullname.data
        form.fullname.data = ''
        print(name)
        global nama
        nama = name
        print(nama)
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template("wtform.html", name=name, form=form)



# running application
if __name__ == '__main__':
    app.run(debug=True)