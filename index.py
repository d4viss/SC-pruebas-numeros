from flask import Flask, render_template, request
from model import MeanTest

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/mean_test')
def meanTest():
    return render_template('mean_test.html')

@app.route('/mean_test', methods=["POST"])
def setAtributesMeanTest():
    meanTestClass = MeanTest.MeanTest(request.form['acept'], request.form['error'], request.form['number_n'])
    meanTestClass.printValues()
    print(meanTestClass.calculateMean())
    return render_template('mean_test.html')

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