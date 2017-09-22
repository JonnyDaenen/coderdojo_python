import turtle

# maak de schildpad
bob = turtle.Turtle()
bob.shape('turtle')

# voor iedere kleur
for c in ['red', 'green', 'yellow', 'blue', 'orange', 'purple']:
    # moet bob het volgende doen
    bob.color(c)
    bob.forward(75)
    bob.left(60)
