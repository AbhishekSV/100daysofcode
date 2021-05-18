from turtle import Turtle, colormode, Screen

color_palette = [(249, 248, 248), (237, 241, 246), (238, 246, 244), (249, 243, 247), (1, 12, 31), (54, 25, 17), (218, 127, 106), (9, 104, 160), (242, 213, 68), (150, 83, 39), (216, 86, 63), (156, 6, 24), (165, 162, 30), (158, 62, 102), (207, 73, 103), (10, 64, 33), (11, 96, 57), (95, 6, 20), (175, 134, 162), (7, 173, 217), (1, 61, 145), (2, 213, 207), (158, 32, 23), (8, 140, 85), (144, 227, 217), (121, 193, 147), (220, 177, 216), (100, 218, 229), (251, 198, 1), (116, 170, 192)]

tory = Turtle()
tory.shape('turtle')
tory.color('aquamarine')
colormode(255)

# # Draws a square
# for _ in range(50):
#     tory.forward(100)
#     tory.left(90)

# # Draws a dotted line
# for _ in range(25):
#     tory.forward(5)
#     tory.penup()
#     tory.forward(5)
#     tory.pendown()

# # Draws symmetric shapes from triangle to decagon with random colors
# for i in range(3,11):
#     angle = 360 / i
#     color = (randint(0,255), randint(0,255), randint(0,255))
#     for j in range(i):
#         tory.pencolor(color)
#         tory.forward(100)
#         tory.right(angle)

# # Draws random walk with random colors
# angles = [90, 180, 270, 360]
# for _ in range(100):
#     color = (randint(0,255), randint(0,255), randint(0,255))
#     tory.pen(pensize = 10, pencolor = color, speed = 10)
#     tory.forward(50)
#     tory.setheading(choice(angles))

# # Draws spirograph with random colors
# for i in range(5, 361, 5):
#     color = (randint(0,255), randint(0,255), randint(0,255))
#     tory.pen(pencolor = color, speed = 10)
#     tory.circle(100)
#     tory.setheading(i)

# from random import randint, choice
# import colorgram as col
# color_palette = []
# # Extract 30 colors from an image.
# colors = col.extract('/Users/abhisheksabnivis/Desktop/100daysofcode/Day 18/spot_painting.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r, g, b)
#     color_palette.append(color_rgb)
# print(color_palette)


canvas = Screen()
canvas.exitonclick()