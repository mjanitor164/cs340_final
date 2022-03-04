from flask import Flask, render_template
import os

# Configuration

app = Flask(__name__)

# Routes 

@app.route('/')
def root():
	
	return render_template('index.html')

# Listener

if __name__ == "__main__":
    
	app.run(host="0.0.0.0", port=8766, debug=True) 

