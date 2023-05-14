"""entry_filter.py provides all of the application's entry fields,
with filtering capability to be implemented.
"""
from tkinter import ttk, StringVar, Tk
from decimal import Decimal, InvalidOperation


class RatioEntry(ttk.Entry):
    """Defines an entry field that validates input to be of recipe form.
    """

    def __init__(self, value: StringVar, *args, **kwargs):
        """Runs super's init and registers validation command.

        Args:
            value (StringVar): StringVar to link to.
        """
        ttk.Entry.__init__(self, textvariable=value, *args, **kwargs)

        vcmd = (self.register(self.on_validate), "%P")
        self.configure(validate="key", validatecommand=vcmd)

    def disallow(self):
        """Rings the bell of the display if validation fails.
        """
        self.bell()

    def on_validate(self, new_value: str) -> bool:
        """Validates the input if it is an integer between 1 and 200,
        and runs disallow() if input is not valid.

        Args:
            new_value (str): Input.

        Returns:
            bool: True if the input is valid, False if the input is not valid.
        """
        try:
            if new_value.strip() == "":
                return True
            value = Decimal(new_value)
            if value < 1 or value > 200:
                self.disallow()
                return False
            return True
        except (InvalidOperation, ValueError):
            self.disallow()
            return False


class LabelEntry:
    """Defines an entry field along with a label.
    """

    def __init__(self, root: Tk, value: StringVar, label: str):
        """Constructs a LabelEntry object.

        Args:
            root (Tk): A Tk object to attach to.
            value (StringVar): A StringVar to attach the entry field to.
            label (str): The label of the entry field.
        """
        self._root = root
        self._frame = None
        self.__label = label
        self.__value = value
        self._initialize()

    def display(self, **options):
        """Displays the entry field and label in a grid.
        """
        self._frame.grid(**options)

    def _initialize(self):
        """Creates a frame containing the entry field along with a label.
        """
        self._frame = ttk.Frame(master=self._root)
        self._field = ttk.Entry(
            master=self._frame, width=6, textvariable=self.__value)
        self._text = ttk.Label(master=self._frame, text=self.__label)
        self._field.grid()
        self._text.grid()
