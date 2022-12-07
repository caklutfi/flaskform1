from flask import Flask, render_template, request, redirect,url_for, session, flash
from clientform import ClientForm
from werkzeug.utils import secure_filename
import os
import requests
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'zip'}
# Setting up the application
app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"
app.config['UPLOAD_FOLDER'] = 'static'


url= 'https://api.npoint.io/e21406b80f9016c674e8'
response= requests.get(url).json()



# making route
@app.route('/')
def home():

    data = response
    return render_template('index.html', json=data )

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method =='POST':
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route('/wtform', methods=['GET', 'POST'])
def wtform():
    name = None
    form = ClientForm()
    if request.method == 'POST':
        name = form.fullname.data
        email = form.email.data
        address = form.address.data
        phone = form.phone.data
        date = form.date.data
        time = form.time.data
        file = form.payment.data
        print(type(file))
        print(file.filename)
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        session['user'] = name
        session['email'] = email
        session['address'] = address
        session['phone'] = phone
        session['date'] = date.strftime("%m/%d/%Y")
        session['time'] = time.strftime("%H:%M:%S")
        session['payment'] = file.filename
        # form.fullname.data = ''
        flash('you are loged in')
        return redirect(url_for('user'))
    return render_template("wtform.html", name=name, form=form)

@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        email = session['email']
        address = session['address']
        phone = session['phone']
        date = session['date']
        time = session['time']
        payment = session['payment']
        return render_template('user.html', user=user,email=email,address=address,phone=phone,date=date,time=time,payment=payment)
    else:
        return redirect(url_for('home'))



# running application
if __name__ == '__main__':
    app.run(host='192.168.0.11', port=80, debug=True)