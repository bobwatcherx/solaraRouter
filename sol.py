from solara import *

# NOW DEFINE ROUTES HERE
routes = [
	Route(path="/"),
	Route(path="about"),
]

# NOW I CREATE 2 COMPONENT HOME AND ABOUT

@solara.component
def Home():
	with Column():
		Title("My Home")
	# CREATE CARD
	with Card():
		Markdown("welcome HOME",
			style={"font-size":"30px"}
			)
		# AND CREATE BUTTON LINK TO SECOND PAGE
		with Link("/about"):
			Button("About page",color="primary")

# NOW CREATE ABOUT COMPONENT
@solara.component
def About():
	with Column():
		Title("ABOUT")
	with Card():
		Markdown("THIS ABOUT PAGE",
			style={"font-size":"30px"}
			)
		with Link("/"):
			Button("BACK TO HOME",color="red")



@solara.component
def Page():
	# AND NOW REGISTER component AND ROUTE HERE
	router = solara.use_router()
	# YOU SEE ROUTER RESULT IN TERMINAL
	print(router.path,router.search)
	path = router.path
	# REMOVE / IF /about THEN RESULT IS about
	parts = path.split("/")
	print("Result",parts)

	# NOW DEFINE ROUTER AND VIEW COMPonent
	if parts[1] == "":
		return Home()
	if parts[1] == "about":
		return About()
	