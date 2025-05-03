from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import json
from encryption import xor_encrypt_decrypt
from chat_features import ChatFeatures
from user_manager import UserManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

# Initialize user manager
user_manager = UserManager()

# Store connected users
connected_users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email', '')
    
    if not username or not password:
        return jsonify({'success': False, 'message': 'Username and password are required'})
    
    success, message = user_manager.add_user(username, password, email)
    return jsonify({'success': success, 'message': message})

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    # Remove user from connected users
    for username, sid in list(connected_users.items()):
        if sid == request.sid:
            del connected_users[username]
            emit('user_status', {'username': username, 'status': 'offline'}, broadcast=True)
            break

@socketio.on('login')
def handle_login(data):
    username = data['username']
    password = data['password']
    
    # Verify user credentials
    success, message = user_manager.verify_user(username, password)
    
    if success:
        connected_users[username] = request.sid
        emit('login_success', {'username': username})
        emit('user_status', {'username': username, 'status': 'online'}, broadcast=True)
        emit('user_list', {'users': list(connected_users.keys())}, broadcast=True)
    else:
        emit('login_error', {'message': message})

@socketio.on('message')
def handle_message(data):
    username = data['username']
    message = data['message']
    
    # Format message
    formatted_msg = ChatFeatures.format_message(message)
    msg_obj = ChatFeatures.create_message(username, formatted_msg)
    
    # Broadcast message to all clients
    emit('message', msg_obj, broadcast=True)

@socketio.on('file')
def handle_file(data):
    username = data['username']
    file_data = data['file']
    file_info = data['info']
    
    # Create file message
    file_msg = ChatFeatures.create_message(
        username,
        {"data": file_data, "info": file_info},
        "file"
    )
    
    # Broadcast file to all clients
    emit('file', file_msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True) 