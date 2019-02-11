from display import *
from draw import *
import math

screen = new_screen()
color1 = [ 0, 255, 0 ]
color2 = [255,0,0]
color3 = [0,0,255]
color4 = [0,255,255]

for xcor in range(0, 501, 10):
    ycor =  math.floor(xcor/2)
    draw_line(xcor, 500, 0, ycor, screen, color1)
for ycor in range(0, 501, 10):
    xcor = math.floor(ycor/2)
    draw_line(xcor, 500, 0, ycor, screen, color2)
draw_line(250, 250, 250, 500, screen, color3)
draw_line(250, 250, 500, 250, screen, color3)
draw_line(250, 250, 500, 500, screen, color3)
draw_line(250, 250, 500, 0, screen, color3)
draw_line(250, 250, 500, 125, screen, color3)
draw_line(250, 250, 375, 0, screen, color3)
draw_line(250, 250, 375, 500, screen, color3)
draw_line(250, 250, 500, 375, screen, color3)
draw_line(250, 250, 250, 0, screen, color3)

'''
eh=0
oh=True

for x in range(0, 499):
    for y in range(0, 499):
        d = int(math.sqrt( (250-x)**2 + (250 - y)**2))
        if d < 203 and d > 198:
            if eh%30==0:
                oh=not oh
            if oh:
                color=color3
            else:
                color=color4
            eh+=1
            draw_line(250+x, 250+y, x, y, screen, color)
'''

save_extension(screen, 'img.png')
print("img.png")
