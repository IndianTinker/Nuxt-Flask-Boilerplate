from flask import Flask, render_template, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/api')
def api():
    my_dict = {"user": {"name": "Lucas", "age": "28"}}
    return json.dumps(my_dict)


if __name__ == "__main__":
    print("Server is running on localhost")
    app.run(debug=True)
