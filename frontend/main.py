import requests
import json

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

#backend_url='http://localhost:5001'

backend_url='https://backend-dot-blog-app-edu.appspot.com'

class Post:
	def __init__(self, id, title, subtitle, content, author, date_posted):
		self.id = id
		self.title = title
		self.subtitle = subtitle
		self.content = content
		self.author = author
		self.date_posted = date_posted

@app.route('/')
def index():
	complete_url = backend_url + "/post"

	response = requests.get(complete_url)

	json_data = json.loads(response.text)

	posts = []
	for post in json_data:
		post = Post(post['id'], post['title'], 
			post['subtitle'], post['content'], post['author'], 
			post['date_posted'])

		posts.append(post)


	return render_template('index.html', posts=posts)

@app.route('/post/<string:post_id>')
def post(post_id):

	complete_url = backend_url + "/post/" + post_id

	response = requests.get(complete_url)

	json_data = json.loads(response.text)

	post = Post(json_data['id'], json_data['title'], 
		json_data['subtitle'], json_data['content'], json_data['author'], 
		json_data['date_posted'])

	return render_template('post.html', post=post)

@app.route('/create')
def create():
	return render_template('create.html')

@app.route('/createPost', methods=['POST'])
def create_post():

	post = {
			"title": request.form['title'],
			"subtitle": request.form['subtitle'],
			"content": request.form['content'],
			"author": request.form['author'],
		}

	complete_url = backend_url + "/post"

	requests.post(url = complete_url, json = post)

	return redirect(url_for('index'))


if __name__ == '__main__':
	app.run(port=5000, debug=True)