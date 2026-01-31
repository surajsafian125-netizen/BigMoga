from flask import Flask, render_template, request

app = Flask(__name__)

# --- HOME PAGE ---
@app.route('/')
def home():
    return render_template('index.html')

# --- SUBSCRIBE ENGINE ---
@app.route('/subscribe', methods=['POST'])
def subscribe():
    # 1. Get data (using the correct HTML names)
    name = request.form.get('name_input')
    email = request.form.get('email_input')

    # 2. Save to file
    with open('subscribers.txt', 'a') as file:
        file.write(f"{name} | {email}\n")

    # 3. Show success page
    return render_template('success.html', name=name)

# --- SECRET CHECK PAGE ---
@app.route('/check')
def check_list():
    try:
        with open('subscribers.txt', 'r') as file:
            content = file.read()
        return f"<h1>Subscriber List:</h1><br><pre>{content}</pre>"
    except FileNotFoundError:
        return "No subscribers yet."

# --- START THE APP ---
if __name__ == '__main__':
    app.run(debug=True)
