# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s): Stanislav Yanakiev & Gerardo Garcia
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
    canvas (tkinter.Canvas):
    status (tkinter.Label):
    attempts (int):
    points (int):
    delay (int):
    player_color (string):

    """

    # Add your class variables if needed here - square size, etc...)
    TILE_SIZE = 125

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        # Create the restart button widget
        # the command was being called on initialization so
        # StackOverlfow answer said to include lambda
        restart_button = tkinter.Button(parent, text='Restart', width=50,
                                        command=self.restart)
        restart_button.grid()
        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=500, height=500)
        # Create tile widgets
        for row in range(0, 500, self.TILE_SIZE):
            for col in range(0, 500, self.TILE_SIZE):
                self.canvas.create_rectangle(row, col, row + self.TILE_SIZE,
                                             col + self.TILE_SIZE,
                                             fill="yellow")
        # bind the tiles to an event
        self.canvas.bind("<Button-1>", self.play)
        self.canvas.grid()

        # Create a label widget for the score and end of game messages
        self.status = tkinter.Label(parent, text='Score: 100')
        self.status.grid()
        self.attempts = 0
        self.points = 100
        # Create any additional instance variable you need for the game
        self.delay = delay
        self.player_color = player_color

        # get the list of images
        images_file = [file for file in os.listdir(folder) if
                       os.path.splitext(file)[1] == '.gif']
        # save the images
        images = [tkinter.PhotoImage(file=folder + "/" + images_file[num])
                  for num in range(len(images_file))]

        self.combinedImages = images + images

        # shuffle images
        self.restart()

    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        self.disappear()
        for img in self.canvas.find_all()[0:16]:
            self.canvas.itemconfigure(img, fill='yellow', tag='',
                                      outline='black')
        self.attempts = 0
        self.points = 100
        self.status.configure(text='Score: 100')

        random.shuffle(self.combinedImages)

    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        tile = self.canvas.find_withtag(tkinter.CURRENT)[0]
        if tile not in self.canvas.find_withtag('matched') and \
                len(self.canvas.find_withtag('selected')) < 2:
            # Tile selected is not already matched
            if len(self.canvas.find_withtag('selected')) == 0:
                # First tile
                # Tag it
                self.canvas.itemconfigure(tile, tag='selected')
                # Draw it
                self.first_image = self.appear(tile, event)
            else:
                # Second tile
                first_tile = self.canvas.find_withtag('selected')[0]
                self.canvas.itemconfigure(tile, tag='selected')
                second_image = self.appear(tile, event)
                if self.first_image == second_image:
                    # If images are matched
                    # Erase images after delay
                    self.canvas.after(self.delay, self.disappear)
                    # Color second tile as match after delay
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure
                                      (tile, fill=self.player_color,
                                       outline=self.player_color))
                    # Color first tile as match after delay
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure
                                      (first_tile, fill=self.player_color,
                                       outline=self.player_color))
                    # Mark second tile as match after delay
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure(
                                            tile, tag='matched'))
                    # Mark first tile as match after delay
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure(
                                            first_tile, tag='matched'))

                else:
                    # No match is found
                    # Erase images after delay
                    self.canvas.after(self.delay, self.disappear)
                    # remove tag from first tile
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure(
                                        first_tile, tag=''))
                    self.canvas.after(self.delay,
                                      lambda: self.canvas.itemconfigure(
                                        tile, tag=''))
                self.score()
                self.canvas.after(self.delay, self.finished)

    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.

    def disappear(self):
        """Remove's image from the CanvasCall appear to have
        the image reappear after a delay"""

        self.canvas.delete('image')

    def appear(self, tile, event):
        """Add Sammy's image to CanvasCall disappear
        to have the image disappear after a delay"""
        self.canvas.create_image(event.x // self.TILE_SIZE
                                 * self.TILE_SIZE + 62.5, event.y //
                                 self.TILE_SIZE * self.TILE_SIZE + 62.5,
                                 image=self.combinedImages[tile - 1],
                                 tag="image", state='disabled')
        return self.combinedImages[tile - 1]

    def score(self):
        self.attempts += 1
        if self.attempts > 13:
            self.points -= 10
            self.status.configure(text=f'Score: {self.points}')

    def finished(self):
        if len(self.canvas.find_withtag('matched')) == 16:
            self.status.configure(text=f'Game over!\nScore: '
                                       f'{self.points}\nNumber of tries: '
                                       f'{self.attempts}')

# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.


def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the color (string), image_folder
    (file object) and the fast option (integer).
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What color would you like for matched tiles?',
                        choices=['blue', 'green', 'magenta'])

    parser.add_argument('image_folder',
                        help='File folder containing images to be used',
                        type=dir_validate
                        )

    parser.add_argument('-f', '--fast',
                        help='Tile unveiling will be faster',
                        action='store_const',
                        const=1000,
                        default=3000
                        )

    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast
    return color, image_folder, fast


def dir_validate(path):
    if os.path.isdir(path):
        num_of_images = [file for file in os.listdir(path) if
                         os.path.splitext(file)[1] == '.gif']
        if len(num_of_images) >= 8:
            return path
        else:
            raise argparse.ArgumentTypeError(
                f"argument {path} must contain at least 8 gif images")
    else:
        raise argparse.ArgumentTypeError(
            f"argument {path} is not a valid folder")


def main():
    # Retrieve and validate the command line arguments using argparse
    color, image_folder, fast = get_arguments()
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a MatchGame object with the correct arguments
    game = MatchGame(root, color, image_folder, fast)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
