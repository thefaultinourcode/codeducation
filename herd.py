import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
wn.bgcolor("lightgreen")
wn.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)

turtle.mainloop()

#alex = turtle.Turtle()    # Create a turtle, assign to alex

#alex.forward(50)          # Tell alex to move forward by 50 units
#alex.left(90)             # Tell alex to turn by 90 degrees
#alex.forward(30)          # Complete the second side of a rectangle

#turtle.mainloop()             # Wait for user to close window