# The code defines a function lwsum() that calculates the sum of 5 and 2, storing the result in the variable z.
# The function then returns the value of z, which is 7.
# When lwsum() is called it outputs is 7
"""
def lwsum():
    z = 3 + 4
    return z

print(lwsum())

# An API gateway handling HTTP requests and response between a client and a server.

# The server proccess functions like lwsum() and lwmul() with lwsum() adding 5 and 2 to return 7.

# The API facililates communication over a specifified port, ensuring smooth data exchange.

# A network architecture where a gateway routes traffic to different services(search, mail) on server identified by an IP address. It higlights the use of HTTP(port 80) and HTTPS(port 443) protocols for secure communication.

# The flows show request being directed to specific services via URLs.

#https://www.google.com/search?q=faizan+shaikh

# Two Flask route handlers. The first route, "/sum", defines a function lwsum() that calculates the sum of 5 and 2, returing the result. The second route, "/mail", defines a function lwmail() that returns the strings "mail send".

@app.route("/sum")
def lwsum()
    z = 3 + 4
    return z

@app.route("/mail")
def lwmail():
    return("mail send")

"""
# A ping cmd was exec on win 10 sys to test the loopback address(127.0.0.1).

# All packets were succesfully received with 0% loss, and response times were under 1 ms, indicating the network configuration is functioning correctly.

# ping 127.0.0.1

# Choose an Amazon Machine Image (AMI): Select an AMI that has the operating system and software configuration you need. 
# Select an Instance Type: Choose the instance type based on the required CPU, memory, and network performance. 
# Configure Instance Details: Set up details like the number of instances, network settings . # Add Storage: Define the storage requirements for your instance, such as the type and size of the volumes.
# Configure Security Group and Launch: Set up security groups to control inbound and outbound traffic, review all settings, and launch the instance

# This Flask application defines a route at "/sum" that executes the lwsum function.  
# When accessed, it calculates the sum of 5 and 2, returning the result as a strings
from flask import Flask
app = Flask(__name__)

@app.route("/sum")
def lwsum():
    z = 3 + 4
    return(str(z))

@app.route("/mail")
def lwmail():
    return("mail send")

#app.run(port=80, host="0.0.0.0")
app.run(debug=True)
# This code snippet defines two Flask routes: "/sum" and "/mail". The "/sum" route calculates the sum of 3 and 4, returning the result as a string.  

# The "/mail" route simply returns the string "mail send".

# The application is configured to run on port 80 and host "0.0.0.0", which makes it accessible from any IP address on the local network.

# The package manager for Python 3, on systems using the yum package manager.
# yum install python3-pip
# The command "pip3 install flask" which install the Flask web framework for Python 3.
# pip3 install flask
# The Python script sets up a basic Flask web application with two routes.  
# The/sum route returns the sum of 3 and 4 as a string, while the /mail route returns the string "mail send". The application runs on port 80 and is accessible from any host.

# A Flask application running in a development server mode.  
# The application is accessible at http://127.0.0.1:80 and http://172.31.0.142:80.


