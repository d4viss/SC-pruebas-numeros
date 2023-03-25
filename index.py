from flask import Flask, render_template, request, send_file
from model import MeanTest
from werkzeug.utils import secure_filename
from os.path import join
from os import getcwd, mkdir
import base64
from model.variance_test import VarianceTest
from model.k_smirnoff_test import KolmogorovSmirnovTest
from model import constants, Utilities
import csv

pathFiles = getcwd() + "/files/"

app = Flask(__name__)
try:
    mkdir(pathFiles)
    app.config['UPLOAD_FOLDER'] = "files"
except OSError:
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
    
    meanTestClass = MeanTest.MeanTest(request.form['acept'], path)

    encoded_img = base64.b64encode(meanTestClass.generateGrafic().read()).decode('utf-8')

    return render_template('mean_test.html', randomNumbers=meanTestClass.randomNumbers, acept=meanTestClass.acept, error=meanTestClass.error, n=meanTestClass.numberN, r=meanTestClass.calculateMean(), alpha=meanTestClass.alpha, z=meanTestClass.z, li=meanTestClass.calculateLI(), ls=meanTestClass.calculateLS(), verify=meanTestClass.verifyTest(), grafic=encoded_img)


@app.route('/variance_test')
def varianceTest():
    return render_template('variance_test.html')


@app.route('/variance_test', methods=['POST'])
def set_numbers_in_variance_test():
    file = request.files['file']
    ri_list = Utilities.get_ri_list(file, app.config['UPLOAD_FOLDER'])
    variance_test = VarianceTest(ri_list)
    ri_list = variance_test.ri_list
    mean = variance_test.calculate_average()
    variance = variance_test.calculate_variance()
    variables = variance_test.calculate_variables()
    is_valid = variance_test.is_valid_test(variables[2], variables[3], variance)
    encode_img = base64.b64encode(Utilities.generateGrafic(variance_test.ri_list).read()).decode('utf-8')
    return render_template('variance_test.html', ri_list=ri_list, length=len(ri_list), mean=mean, variance=variance, variables=variables, is_valid=is_valid, grafic=encode_img)


@app.route('/ks_test')
def ksTest():
    return render_template('ks_test.html')


@app.route('/ks_test', methods=['POST'])
def set_attributes_ks_test():
    file = request.files['file']
    ri_list = Utilities.get_ri_list(file, app.config['UPLOAD_FOLDER'])
    ks_test = KolmogorovSmirnovTest(ri_list, 0, 1)
    ks_test.calculate_intervals()
    freq_obt = ks_test.get_frequency_obt()
    freq_obt_acc = ks_test.get_freq_obt_acc(freq_obt)
    prob_obt = ks_test.get_prob_obt(freq_obt_acc)
    exp_freq = ks_test.get_exp_freq_acc()
    exp_prob = ks_test.get_exp_prob_acc(exp_freq)
    diff_list = ks_test.get_abs_diff(prob_obt, exp_prob)
    encode_img = base64.b64encode(Utilities.generateGrafic(ks_test.ri_list).read()).decode('utf-8')
    return render_template('ks_test.html', ri_list=ri_list, initial=ks_test.initial_list, final=ks_test.final_list, freq_obt=freq_obt, freq_obt_acc=freq_obt_acc, prob_obt=prob_obt, exp_freq=exp_freq, exp_prob=exp_prob, diff_list=diff_list, diff=max(diff_list), max_diff_allow=ks_test.get_critic_value(), grafic=encode_img)


@app.route('/chi_test')
def chiTest():
    return render_template('chi_test.html')


@app.route('/poker_test')
def pokerTest():
    return render_template('poker_test.html')


if __name__ == '__main__':
    app.run(debug=True)
