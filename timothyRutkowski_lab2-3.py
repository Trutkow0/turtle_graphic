# Timothy Rutkowski 2/01/2024 timothyRutkowski_lab2-3.py
# This program uses turtle graphics to create an image

# Gets turtle module
import turtle

# Draws two connected diamonds
# Begins first diamond
turtle.right(45)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(200) # Ends first diamond and continues into second diamond using same side
# Begins second diamond
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.right(90)
turtle.forward(100)

# Draws two triangles, one within the other using the same base for both triangles
# Begins first/outer triangle in center where diamonds meet
turtle.left(45)
turtle.forward(75) # Sets corner for both triangles in the center of the first diamond
turtle.left(115)
turtle.forward(175) # Top of first/outer triangle
turtle.left(130)
turtle.forward(175)
turtle.left(115)
turtle.forward(148) # Finishes drawing the base for both triangles and sets corner for second/inner triangle
# Begins second/inner triangle
turtle.left(145)
turtle.forward(90) # Top of second/inner triangle
turtle.left(70)
turtle.forward(90)

# Terminates turtle program with graphics remaining on the screen
turtle.done()