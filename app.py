from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    # 1. Grab the data from the form
    name = request.form['first_name']
    email = request.form['email']

    # 2. Open the "notebook" file and write the data
    # 'a' stands for "Append" (add to the end)
    with open('subscribers.txt', 'a') as file:
        file.write(name + " | " + email + "\n")

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