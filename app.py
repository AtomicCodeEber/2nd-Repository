from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    answers = [
        request.form['q_0'],
        request.form['q_1'],
        request.form['q_2'],
        request.form['q_3'],
        request.form['q_4'],
        request.form['q_5'],
        request.form['q_6'],
        request.form['q_7'],
        request.form['q_8'],
        request.form['q_9'],
        request.form['q_10'],
        request.form['q_11'],
        request.form['q_12'],
        request.form['q_13'],
        request.form['q_14'],
        request.form['q_15'],
        request.form['q_16'],
        request.form['q_17'],
        request.form['q_18']
    ]

    score = sum([int(answer) for answer in answers])
    result_message = "Felicidades, tu puntaje fue de {} puntos. Ganaste un dulce a elegir.".format(score) if score >= 13 else "Desafortunadamente reprobaste, tendrás que repasar el tema."

    return render_template('result.html', score=score, result_message=result_message)

if __name__ == '__main__':
    app.run(debug=True)