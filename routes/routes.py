
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		),
		(
			r"/projects",
			dataController.projectHandler
		),
		(
			r"/members",
			dataController.membersHandler
		),
		(
			r"/events",
			dataController.eventHandler
		)
]
					