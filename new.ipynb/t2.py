from turtle import *
pensize(2)
speed("fastest")
bgcolor('green')
pencolor('white')

for i in range(6):
    lt(60)
    fd(169)
    fillcolor('red')
    begin_fill()
    for i in range(6):
        lt(60)
        fd(150)
        
    end_fill()    
hideturtle()
mainloop()        