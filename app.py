from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'harini-secret-key'  # Needed for session

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
        session['attempts'] = 0

    message = ""

    if request.method == 'POST':
        guess = request.form.get('guess')

        try:
            guess = int(guess)
            session['attempts'] += 1
            number = session['number']

            if guess < number:
                message = "Too low!"
            elif guess > number:
                message = "Too high!"
            else:
                message = f"🎉 Correct! You guessed the number in {session['attempts']} attempts."
                session.pop('number')
                session.pop('attempts')
        except ValueError:
            message = "Please enter a valid number."

    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
