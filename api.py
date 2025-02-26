from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    print("Hello World!")  # Print to terminal
    return "Hello World!"

if __name__ == '__main__':
    print(" Hit the API to see the message!")
    app.run()