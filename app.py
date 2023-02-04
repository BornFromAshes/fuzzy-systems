from flask import Flask, render_template, request
from final_result import ProvideResult

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def final_result():
    input_dict = request.form.to_dict()
    input_dict = {'chest_pain': '1', 'cholestrol': '210', 'ecg': '0.1', 'exercise': '1', 'thallium_scan': '3', 'age': '20', 'blood_pressure': '134', 'blood_sugar': '110', 'heart_rate': '137', 'old_peak': '1.7', 'sex': '0'}
    # print(input_dict)
    provide_result = ProvideResult()
    output = provide_result.get_final_result(input_dict=input_dict)
    return render_template('result.html', output=output)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8448, debug=True)
