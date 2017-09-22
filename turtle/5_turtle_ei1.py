import turtle

# maak de schildpad
bob = turtle.Turtle()
bob.shape('turtle')

# instellingen
aantal = 10
sprong_lengte = 20

# bob mag zijn pen niet neerzetten
bob.penup()

# bob moet 'aantal' keer springen
for nummer in range(aantal):
  # bob teken
  bob.dot()
  bob.forward(sprong_lengte)
