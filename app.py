from flask import Flask, render_template, request
import itertools
import string
import time

app = Flask(__name__)

def simple_password_cracker(target_password, max_length=5):
    characters = string.ascii_letters + string.digits + string.punctuation
    start_time = time.time()
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess = ''.join(guess)
            if guess == target_password:
                end_time = time.time()
                return guess, end_time - start_time
    return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target_password = request.form['password']
        max_length = int(request.form['max_length'])
        cracked_password, time_taken = simple_password_cracker(target_password, max_length)
        return render_template('index.html', password=target_password, cracked_password=cracked_password, time_taken=time_taken)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
