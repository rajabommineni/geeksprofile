# importing libraries 
from flask import Flask, jsonify
from flask_mail import Mail, Message


app = Flask(__name__) 
mail = Mail(app) # instantiate the mail class 

# configuration of mail 
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app) 

@app.route("/") 
def hello():
	return jsonify({'status': 'Hello! Your profile is sent to your email'})

# message object mapped to a particular URL ‘/’ 
@app.route("/mail") 
def index():
	msg = Message(
					'Hello', 
					sender ='yourId@gmail.com', 
					recipients = ['receiver’sid@gmail.com'] 
				)
	msg.body = 'Hello Flask message sent from Flask-Mail'
	mail.send(msg) 
	return 'Sent'

if __name__ == '__main__': 
	app.run(debug = True)
