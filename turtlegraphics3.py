import time
start=time.time()
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
turtle.title("Turtle animation!")
count=0
aborted=False

def do_pause(a,b):
    global count
    count = count+1
    if count<3:
        print("Pausing for 2 secs.",count,"click(s) detected.")
        time.sleep(2)
    else:
        print(str(count),"clicks are detected. Aborting!")
        global aborted
        aborted=True

for x in range(120):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
    turtle.onscreenclick(do_pause)
    if aborted:
        break

print(str(round(time.time()-start,1)),"secs have elapsed.")
turtle.exitonclick()