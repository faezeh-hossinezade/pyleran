"""
Example "Arcade" library code.

Showing how to do nested loops.

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.nested_loops_bottom_left_triangle
"""

# Library imports
import arcade

COLUMN_SPACING = 20
ROW_SPACING = 25
LEFT_MARGIN = 110
BOTTOM_MARGIN = 100

# Open the window and set the background
arcade.open_window(400, 400, "Complex Loops - Bottom Left Triangle")

arcade.set_background_color(arcade.color.WHITE)

# Start the render process. This must be done before any drawing commands.
arcade.start_render()
is_blue = True
# Loop for each row
for row in range(10):
    # Loop for each column
    # Change the number of columns depending on the row we are in

    for column in range(10 - row):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        # Draw the item
        if column == 9:
            if is_blue:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            continue
        if is_blue:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            is_blue = False
        else:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            is_blue = True

for row in range(10):
    # Loop for each column
    # Change the number of columns depending on the row we are in

    for column in range(0,10):
        # Calculate our location
        x = column * COLUMN_SPACING + LEFT_MARGIN
        y = row * ROW_SPACING + BOTTOM_MARGIN

        # Draw the item
        if column == 9:
            if is_blue:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            else:
                arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            continue
        if is_blue:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.BLUE, tilt_angle=45)
            is_blue = False
        else:
            arcade.draw_rectangle_filled(x, y, 12, 12, arcade.color.RED, tilt_angle=45)
            is_blue = True
# Finish the render.
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()