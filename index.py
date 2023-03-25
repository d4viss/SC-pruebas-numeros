from flask import Flask, render_template, request
from model import MeanTest
from model import poker_test
from model import chi2_test
from werkzeug.utils import secure_filename
from os.path import join
from os import getcwd, mkdir
import base64
from model.variance_test import VarianceTest
from model.k_smirnoff_test import KolmogorovSmirnovTest
from model import constants, Utilities
import csv
from model import constants

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
    try:
        file = request.files['input-file']
        fileRoute = secure_filename(file.filename)
        file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

        path = getcwd() + "/files/" + file.filename
        meanTestClass = MeanTest.MeanTest(path)

        encoded_img = base64.b64encode(meanTestClass.generateGrafic().read()).decode('utf-8')

        return render_template('mean_test.html', randomNumbers=meanTestClass.randomNumbers, acept=meanTestClass.acept, error=meanTestClass.error,   n=meanTestClass.numberN, r=constants.FORMAT_NUMBER.format(meanTestClass.calculateMean()), alpha=constants.FORMAT_NUMBER.format(meanTestClass.alpha), z=constants.FORMAT_NUMBER.format(meanTestClass.z), li=constants.FORMAT_NUMBER.format(meanTestClass.calculateLI()), ls=constants.FORMAT_NUMBER.format(meanTestClass.calculateLS()), verify=meanTestClass.verifyTest(), grafic=encoded_img)
    except IOError:
        return meanTest()


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

@app.route('/chi_test', methods=["POST"])
def set_atributes_chi_test():
    try:
        file = request.files['input-file']
        fileRoute = secure_filename(file.filename)
        file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

        path = getcwd() + "/files/" + file.filename
    
        poker_test_class = chi2_test.chi2_test(path)

        encoded_img = base64.b64encode(poker_test_class.generateGrafic().read()).decode('utf-8')

        return render_template('/chi_test.html', grafic=encoded_img, randomNumbers=poker_test_class.random_numbers, sum=constants.FORMAT_NUMBER.format(poker_test_class.sum), chi2=constants.FORMAT_NUMBER.format(poker_test_class.chi2), matrix=poker_test_class.matrix, verify=poker_test_class.verify())
    except IOError:
        return chiTest()

@app.route('/poker_test')
def pokerTest():
    return render_template('poker_test.html')

@app.route('/poker_test', methods=["POST"])
def set_atributes_poker_test():
    try: 
        file = request.files['input-file']
        fileRoute = secure_filename(file.filename)
        file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

        path = getcwd() + "/files/" + file.filename
    
        poker_test_class = poker_test.poker_test(path)

        encoded_img = base64.b64encode(poker_test_class.generateGrafic().read()).decode('utf-8')

        return render_template('/poker_test.html', grafic=encoded_img, randomNumbers=poker_test_class.random_numbers, sum=constants.FORMAT_NUMBER.format(poker_test_class.sum), chi2=constants.FORMAT_NUMBER.format(poker_test_class.chi2), matrix=poker_test_class.matrix, verify=poker_test_class.verify())
    except IOError:
        return pokerTest()


if __name__ == '__main__':
    app.run(debug=True)
