from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)



# To render a login form 
@app.route('/')
def view_form():
    return render_template('temperature.html')


@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        temperature = request.args['temperature']
        print(temperature)
        return 'hello this is the get method'
    else:
        return render_template('temperature.html')


@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        temperature = request.form['temperature']
        print(temperature)
        return 'hello this is the post method'
    else:
        return render_template('temperature.html')

if __name__ == '__main__':
    app.run()