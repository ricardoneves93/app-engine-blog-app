from flask import Flask, jsonify, request
from google.cloud import datastore
from datetime import datetime
from flask_api import status

# Init datastore
datastore_client = datastore.Client()

app = Flask(__name__)

datastore_post_kind = 'post'
datastore_post_namespace = 'blog-app'

@app.route('/post')
def get_posts():
	post_query = datastore_client.query(kind=datastore_post_kind, namespace=datastore_post_namespace)

	post_query_results = list(post_query.fetch())

	posts = []
	for post_from_db in post_query_results:

		post = {
			"id": post_from_db.key.id_or_name,
			"title": post_from_db['title'],
			"subtitle": post_from_db['subtitle'],
			"content": post_from_db['content'],
			"author": post_from_db['author'],
			"date_posted": post_from_db['date-posted'].strftime('%B %-d, %Y'),
		}

		posts.append(post)

	return jsonify(posts), status.HTTP_200_OK


@app.route('/post/<int:post_id>')
def get_post_by_id(post_id):
	post_key = datastore_client.key(datastore_post_kind, post_id, namespace=datastore_post_namespace)

	post_from_db = datastore_client.get(post_key)

	print(post_from_db)

	post = {
			"id": post_from_db.key.id_or_name,
			"title": post_from_db['title'],
			"subtitle": post_from_db['subtitle'],
			"content": post_from_db['content'],
			"author": post_from_db['author'],
			"date_posted": post_from_db['date-posted'].strftime('%B %-d, %Y'),
		}

	return jsonify(post), status.HTTP_200_OK

@app.route('/post', methods=['POST'])
def create_post():
	post = request.json

	# Create the post
	post_key = datastore_client.key(datastore_post_kind, namespace=datastore_post_namespace)

	entity = datastore.Entity(key=post_key, exclude_from_indexes=['content'])

	entity.update({
		"title": post['title'],
		"subtitle": post['subtitle'],
		"author": post['author'],
		"content": post['content'],
		"date-posted": datetime.now()
	})

	datastore_client.put(entity)

	return "", status.HTTP_201_CREATED


if __name__ == '__main__':
	app.run(port=5001, debug=True)