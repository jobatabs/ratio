"""tab_gl.py provides the g / L UI tab of the application.
"""
from tkinter import ttk, Tk, StringVar
from ui.entry_filter import RatioEntry, LabelEntry
from ui.selector import Selector


class TabGL:
    """Defines a tab for the UI that takes a Recipe in the form of grams per litre.
    """

    def __init__(self, root: Tk, coffee_var: StringVar,
                 water_var: StringVar, recipe_var: StringVar):
        """Constructs a TabGL object.

        Args:
            root (Tk): A Tk object to attach to.
            coffee_var (StringVar): Amount of coffee, populated into the coffee entry field.
            water_var (StringVar): Amount of water, populated into the water entry field.
            recipe_var (StringVar): The recipe, populated into the recipe entry field.
        """
        self._root = root
        self._frame = None
        self._coffee_var = coffee_var
        self._water_var = water_var
        self._recipe_var = recipe_var
        self.label = "g/L"
        self._initialize()

    @property
    def frame(self):
        """Getter for the tab's Tk frame.
        """
        return self._frame

    def _initialize(self):
        """Configures the tab for display.
        """
        self._frame = ttk.Frame(master=self._root)

        self._ratio_entry = RatioEntry(
            master=self._frame, width=6, value=self._recipe_var)

        self._ratio_explainer = ttk.Label(master=self._frame, text="g / 1L")

        self._coffee_entry = LabelEntry(self._frame, self._coffee_var, "Coffee")
        self._water_entry = LabelEntry(self._frame, self._water_var, "Water")
        self._coffee_selector = Selector(self._frame, ("g", "spoons"))
        self._water_selector = Selector(self._frame, ("g", "ml"))

        self._ratio_entry.grid(row=0, column=1)
        self._ratio_explainer.grid(row=0, column=2)
        self._coffee_entry.display(row=1, column=0)
        self._water_entry.display(row=1, column=2)
        self._coffee_selector.display(row=1, column=1)
        self._water_selector.display(row=1, column=3)

        self._frame.grid_rowconfigure(0, weight=1)
        self._frame.grid_columnconfigure(0, weight=1)
        self._frame.grid_rowconfigure(1, weight=1)
        self._frame.grid_columnconfigure(1, weight=1)
        self._frame.grid_columnconfigure(2, weight=1)
        self._frame.grid_columnconfigure(3, weight=1)
