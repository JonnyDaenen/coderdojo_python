import turtle

# maak de schildpad
bob = turtle.Turtle()
bob.shape('turtle')


# we geven bob 4x het zelfde bevel
for i in range(4):
    bob.forward(50)
    bob.right(90)
