from flask import Flask, render_template, json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/data-visualization')
def data_visualization(): 	
	return render_template('data_visualization.html')

@app.route('/input')
def input(): 	
	return render_template('input.html')


@app.route('/test')
def test():
	my_dict = { "title": "Assessment IKE Analytics"}
	return json.dumps(my_dict)


if __name__ == "__main__":
	print('Server is running!')
	app.run(debug=True)