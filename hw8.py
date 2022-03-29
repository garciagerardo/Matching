import tkinter
import os
import random


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
        os.chdir(folder)
        listim = os.listdir(os.curdir)
        gifs = [file for file in listim if os.path.splitext(file)[1] ==
                '.gif']
        print(list)
        image = tkinter.PhotoImage(file=gifs[0])

        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                        command=self.restart)
        restart_button.grid()
        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=500, height=500)
        self.canvas.create_rectangle(0, 0, 500, 500, fill=player_color)
        self.canvas.create_rectangle(0, 0, 124, 124, fill='yellow')
        self.canvas.create_rectangle(0, 125, 124, 249, fill='yellow')
        self.canvas.create_rectangle(0, 250, 124, 374, fill='yellow')
        self.canvas.create_rectangle(0, 375, 124, 500, fill='yellow')
        self.canvas.create_rectangle(125, 0, 249, 124, fill='yellow')
        self.canvas.create_rectangle(125, 125, 249, 249, fill='yellow')
        self.canvas.create_rectangle(125, 250, 249, 374, fill='yellow')
        self.canvas.create_rectangle(125, 375, 249, 500, fill='yellow')
        self.canvas.create_rectangle(250, 0, 374, 124, fill='yellow')
        self.canvas.create_rectangle(250, 125, 374, 249, fill='yellow')
        self.canvas.create_rectangle(250, 250, 374, 374, fill='yellow')
        self.canvas.create_rectangle(250, 375, 374, 500, fill='yellow')
        self.canvas.create_rectangle(375, 0, 500, 124, fill='yellow')
        self.canvas.create_rectangle(375, 125, 500, 249, fill='yellow')
        self.canvas.create_rectangle(375, 250, 500, 374, fill='yellow')
        self.canvas.create_rectangle(375, 375, 500, 500, fill='yellow')
        self.image_example = self.canvas.create_image(150, 150, image=image)
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


def main():
    # Retrieve and validate the command line arguments using argparse
    # Instantiate a root window
    # Instantiate a MatchGame object with the correct arguments
    # Enter the main event loop

    root = tkinter.Tk()
    match_app = MatchGame(root, 'green', 'SJSUimages', True)
    root.mainloop()


if __name__ == '__main__':
    main()