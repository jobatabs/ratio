from tkinter import ttk, constants, StringVar

class Selector:
    def __init__(self, root, units: tuple):
        self._root = root
        self._frame = None
        self._selection = StringVar()
        self._units = units
        self._initialize()

    def display(self, **options):
        self._frame.grid(**options)

    @property
    def selection(self):
        return self._selection

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        for unit in self._units:
            ttk.Radiobutton(master=self._frame, var=self._selection, value=unit, text=unit)\
                .grid(sticky=constants.W)
        self._selection.set(self._units[0])
