from flask import Flask, render_template, request
from model import MeanTest
from model.variance_test import VarianceTest
from model import constants
from utilities import utilities
import csv

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


@app.route('/poker_test')
def pokerTest():
    return render_template('poker_test.html')


if __name__ == '__main__':
    app.run(debug=True)
