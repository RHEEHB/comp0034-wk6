from flask import current_app as app
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    """
    Returns a view (HTML page) with a greeting message 'Hello, world'.
    """
    return render_template('index.html')
