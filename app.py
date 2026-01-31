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

if __name__ == '__main__':
    app.run(debug=True)