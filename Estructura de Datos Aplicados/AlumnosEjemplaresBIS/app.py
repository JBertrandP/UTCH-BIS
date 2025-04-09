from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

MAX_QUEUE_SIZE = 10

queue = []
waitlist = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')

    if not username:
        return jsonify({"message": "Username cannot be empty"}), 400

    if username in queue or username in waitlist:
        return jsonify({"message": "Username already in queue or waitlist"}), 400

    if len(queue) < MAX_QUEUE_SIZE:
        queue.append(username)
        return jsonify({"message": f"{username} added to the queue"}), 200
    else:
        waitlist.append(username)
        return jsonify({"message": f"Queue is full. {username} added to the waitlist"}), 200

@app.route('/remove_user', methods=['POST'])
def remove_user():
    data = request.get_json()
    username = data.get('username')

    if username in queue:
        queue.remove(username)
        if waitlist:
            next_user = waitlist.pop(0)
            queue.append(next_user)
        return jsonify({"message": f"{username} removed from queue"}), 200
    else:
        return jsonify({"message": "User not found in queue"}), 404

@app.route('/list_users', methods=['GET'])
def list_users():
    return jsonify({"queue": queue, "waitlist": waitlist})

if __name__ == '__main__':
    app.run(debug=True)
