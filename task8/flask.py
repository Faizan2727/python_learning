from flask import Flask
app = Flask(__name__)

@app.route("/sum")
def lwsum():
    z = 3 + 4
    return(str(z))

@app.route("/mail")
def lwmail():
    return("mail send")

#app.run(port=80, host="0.0.0.0") #when you are deployin on cloud or public IP
app.run(debug=True) # In you local machine


