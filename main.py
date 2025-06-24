from flask import Flask , render_template , request,  redirect, session , url_for
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key ="your_secret_key"


    #Confug SQL Alchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///user.db"
app.config["SQLALCHERY_TRACK_MODIFICATION"] = False
db= SQLAlchemy(app)


    # Database Model - single Row with our DB
class User(db.Model) :
    # class variables
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(25), unique=True , nullable=False)
    password = db.Column(db.String(150) , nullable =False)


def set_password(self,password):
    self.check_password_hash = generate_password_hash(password)

def check_password(self,password):
    return check_password_hash(self.password_hash ,password)




    #Route
@app.route("/")
def home():
    if"username" in session :
        return redirect(url_for('dashboard'))
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)