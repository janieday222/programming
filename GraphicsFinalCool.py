#Five Colorful Balls Bouncing Around on a Pink TV Screen

from graphics import *
from time import *
from random import *
from math import sqrt

win = GraphWin("My Program", 1000, 700)
win.setCoords(0, 0, 1000, 700)
win.setBackground("black")

#Adds pink TV image to the window:
image = Image(Point(570, 410), "pinktv.gif")
image.draw(win)

#Adds text instructions to the window:
message = Text(Point(400, 400), "click the screen to start")
message2 = Text(Point(400, 380), "press a key to end :)")
message.setTextColor("light pink")
message2.setTextColor("light pink")
message.setFace("courier")
message2.setFace("courier")
message.draw(win)
message2.draw(win)

#Adds five colored circles to the window:
cute_circle = Circle(Point(500,250), 30)
cute_circle.draw(win)
cute_circle.setFill("pale violet red")
cute_circle.setOutline("pale violet red")

pretty_circle = Circle(Point(550,400), 30)
pretty_circle.draw(win)
pretty_circle.setFill("plum")
pretty_circle.setOutline("plum")

nice_circle = Circle(Point(330,250), 30)
nice_circle.draw(win)
nice_circle.setFill("peach puff")
nice_circle.setOutline("peach puff")

cool_circle = Circle(Point(250,400), 30)
cool_circle.draw(win)
cool_circle.setFill("dark sea green")
cool_circle.setOutline("dark sea green")

fire_circle = Circle(Point(400,500), 30)
fire_circle.draw(win)
fire_circle.setFill("light sky blue")
fire_circle.setOutline("light sky blue")

#Picks how much each circle will move along the x and y axes:
dx = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])    #picks random length in this range to move every 0.005 secs along x axis
dy = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])                               #made this range so it won't go too slow

dx2 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
dy2 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])

dx3 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
dy3 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])

dx4 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
dy4 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])

dx5 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])
dy5 = choice([-10, -9, -8, -7, -6, 6, 7, 8, 9, 10])

key = win.checkKey()                #circles will keep moving until user presses a key
clickPoint = win.getMouse()         #circles start moving when the window is clicked


#Makes circles bounce off the edges of the pink tv screen and off eachother:
while key == "":
    cute_circle.move(dx, dy)                    #dx is movement along x axis and dy is movement along y axis
    sleep(0.0025)                             #circle will wait 0.0025 seconds before moving again
    center = cute_circle.getCenter()
    x = center.getX()                           #gets the x coordinate of the center
    if (x - 30) <= 90 or (x + 30) >= 700:    #-30 and +30 account for the radius of the circle so it doesn't bounce off at center of circle
        dx = -dx                                #when it bounces off wall, the ball moves in the opposite direction as it was
    y = center.getY()
    if (y - 30) <= 125 or (y + 30) >= 590:
        dy = -dy

    pretty_circle.move(dx2, dy2)
    sleep(0.005)
    center2 = pretty_circle.getCenter()
    x2 = center2.getX()
    if (x2 - 30) <= 90 or (x2 + 30) >= 700:
        dx2 = -dx2
    y2 = center2.getY()
    if (y2 - 30) <= 125 or (y2 + 30) >= 590:
        dy2 = -dy2

    nice_circle.move(dx3, dy3)
    sleep(0.005)
    center3 = nice_circle.getCenter()
    x3 = center3.getX()
    if (x3 - 30) <= 90 or (x3 + 30) >= 700:
        dx3 = -dx3
    y3 = center3.getY()
    if (y3 - 30) <= 125 or (y3 + 30) >= 590:
        dy3 = -dy3

    cool_circle.move(dx4, dy4)
    sleep(0.005)
    center4 = cool_circle.getCenter()
    x4 = center4.getX()
    if (x4 - 30) <= 90 or (x4 + 30) >= 700:
        dx4 = -dx4
    y4 = center4.getY()
    if (y4 - 30) <= 125 or (y4 + 30) >= 590:
        dy4 = -dy4

    fire_circle.move(dx5, dy5)
    sleep(0.005)
    center5 = fire_circle.getCenter()
    x5 = center5.getX()
    if (x5 - 30) <= 90 or (x5 + 30) >= 700:
        dx5 = -dx5
    y5 = center5.getY()
    if (y5 - 30) <= 125 or (y5 + 30) >= 590:
        dy5 = -dy5

    distance = sqrt((x2 - x)*(x2 - x)+(y2 - y)*(y2 - y))
    if distance <= 60:   #if the distance between the two centers of the circles is = to the sum of the two radii, they have collided
        dx = -dx
        dy = -dy
        dx2 = -dx2
        dy2 = -dy2

    distance2 = sqrt((x3 - x)*(x3 - x)+(y3 - y)*(y3 - y))
    if distance2 <= 60:
        dx = -dx
        dy = -dy
        dx3 = -dx3
        dy3 = -dy3

    distance3 = sqrt((x4 - x)*(x4 - x)+(y4 - y)*(y4 - y))
    if distance3 <= 60:
        dx = -dx
        dy = -dy
        dx4 = -dx4
        dy4 = -dy4

    distance4 = sqrt((x5 - x)*(x5 - x)+(y5 - y)*(y5 - y))
    if distance4 <= 60:
        dx = -dx
        dy = -dy
        dx5 = -dx5
        dy5 = -dy5

    distance5 = sqrt((x3 - x2)*(x3 - x2)+(y3 - y2)*(y3 - y2))
    if distance5 <= 60:
        dx2 = -dx2
        dy2 = -dy2
        dx3 = -dx3
        dy3 = -dy3

    distance6 = sqrt((x4 - x2)*(x4 - x2)+(y4 - y2)*(y4 - y2))
    if distance6 <= 60:
        dx2 = -dx2
        dy2 = -dy2
        dx4 = -dx4
        dy4 = -dy4

    distance7 = sqrt((x5 - x2)*(x5 - x2)+(y5 - y2)*(y5 - y2))
    if distance7 <= 60:
        dx2 = -dx2
        dy2 = -dy2
        dx5 = -dx5
        dy5 = -dy5

    distance8 = sqrt((x4 - x3)*(x4 - x3)+(y4 - y3)*(y4 - y3))
    if distance8 <= 60:
        dx3 = -dx3
        dy3 = -dy3
        dx4 = -dx4
        dy4 = -dy4

    distance9 = sqrt((x5 - x3)*(x5 - x3)+(y5 - y3)*(y5 - y3))
    if distance9 <= 60:
        dx3 = -dx3
        dy3 = -dy3
        dx5 = -dx5
        dy5 = -dy5

    distance10 = sqrt((x5 - x4)*(x5 - x4)+(y5 - y4)*(y5 - y4))
    if distance10 <= 60:
        dx4 = -dx4
        dy4 = -dy4
        dx5 = -dx5
        dy5 = -dy5

    key = win.checkKey()