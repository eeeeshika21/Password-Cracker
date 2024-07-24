from flask import Flask, request, jsonify
import hashlib
from itertools import product

app = Flask(__name__)

# Define a small dictionary for the dictionary attack
dictionary = ["password", "123456", "123456789", "qwerty", "abc123"]

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def brute_force_attack(hash):
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    max_length = 5  # Limit length for demonstration purposes
    for length in range(1, max_length + 1):
        for attempt in product(chars, repeat=length):
            attempt = ''.join(attempt)
            if hash_password(attempt) == hash:
                return attempt
    return None

def dictionary_attack(hash):
    for word in dictionary:
        if hash_password(word) == hash:
            return word
    return None

@app.route('/crack', methods=['POST'])
def crack_password():
    data = request.json
    hash = data['hash']
    attack_type = data['attackType']

    if attack_type == 'brute':
        password = brute_force_attack(hash)
    elif attack_type == 'dictionary':
        password = dictionary_attack(hash)
    else:
        return jsonify({"error": "Invalid attack type"}), 400

    return jsonify({"password": password})

if __name__ == '__main__':
    app.run(debug=True)
