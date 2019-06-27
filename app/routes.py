from app import app
@app.route('/')

@app.route('/index')
def index():
	return """
<html>
<head><title>burrraahhh</title></head>
<body>
<p>hello</p>
</body>
</html>
"""