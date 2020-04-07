from flask import Flask , request , Response , jsonify 

app = Flask(__name__)

USERS = {}
GET = 'GET'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/user/<username>", methods=[GET])
def access_users(username):
    if request.method == GET:
        user_details = USERS.get(username)
        if user_details:
            return jsonify(user_details)
        else:
            return Response(status=404)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port='5000', debug=True)