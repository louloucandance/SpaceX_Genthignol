class Robot:

	# robot r = (nom, abscisse, ordonnee, resources, etat)
    def __init__(self, name,x,y):
        self.name = name    # instance variable unique to each instance
        self.state = "CONNECTED"
        self.coordinates = (x,y)
        self.resources = 0

    def set_state(self, s):
      	self.state = s

	def set_coordinates(self, x, y):
        self.coordinates = (x,y)

    def set_name(self, name):
        self.name = name

    def set_resources(self, nb_resources):
        self.resources = nb_resources

    def resourses_gather(self, r):
        self.resourses += r

    def move_robot(self, x, y):
        self.set_coordinates=(x,y)
