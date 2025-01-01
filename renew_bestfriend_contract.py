import turtle

def yes_renew():
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title('Happy New Year Bestie!!')

    t = turtle.Turtle()
    t.speed(1)

    def draw_layer(x, y, color):
        t.fillcolor(color)
        t.begin_fill()
        t.pencolor("white")

        for _ in range(2):
            t.forward(x)
            t.left(90)
            t.forward(y)
            t.left(90)
        t.end_fill()

    #  base of the cake
    t.penup()
    t.goto(-125, -50)
    t.pendown()
    draw_layer(250, 100, 'Pink')

    # Draw the meddle layer
    t.penup()
    t.goto(-100, 50)
    t.pendown()
    draw_layer(200, 100, 'white')

    # Draw the top layer    
    t.penup()
    t.goto(-75, 150)
    t.pendown()
    draw_layer(150, 60, 'Pink')

    # Draw the candles
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.fillcolor("yellow")

    for i in range(3):
        t.penup()
        t.goto(-70 + i * 60, 209)
        t.pendown()
        t.begin_fill()

        for _ in range(2):
            t.forward(10)
            t.left(90)
            t.forward(30)
            t.left(90)

        t.end_fill()
        t.penup()
        t.goto(-65 + i * 60, 245)
        t.pendown()
        t.dot(10, "orange")  

    
    t.penup()
    t.goto(-190, -80)
    t.color("white")
    t.write("🎊🎊🎀 Happy New Year Bestie 🎀🎊🎊", font=("Arial", 20, "bold"))

    t.hideturtle()
    screen.mainloop()

def no_renew():
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title(' Am i not good enough? ')

    t = turtle.Turtle()
    t.speed(1)

    # draw the face
    t.penup()
    t.goto(-10, -100)
    t.pencolor("white")  
    t.fillcolor('Orange')  
    t.begin_fill()
    t.circle(180)
    t.end_fill()

    # draw the eyes
    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(50, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.penup()
    t.goto(-90, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("white")
    t.begin_fill()
    t.circle(40)
    t.end_fill()

    t.penup()
    t.goto(-90, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("black")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # the tears
    t.penup()
    t.goto(-80, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("sky blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(-20)
        t.left(90)
        t.forward(-200)
        t.left(90)
    t.end_fill()

    #tears of the other eye
    t.penup()
    t.goto(40, 100)
    t.pendown()
    t.pencolor("white")  
    t.fillcolor("sky blue")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(-200)
        t.left(90)
    t.end_fill()

    # sad mouth
    t.penup()
    t.goto(30, -40)
    t.pendown()
    t.pencolor("black") 
    t.fillcolor("black")
    t.begin_fill()
    t.left(90)
    t.circle(50, 180)
    t.end_fill()
    
    
    t.penup()
    t.goto(-190, -150)
    t.color("white")
    t.write("😭😭😭SAD SAD SAD SAD😭😭😭", font=("Arial", 20, "bold"))

    t.hideturtle()
    screen.mainloop()

def cant_decide():
    print('looser are we really not that deep?')

while True:
    print('-----------*OPTIONS*-----------')
    print('1. Renew contract :) ')
    print('2. No renewal :(')
    print('3. Cant decide')

    choice = input('Enter your choice: ')
    if choice.isdigit():
        if choice == '1':
            yes_renew()
            break
        elif choice == '2':
            no_renew()
            break
        elif choice == '3':
            cant_decide()
            break
        else:
            print('Invalid choice, try again!')
    else:
        print('Stupid ass, enter a number!!')
