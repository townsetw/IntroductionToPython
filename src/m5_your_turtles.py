"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and TYLER TOWNSEND.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

tyler = rg.SimpleTurtle('turtle')
tyler.pen = rg.Pen('red', 4)
tyler.speed = 100
bob = rg.SimpleTurtle('turtle')
bob.pen = rg.Pen('green', 4)
bob.speed = 100

size = 300
size2 = 100

for k in range(15):
    tyler.draw_square(size)
    bob.draw_circle(size2)

    tyler.pen_up()
    bob.pen_up()

    tyler.right(45)
    tyler.forward(10)
    tyler.left(45+k)
    bob.right(135)
    bob.forward(10)
    bob.left(135+k)
    tyler.pen_down()
    bob.pen_down()

    size = size - 20
    size2 = size2 - 5

window.close_on_mouse_click()
