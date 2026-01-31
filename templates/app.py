from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # ✅ FIX: We now use the names that match your HTML form
    name = request.form.get('name_input')
    email = request.form.get('email_input')

    # Save to file
    with open('subscribers.txt', 'a') as file:
        file.write(f"{name} | {email}\n")

    # Show success page
    return render_template('success.html', name=name)

# The Secret Route
@app.route('/check')
def check_list():
    try:
        with open('subscribers.txt', 'r') as file:
            content = file.read()
        return f"<h1>Subscriber List:</h1><br><pre>{content}</pre>"
    except FileNotFoundError:
        return "No subscribers yet."

if __name__ == '__main__':
    app.run(debug=True)