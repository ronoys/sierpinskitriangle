import turtle
window = turtle.Screen()
q = turtle.Turtle()
size = int(input("Enter the size of the triangle in pixels "))
loop = int(input("Enter the number of levels of the fractal to be created "))

def triangle(x,y):

    if y != 0:
        triangle(x/2,y-1)
        q.forward(x/2)
        triangle(x/2,y-1)
        q.backward(x/2)
        q.left(60)
        q.forward(x/2)
        q.right(60)
        triangle(x/2,y-1)
        q.left(60)
        q.backward(x/2)
        q.right(60)
        
    else:
        
        for i in range(0,3):
            q.forward(x)
            q.left(120)
  
            
triangle(size,loop)
