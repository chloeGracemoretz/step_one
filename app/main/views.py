from flask import render_template,redirect,url_for,request,jsonify
from . import main
@main.route('/',methods=['POST','GET'])
def index():

		return render_template('index.html')
@main.route('/addition')
def addition():
	a=request.args.get('a',0,type=int)
	b=request.args.get('b',0,type=int)
	result=a+b

	return jsonify(result=result)
@main.route('/about')
def about():
	
	return render_template('about.html')	
@main.route('/test')
def test():
	dist=[]
	txt1="This is a test."
	txt2="Good night"
	dist.append(txt1)
	dist.append(txt2)
	return jsonify(result=dist)