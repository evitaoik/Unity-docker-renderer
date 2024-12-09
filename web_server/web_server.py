from flask import Flask, jsonify
import time

# Create a Flask application
app = Flask(__name__)

# Define a route to check if the server is up and decide whether to render graphics
@app.route('/should_render', methods=['GET'])
def should_render():
    # Simple logic to alternate between True and False for rendering
    # You can replace this with your custom logic
    return jsonify({"render": True})

# Run the app on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

