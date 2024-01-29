from flask import Flask, request
import socket
import subprocess

app = Flask(__name__)

SEED=0
@app.route('/',methods = ['POST', 'GET'])
def number():
   global SEED
   if request.method == 'POST':
      subprocess.Popen(["python3", "stress_cpu.py"])
      return "success"
   if request.method == 'GET':
      return socket.gethostname()

if __name__ == '__main__':
   app.run()