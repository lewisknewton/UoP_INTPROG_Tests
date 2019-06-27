from graphics import GraphWin, Circle, Point


def main():
    draw_positioned_circles()
    draw_stacked_circles()


def draw_positioned_circles():
    '''
    Draw 15 circles on each mouse click, changing fill and outline colours depending on the X co-ordinates and placing them in the same point clicked.
    '''
    win = GraphWin("Circles", 800, 200)
    radius = 20

    for _ in range(15):
        click = win.getMouse()
        click_x = click.getX()
        circle = Circle(click, radius)

        colour_circles(click_x, circle, win)


def draw_stacked_circles():
    '''
    Draw 25 circles on each mouse click, changing fill and outline colours depending on the X co-ordinates and stacking in rows of 5.
    '''
    win = GraphWin("Circles", 800, 200)
    radius = 20
    diameter = radius * 2

    # Get centre offset
    offset = 800 // 2 - diameter * 2 - radius

    for i in range(diameter * 5, radius, -diameter):
        for j in range(radius + offset, diameter * 5 + offset, diameter):
            click = win.getMouse()
            click_x = click.getX()
            circle = Circle(Point(j, i - 20), radius)

            colour_circles(click_x, circle, win)

    click = win.getMouse()
    win.close()


def colour_circles(click_x, circle, win):
    '''
    Check co-ordinates of a mouse click to determine the fill and outline colours.
    '''
    outline_colour, fill_colour = "", ""

    if click_x < 400:
        outline_colour = "green"
        if click_x < 200:
            fill_colour = "green"
    else:
        outline_colour = "blue"
        if click_x > 600:
            fill_colour = "blue"

    circle.setOutline(outline_colour)
    circle.setFill(fill_colour)
    circle.draw(win)


main()
