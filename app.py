from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
  @app.route('/subscribe', methods=['POST'])
def subscribe():
    # ✅ THE FIX: Match the HTML names
    name = request.form.get('name_input')
    email = request.form.get('email_input')

    # Save to file
    with open('subscribers.txt', 'a') as file:
        file.write(f"{name} | {email}\n")

    # Show success page
    return render_template('success.html', name=name)
    # 3. Show the success page
    return render_template('success.html', name=name, email_address=email)
# A secret route to view the file
@app.route('/check')
def check_list():
    try:
        # Open the file in 'read' mode
        with open('subscribers.txt', 'r') as file:
            content = file.read()
        # Replace newlines with HTML breaks so it looks nice
        return f"<h1>Subscriber List:</h1><br><pre>{content}</pre>"
    except FileNotFoundError:
        return "No subscribers yet (or file was lost)."
if __name__ == '__main__':

    app.run(debug=True)
