"""selector.py provides Selector, which is used for radio button selectors.
"""

from tkinter import ttk, constants, StringVar, Tk


class Selector:
    """Contains a Tkinter frame with radio buttons along with their labels.
    """

    def __init__(self, root: Tk, units: tuple[str]):
        """Creates a Tkinter frame of radio buttons along with their labels.

        Args:
            root (Tk): A Tk object to attach to.
            units (tuple[str]): A tuple of strings for the radio buttons labels.
        """
        self._root = root
        self._frame = None
        self._selection = StringVar()
        self._units = units
        self._initialize()

    def display(self, **options):
        """Displays the frame contents in a grid.
        """
        self._frame.grid(**options)

    @property
    def selection(self):
        """Getter for the selected radio button.

        Returns:
            StringVar: The selected item's content.
        """
        return self._selection

    def _initialize(self):
        """Sets the radio buttons along with their labels up into a grid.
        """
        self._frame = ttk.Frame(master=self._root)
        for unit in self._units:
            ttk.Radiobutton(master=self._frame, var=self._selection, value=unit, text=unit)\
                .grid(sticky=constants.W)
        self._selection.set(self._units[0])
