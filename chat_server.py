from flask import Flask, request, jsonify
from collections import defaultdict

app = Flask(__name__)
messages = defaultdict(list)

@app.route('/send', methods=['POST'])
def send_message():
    data = request.get_json()
    from_user = data.get('from_user')
    to_user = data.get('to_user')
    message = data.get('message')

    if not from_user or not to_user or not message:
        return jsonify({'error': 'Invalid request'}), 400

    messages[to_user].append({
        'from_user': from_user,
        'message': message,
        'read': False
    })

    return jsonify({'status': 'Message sent'}), 200

@app.route('/messages', methods=['GET'])
def get_messages():
    user = request.args.get('user')

    if not user:
        return jsonify({'error': 'Invalid request'}), 400

    unread_messages = [m for m in messages[user] if not m['read']]
    for message in unread_messages:
        message['read'] = True

    return jsonify(unread_messages), 200

if __name__ == '__main__':
    app.run(debug=True)
