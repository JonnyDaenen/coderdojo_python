import turtle

# maak de schildpad
bob = turtle.Turtle()
bob.shape('turtle')

for c in ['red', 'green', 'yellow', 'blue', 'orange', 'purple']:
    bob.color(c)
    bob.forward(75)
    bob.left(60)
