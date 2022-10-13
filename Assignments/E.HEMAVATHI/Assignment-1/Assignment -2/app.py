from flask import Flask,render_template,request,session,logging,url_for,redirect,flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

from passlib.hash import sha256_crypt
engine = create_engine("mysql+pymysql://root:1234567@localhost/signin")
db=scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)

@app.route("/")
@app.route("index")
def index():
   return render_template("home.html")

@app.route("/signup")
def signup():
   if request.method =="POST":
      name = request.form.get("name")
      username =request.form.get("username")
      password = request.form.grt(" password")
      confirm = request.form.grt("confirm")
      secure_password = sha256_crypt.encrypt(str(password))

      if password == confirm:
           db.execute("INSERT INTO users(name, username,password) VALUES(:name,:username,:password)",
                           {"name":name,"username":username,"password":secure_password})
            db.commit()   
            flash("U are registered& can login","success")

            return redircet(url_for('signin')) 
      else:
         flash("password does not match","failed")

         return render_template("signup.html")

   return render_template("signup.html")

@app.route("/signin",method=["GET","POST"])
def signin():
    if request.method  =="POST":
        username = request.form.get("name")
        password = request.form.grt(" password")
        usernamedata = db.execute("SELECT username FROM users WHERE username=:username",{"username":username}).fetchone()
        passwordata = db.execute("SELECT password FROM users WHERE username=:username",{"username":username}).fetchone()

        if usernamedata is None:
            flash("No username","failed")
            return render_template("signin.html")
         else:
             for passwor_data in passwordata:
                 if sha256_crypt.verify(password,passwor_data):
                      flas("you are now login","success")
                      return redircet(url_for('photo')) 
                  else:
                      flash("incorrect password","failed")
                      return render_template("signin.html") 

   return render_template("signin.html")   

if __name__=="__main__":
      app.secret_keys="1234567dailywebcoding"
      app.run(debug=True)
