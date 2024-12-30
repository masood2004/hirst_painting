# Import necessary modules
from turtle import Turtle, Screen
import random

# Uncommented code for extracting RGB colors from an image (Hirst painting).
# This code uses the colorgram library to extract colors, but it is not currently used in this script.

# from colorgram import colorgram as cg
# extracted = cg.extract('hirst-painting.jpg', 30)
# colors_list = []
# for x in range(30):
#     r = (extracted[x].rgb.r)
#     g = (extracted[x].rgb.g)
#     b = (extracted[x].rgb.b)
#     colors_list.append((r, g, b))
# print(colors_list)

# List of pre-extracted colors (manually copied from the Hirst painting)
colours_list = [
    (2, 9, 30), (122, 95, 41), (72, 32, 22), (237, 212, 72), (220, 81, 59),
    (225, 117, 100), (93, 1, 21), (178, 140, 170), (150, 92, 115), (34, 90, 26),
    (7, 154, 73), (205, 63, 91), (168, 129, 77), (1, 64, 147), (4, 221, 218),
    (3, 78, 28), (220, 178, 218), (79, 135, 179), (124, 154, 178), (80, 110, 138),
    (121, 185, 164), (10, 214, 221), (121, 13, 33), (243, 204, 7), (133, 222, 208),
    (229, 174, 165)
]

# Function to return a random color from the list


def random_color():
    return random.choice(colours_list)


# Set up the screen
screen = Screen()
screen.colormode(255)  # Enable 255 RGB color mode

# Create the turtle object
t = Turtle()
t.speed("fast")  # Increase the speed of pen for faster drawing
t.penup()  # Lift the pen so it doesn't draw while moving
t.goto(-250, -250)  # Move the turtle to the starting position

# Function to draw a dot, move forward, and draw another dot


def dot_forward_dot():
    t.dot(20, random_color())  # Draw a dot with random color
    t.penup()  # Lift the pen to avoid drawing a line
    t.forward(50)  # Move forward by 50 pixels
    t.dot(20, random_color())  # Draw another dot with random color


# Variable for the y-axis starting position
y_axis = -200

# Nested loops to create a grid of dots
for y in range(10):  # Loop to create 10 rows
    for x in range(10):  # Loop to create 10 dots in each row
        dot_forward_dot()
    t.goto(-250, y_axis)  # Move the turtle to the start of the next row
    y_axis += 50  # Increment the y-axis position for the next row

# Close the screen when clicked
screen.exitonclick()
