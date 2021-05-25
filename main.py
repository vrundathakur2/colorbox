from turtle import Turtle, Screen

COLORS = ["Black", "Blue", "Red", "Green"]
GRID = 5
STAMP_UNIT = 20

def main():
    length = int(input("Enter a desired length (from 1-150): "))
    Drawing = True

    while Drawing:
        print("What color would you like to draw?")
        for i, color in enumerate(COLORS, start=1):
            print("    Enter {} for {}".format(i, color))
        choice = int(input("          Your choice? "))

        if 1 <= choice <= len(COLORS):
            grid(-length * GRID // 2, -length * GRID // 2, length, COLORS[choice - 1])
            Drawing = False
        else:
            print("ERROR: only enter 1-{}.".format(len(COLORS)))
def grid(x, y, width, color):
    tortoise = Turtle('square', visible=False)
    tortoise.shapesize(width / STAMP_UNIT)
    tortoise.color(color)
     tortoise.penup()

    for dy in range(0, GRID):
        tortoise.goto(x, y + width * dy)

        for dx in range(dy % 2, GRID, 2):
            tortoise.setx(x + width * dx)

            tortoise.stamp()

screen = Screen()

main()

screen.exitonclick()
