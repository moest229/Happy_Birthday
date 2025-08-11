from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def input_name():
    if request.method == 'POST':
        name = request.form.get('name')
        return render_template('surprise.html', name=name)
    return render_template('input.html')

if __name__ == '__main__':
    app.run(debug=True)