# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s):
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} image_folder
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            Fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):
    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    Please list ALL the instance variables here
    """

    # Add your class variables if needed here - square size, etc...)

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                        command=self.restart)
        restart_button.grid()
        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=500, height=500)
        self.canvas.grid()
        # Create a label widget for the score and end of game messages
        # Create any additional instance variable you need for the game
        # take out the pass statement and enter your code

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        pass  # take out the pass statement and enter your code

    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        pass  # take out the pass statement and enter your code

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.


# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='this is the color to be used for the '
                             'matched tiles',
                        choices=['blue', 'green', 'magenta'])
    parser.add_argument('image_folder',
                        help='this is the name of a folder/directory that'
                             ' contains the 8 images to be used in the game.',
                        type=directory_type,
                        nargs='?')
    parser.add_argument('-f', '--fast',
                        help='Faster game-play?',
                        action='store_const',
                        cost=1000,
                        default=3000)

    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast
    return color, image_folder, fast


def directory_type(entered_directory):
    try:
        dir_list = os.listdir(entered_directory)
    except FileNotFoundError:
        raise argparse.ArgumentError()
    else:
        gifs = [file for file in dir_list if os.path.splitext(file)[1] ==
                '.gif']
        if len(gifs) != 8:
            raise argparse.ArgumentError()
        return os.path.dirname(entered_directory)


def main():
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop
    color, image_folder, fast = get_arguments()
    root = tkinter.Tk
    match_app = MatchGame(root, color, image_folder, fast)
    root.mainloop()


if __name__ == '__main__':
    main()
