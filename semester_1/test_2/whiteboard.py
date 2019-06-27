from graphics import GraphWin, Circle, Point, Line, Rectangle, Text


def write_letters(win):
    '''
    Draw the eight letters on the whiteboard after each mouse click.
    '''
    eight_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

    # Write the eight letters on the whiteboard
    whiteboard_letters = Text(Point(225, 100), '')
    whiteboard_letters.setTextColor('blue')
    whiteboard_letters.setSize(30)
    whiteboard_letters.draw(win)

    # Get mouse click to write each of the eight letters
    for i in range(len(eight_letters)):
        win.getMouse()

        letter_to_write = eight_letters[i]
        whiteboard_letters.setText(letter_to_write.center(150))


def draw_classroom():
    '''
    Draw the teacher, whiteboard, and marker pen.
    '''
    win = GraphWin("Stick figure", 300, 200)
    head = Circle(Point(100, 60), 20)
    head.draw(win)
    body = Line(Point(100, 80), Point(100, 120))
    body.draw(win)
    arms = Line(Point(70, 90), Point(130, 90))
    arms.draw(win)
    leg1 = Line(Point(100, 120), Point(80, 170))
    leg1.draw(win)
    leg2 = Line(Point(100, 120), Point(120, 170))
    leg2.draw(win)

    # Draw the Whiteboard
    whiteboard = Rectangle(Point(140, 50), Point(290, 150))
    whiteboard.setFill('white')
    whiteboard.draw(win)

    # Draw the blue marker pen base
    marker_pen = Rectangle(Point(120, 80), Point(128, 100))
    marker_pen.setFill('blue')
    marker_pen.draw(win)

    # Draw the blue marker pen tip
    marker_pen_tip = Rectangle(Point(122, 72), Point(126, 80))
    marker_pen_tip.setFill('blue')
    marker_pen_tip.draw(win)

    write_letters(win)
    marker_pen_tip.setFill('white')


draw_classroom()
