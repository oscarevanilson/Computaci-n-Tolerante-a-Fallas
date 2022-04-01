from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return 'Ejemplo Kubernetes'

if __name__ == "__main__":
    app.run()