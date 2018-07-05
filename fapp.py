from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/<name>', methods=['GET'])
def wish_hello(name):
    return jsonify({'response': "Hello " + name})

@app.route('/wish_me', methods=['GET'])
def name_as_params():
    name =  request.args.get('name')
    age =  request.args.get('age')
    # return jsonify({"name": name, "age": age})
    return jsonify(request.args)

if __name__ == '__main__':
    app.run(debug=True)
