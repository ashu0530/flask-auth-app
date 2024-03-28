from flask import Flask,request, render_template,redirect,session
from flask_sqlalchemy import SQLAlchemy #Database inbuilt module
import bcrypt

#Creates a Flask application instance
app = Flask(__name__) ##app is variable we can use to run

#Secret key of db stored in it
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  #Create folder and create file

#database instance
#Creates a SQLAlchemy object with the Flask app as a parameter
db = SQLAlchemy(app)
#Sets a secret key for the session
app.secret_key = 'secret_key'

#table creation and class User
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)  #id is primary key
    name = db.Column(db.String(100), nullable=False) 
    email = db.Column(db.String(100), unique=True) #email is unique
    password = db.Column(db.String(100))

    #Initilise the entry 
    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        #Encrypted password using this module bcrypt and export the the password in db with encryption
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

#Check conditions for login
    def check_password(self,password):
        #self.password is user password which mention on table when user enter
        return bcrypt.checkpw(password.encode('utf-8'),self.password.encode('utf-8'))
    
with app.app_context():
    db.create_all()
    

@app.route('/register', methods=['GET','POST']) #GET as well as POST method use in /register endpoints
def register(): # register function
    if request.method == 'POST':
        #handling request 
        #pass #if nothing you give uncomment
        #here we write out logic code for register
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']


        #When new user enter their name email and password take the value from User class
        new_user = User(name=name,email=email,password=password)
        db.session.add(new_user)
        #write in db
        db.session.commit()
        return redirect('login')
    

    return render_template('register.html')


@app.route('/login', methods=['GET','POST']) #GET as well as POST method use in /login endpoints
def login(): #login function
    if request.method == 'POST':  #if request is post else render the template
        #handling request 
        #pass #if nothing you give uncomment
        #here we write out logic code for register
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()  #get first user from db check email is exist on db or not

        if user and user.check_password(password):    #password matching  if yes
        #   session['name'] = user.name                 #session create and redirect to /dashboard
            session['email'] = user.email
        #    session['password'] = user.password
            return redirect('/dashboard')
        else:
            return render_template('login.html',error='Invalid user')


    return render_template('login.html')

@app.route('/dashboard')  #route to /dashboard 
def dashboard():
    if session['name']:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('dashboard.html',user=user)
    
    return redirect('/login')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)
