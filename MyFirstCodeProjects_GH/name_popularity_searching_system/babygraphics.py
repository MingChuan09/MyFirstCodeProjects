"""
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This program can show the curves of the babyname's ranking trend.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE   # define the edge of the chart
    x_coordinate += int(year_index * ((width-GRAPH_MARGIN_SIZE*2)/len(YEARS)))    # 讓x依照年代個數區隔
    return x_coordinate


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    edge = GRAPH_MARGIN_SIZE
    canvas.create_line(edge, edge, CANVAS_WIDTH-edge, edge)   # the top (y) of the chart
    canvas.create_line(edge, CANVAS_HEIGHT-edge, CANVAS_WIDTH - edge, CANVAS_HEIGHT-edge)  # the bottom (y) of the chart

    for i in range(len(YEARS)):
        x = get_x_coordinate(CANVAS_WIDTH, year_index=i)
        canvas.create_line(x, 0, x, CANVAS_HEIGHT)     # 劃出每個年代(x)界線
        canvas.create_text((x+TEXT_DX), CANVAS_HEIGHT-edge, text=YEARS[i], anchor=tkinter.NW)  # 每個年代底標(x座標代表之年代)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    #################################
    for i in range(len(lookup_names)):
        name = lookup_names[i]
        info = name_data[name]       # get each name's info ,it is a dict {year:rank,.....}
        x_list = []                         # to remember each x for drawing the curve
        y_list = []                         # to remember each y for drawing the curve
        color = COLORS[i % len(COLORS)]     # to change the color of curve and it doesn't be affected by the len(COLORS)

        for j in range(len(YEARS)):
            year_n = str(YEARS[j])     # year_n -> int, 為了確認每一個年代year_n,是否有在info裡
            x = get_x_coordinate(CANVAS_WIDTH, year_index=j)   # get x
            x_list.append(x)

            if year_n in info:
                rank_y = info[year_n]
                canvas.create_text(x+TEXT_DX, int(rank_y)/1000 * (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)+GRAPH_MARGIN_SIZE,
                                   text=(name, rank_y), anchor=tkinter.SW, fill=color)
                y = int(rank_y)/1000 * (CANVAS_HEIGHT-GRAPH_MARGIN_SIZE*2)+GRAPH_MARGIN_SIZE
                y_list.append(y)
            else:
                rank_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                canvas.create_text(x + TEXT_DX, rank_y, text=(name, '*'), anchor=tkinter.SW, fill=color)   # get y
                y = rank_y
                y_list.append(y)

            canvas.create_line(x_list[j-1], y_list[j-1], x, y, fill=color, width=LINE_WIDTH)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
