from flask import Flask, jsonify

app = Flask(__name__)

media_global = 0.0

@app.route('/media', methods=['GET'])
def get_media():
    return jsonify({"media": media_global})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
