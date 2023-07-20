In this coding experinment, I am working with the turtle module. Originally, the app was created as a way for kids to use python concepts for use to draw objects or shapes. It is now used by all python developers. There is also another app being used, which is known as Tkinter. 

A little bit about Tkinter is that its module enables the ability to turn a coding appratus or project into a full fledged graphical unit interface (GUI). 

The purpose of this experiment, is to learn about Turtle and apply its knowledge. The core of this experiment is to take simple shapes and overlap them, and use the grid as an indicator to move the shapes. Much like css, this is a graphical intensive module that draws shapes. With the help of Tkinter, the shapes are visible on a window.

The turtle module starts at the gridline of (0,0). The gridline is based on the (x,y) coordinates in a graph. 

            Turtle starts at (x,y) ---> (0,0).

The syntax calls the turtle class and its methods or functions from its module.
            import Turtle

The function is written in its following format:
            turtle.<function>(<parameters>)

Within the turtle class can use the following methods to be customizable. The most common use are the follwoing:

            turtle.<function>(<parameters>)
                  .color("<color>")
                  .penup()
                  .pendown()
                  .goto(x,y)
                  .exitonclick()

In addition to goto(), there are other methods that use the (x,y) format in its arguments. They are the following:

            turtle.forward()
                  .backward()

Other methods use the geometric bearings allow the turtle indicator (arrow that is analogous to the turtle shape), to create the lines for the shape. Those methods are:
            turtle.right(<degree>)
                  .left(<degree>)


The exitonclick() is used at the end of the code in order to end the process of the building of the shape. In its default mode, the speed of the demonstration of the output shapes is at the speed of 0, which is set to be the fastest. To contorl this, set the mehtod to speed():

            turtle.speed("see below for the speed setting")
            speed ----> 0: Fastest (default; this is automatc, when not coding the method.)

                        1,2: slowest
                        3-5: slow
                        6:9: Normal (The closer to the fast setting, the faster the build demonstration gets.)
                        10:  Fast

Other methods that are used. are the follwoing:

            pencolor: turtle.pencolor(<color>)
            pensize:        .(<width>)

The code for overlap.py, utilizes functions, that create the shape. The most simplest shape is the circle, which uses the size as an argument. Othr shapes such as a square or a triangle use for loops to code ewual distances of lines in their shape that give the shape their characteristics. Each for loop is using the range() to take in the number of size, graphical coordinates and its angular degree in its direction to form the shape. 

The square shape is a simpler use of the for loop, since it is four sided and 90 degrees in angle on each side. Thus the for loop with the range(4) will create a square. For a triangle. it is not so simple, since two sides out of three sides are equal and the third line is a seperate code. Whereas other shapes can only be determned via the way the shape looks like, its repetitive nature and its unequalness of lines, where they are not equal. 

All codes for their respective shapes are enclosed as a block of code in a function. For example, 

            def round(x):
                turtle.color("blue")
                turtle.circle(x)

            round(200)
