
'''
Preset controller by torn for / route
'''
from modules import *
import env
import json
mlabKey = env.MLAB_API
baseURL = env.BASE_URL
import requests
class projectHandler(tornado.web.RequestHandler):
	def get(self):
		payload = {'apiKey':mlabKey}
		projects  = requests.get(baseURL+"databases/gdg-vit/collections/projects", params=payload)

		ob = {
			'status':'OK',
			'projects':json.loads(projects.text),
			'reponse':'Application running'
		}
		self.write(tornado.escape.json_encode(ob))
class eventHandler(tornado.web.RequestHandler):
	def get(self):
		payload = {'apiKey':mlabKey}
		events  = requests.get(baseURL+"databases/gdg-vit/collections/events", params=payload)

		ob = {
			'status':'OK',
			'events':json.loads(events.text),
			'reponse':'Application running'
		}
		self.write(tornado.escape.json_encode(ob))

class membersHandler(tornado.web.RequestHandler):
	def get(self):
		payload = {'apiKey':mlabKey}
		members  = requests.get(baseURL+"databases/gdg-vit/collections/members", params=payload)

		ob = {
			'status':'OK',
			'members':json.loads(members.text),
			'reponse':'Application running'
		}
		self.write(tornado.escape.json_encode(ob))

					