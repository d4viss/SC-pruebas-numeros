from flask import Flask, render_template, request, send_file
from model import MeanTest
from werkzeug.utils import secure_filename
from os.path import join
from os import getcwd
import base64

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "files"

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/mean_test')
def meanTest():
    return render_template('mean_test.html')

@app.route('/mean_test', methods=["POST"])
def setAtributesMeanTest():
    file = request.files['input-file']
    fileRoute = secure_filename(file.filename)
    file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

    path = getcwd() + "/files/" + file.filename
    print("ruta" + path)

    meanTestClass = MeanTest.MeanTest(request.form['acept'], path)

    encoded_img = base64.b64encode(meanTestClass.generateGrafic().read()).decode('utf-8')

    return render_template('mean_test.html', randomNumbers=meanTestClass.randomNumbers, acept=meanTestClass.acept, error=meanTestClass.error, n=meanTestClass.numberN, r=meanTestClass.calculateMean(), alpha=meanTestClass.alpha, z=meanTestClass.z, li=meanTestClass.calculateLI(), ls=meanTestClass.calculateLS(), verify=meanTestClass.verifyTest(), grafic=encoded_img)

@app.route('/variance_test')
def varianceTest():
    return render_template('variance_test.html')

@app.route('/ks_test')
def ksTest():
    return render_template('ks_test.html')

@app.route('/chi_test')
def chiTest():
    return render_template('chi_test.html')

@app.route('/poker_test')
def pokerTest():
    return render_template('poker_test.html')

if __name__ == '__main__':
    app.run(debug=True)