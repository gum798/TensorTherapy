# !conda install flask
# !pip install urllib

from flask import Flask, request
from Stable_diffusion import *
import os

sd = Stable_diffusion()

filename = "sd_gen.png"

app = Flask(__name__)
@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/txt2img')
def txt2img():
    txt = request.args.get('txt')
    # img = sd.txt2img("a photo of an astronaut riding a horse on mars")
    img = sd.txt2img(txt)
    img.save(filename)
    print(os.getcwd())
    return os.getcwd() + "/" +filename

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)
    