from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/info')

def info():
    return jsonify({
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'You are doing great, human!!! XOXO',
        'deployed_on': 'kubernetes',
        'env': 'gitlab-test',
        'app_name': 'dev'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'staus': 'up'
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")

