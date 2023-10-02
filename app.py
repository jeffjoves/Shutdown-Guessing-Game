from flask import Flask, render_template, request
import random
import os
import platform

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_number', methods=['POST'])
def check_number():
    try:
        myNumber = int(request.form['number'])
        computerChoice = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = random.choice(computerChoice)
        message = ""

        if myNumber == result:
            message = "Congratulations! You're lucky!"
        else:
            system_platform = platform.system()
            message = "Sorry, you lose. Shutting down..."
            if system_platform == "Linux":
                os.system("poweroff")
            elif system_platform == "Windows":
                os.system("shutdown /s /t 0")
            elif system_platform == "Darwin":
                os.system("shutdown -h now")
            else:
                message = "Shutdown not supported on this operating system."
        return render_template('index.html', message=message, result=result)
    except ValueError:
        return render_template('index.html', message="Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    app.run(debug=False, port=5000)

