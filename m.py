from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html', name='John Doe', number=30, numbers=[1, 2, 3, 4, 5])


@app.route('/second')
def second():
    return render_template('second.html')

@app.route('/math/<int:num>')
def math(num):
    result = num * 2
    return render_template('math.html', number=num, result=result)

num = 10


@app.route("/number/<int:num>")
def number(num):
    return f"result: {num * 2}"



if __name__ == '__main__':
    app.run(debug=True)


