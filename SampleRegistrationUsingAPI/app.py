from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# In-memory storage for registered users
registered_users = []

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.form

    username = data.get('username')
    password = data.get('password')
    name = data.get('name')
    mobile_number = data.get('mobile_number')
    address = data.get('address')

    if not username or not password or not name or not mobile_number or not address:
        return jsonify({'error': 'Please provide all required information'}), 400

    new_user = {
        'username': username,
        'password': password,
        'name': name,
        'mobile_number': mobile_number,
        'address': address
    }

    registered_users.append(new_user)

    return jsonify({'message': 'Registration successful'}), 201

if __name__ == '__main__':
    app.run(debug=True)