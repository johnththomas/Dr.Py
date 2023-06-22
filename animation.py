import turtle
def animation_dr_py():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.bgcolor("black")

    # Create a turtle object
    dr_py = turtle.Turtle()
    dr_py.color("green")
    dr_py.shape("turtle")
    dr_py.pensize(3)

    # Define the drawing functions for Dr. Py
    def draw_head():
        dr_py.penup()
        dr_py.goto(0, -150)  # Adjust the starting position of the head
        dr_py.pendown()
        dr_py.color("cyan")
        dr_py.fillcolor("")
        dr_py.begin_fill()
        dr_py.circle(170)  # Increase the radius of the head
        dr_py.end_fill()

    def draw_eyes():
        dr_py.penup()
        dr_py.goto(-60, 40)  # Adjust the position of the eyes
        dr_py.pendown()
        dr_py.color("cyan")
        dr_py.fillcolor("")
        dr_py.begin_fill()
        dr_py.circle(35)  # Increase the radius of the eyes
        dr_py.end_fill()

        dr_py.penup()
        dr_py.goto(60, 40)  # Adjust the position of the eyes
        dr_py.pendown()
        dr_py.color("cyan")
        dr_py.fillcolor("cyan")
        dr_py.begin_fill()
        dr_py.circle(35)  # Increase the radius of the eyes
        dr_py.end_fill()
    
    def draw_smile():
        dr_py.penup()
        dr_py.goto(-70, -60)  # Adjust the position of the smile
        dr_py.pendown()
        dr_py.color("cyan")
        dr_py.width(8)  # Increase the width of the smile
        dr_py.setheading(-60)
        dr_py.circle(80, 120)  # Increase the radius of the smile

    def draw_name():
        dr_py.penup()
        dr_py.goto(0, -250)  # Adjust the position of the name
        dr_py.pendown()
        dr_py.color("cyan")
        dr_py.write("Dr. Py", align="center", font=("Arial", 60, "bold"))  # Increase the font size of the name

    # Draw Dr. Py
    draw_name()
    draw_head()
    draw_eyes()  
    draw_smile()
    

    # Hide the turtle object
    dr_py.hideturtle()
    
    #turtle.done() # it needed be closed by user
    turtle.bye() # it will be closed automatically
    
animation_dr_py()
