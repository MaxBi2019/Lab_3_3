from flask import Flask, render_template, request, redirect
import max
from mover import bring
import os
from cash import clear_the_cash
app = Flask("max")
data = {}


@app.route('/', methods=['POST', 'GET'])
def index():
    path = os.getcwd()
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    clear_the_cash(ip)
    if request.method == 'POST':
        name = request.form['content']
        full = path.replace("\\", "/") + "/" + name + ip + ".html"
        data[ip] = full
        max.main(name, ip)
        bring(name+ip)
        return redirect("/map")
    else:
        return render_template("home.html")


@app.route('/map')
def outlook():
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    file = data[ip].split("/")[-1]
    return render_template(file)


if __name__ == '__main__':
    app.debug = True
    app.run(host='192.168.1.100', port=8000)