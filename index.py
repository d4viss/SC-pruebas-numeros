from flask import Flask, render_template, request
from model import MeanTest
from model import poker_test
from model import chi2_test
from werkzeug.utils import secure_filename
from os.path import join
from os import getcwd, mkdir
import base64
from model.variance_test import VarianceTest
from model import constants
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
    file = request.files['input-file']
    fileRoute = secure_filename(file.filename)
    file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

    path = getcwd() + "/files/" + file.filename
    
    meanTestClass = MeanTest.MeanTest(path)

    encoded_img = base64.b64encode(meanTestClass.generateGrafic().read()).decode('utf-8')

    return render_template('mean_test.html', randomNumbers=meanTestClass.randomNumbers, acept=meanTestClass.acept, error=meanTestClass.error, n=meanTestClass.numberN, r=constants.FORMAT_NUMBER.format(meanTestClass.calculateMean()), alpha=constants.FORMAT_NUMBER.format(meanTestClass.alpha), z=constants.FORMAT_NUMBER.format(meanTestClass.z), li=constants.FORMAT_NUMBER.format(meanTestClass.calculateLI()), ls=constants.FORMAT_NUMBER.format(meanTestClass.calculateLS()), verify=meanTestClass.verifyTest(), grafic=encoded_img)


@app.route('/variance_test')
def varianceTest():
    return render_template('variance_test.html')


@app.route('/variance_test', methods=['POST'])
def set_numbers_in_variance_test():
    file = request.files['file']
    route = app.root_path+'/resources/variance_test/'
    file.save(route+file.filename)
    data_list = read_file(route, file)
    variance_test = VarianceTest(data_list)
    ri_list = variance_test.__getattribute__("ri_list")
    length = len(ri_list)
    mean = variance_test.calculate_variance()
    variance = variance_test.calculate_variance()
    chi_inv1 = variance_test.calculate_chi_inv(constants.ALPHA_HALF)
    chi_inv2 = variance_test.calculate_chi_inv(constants.ONE_MINUS_ALPHA_HALF)
    lower_limit = variance_test.calculate_limit(True, chi_inv1)
    upper_limit = variance_test.calculate_limit(False, chi_inv2)
    is_valid = variance_test.is_valid_test(lower_limit, upper_limit, variance)
    return render_template('variance_test.html', ri_list=ri_list, length=length, mean=mean, variance=variance, alpha_half=constants.ALPHA_HALF, chi_inv1=chi_inv1, chi_inv2=chi_inv2,lower_limit=lower_limit, upper_limit=upper_limit, is_valid = is_valid)


def read_file(route, file):
    with open(route+file.filename, newline='') as file_csv:
        data = csv.reader(file_csv)
        data_list = []
        for row in data:
            data_row = []
            for value in row:
                if value != '':
                    data_row.append(float(value.replace(',', '.')))
            data_list = data_list + data_row
        return data_list

@app.route('/ks_test')
def ksTest():
    return render_template('ks_test.html')


@app.route('/chi_test')
def chiTest():
    return render_template('chi_test.html')

@app.route('/chi_test', methods=["POST"])
def set_atributes_chi_test():
    file = request.files['input-file']
    fileRoute = secure_filename(file.filename)
    file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

    path = getcwd() + "/files/" + file.filename
    
    poker_test_class = chi2_test.chi2_test(path)

    encoded_img = base64.b64encode(poker_test_class.generateGrafic().read()).decode('utf-8')

    return render_template('/chi_test.html', grafic=encoded_img, randomNumbers=poker_test_class.random_numbers, sum=constants.FORMAT_NUMBER.format(poker_test_class.sum), chi2=constants.FORMAT_NUMBER.format(poker_test_class.chi2), matrix=poker_test_class.matrix, verify=poker_test_class.verify())

@app.route('/poker_test')
def pokerTest():
    return render_template('poker_test.html')

@app.route('/poker_test', methods=["POST"])
def set_atributes_poker_test():
    file = request.files['input-file']
    fileRoute = secure_filename(file.filename)
    file.save(join(app.config['UPLOAD_FOLDER'], fileRoute))

    path = getcwd() + "/files/" + file.filename
    
    poker_test_class = poker_test.poker_test(path)

    encoded_img = base64.b64encode(poker_test_class.generateGrafic().read()).decode('utf-8')

    return render_template('/poker_test.html', grafic=encoded_img, randomNumbers=poker_test_class.random_numbers, sum=constants.FORMAT_NUMBER.format(poker_test_class.sum), chi2=constants.FORMAT_NUMBER.format(poker_test_class.chi2), matrix=poker_test_class.matrix, verify=poker_test_class.verify())


if __name__ == '__main__':
    app.run(debug=True)
