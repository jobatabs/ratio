from tkinter import ttk, StringVar, Tk


class RatioEntry(ttk.Entry):
    def __init__(self, value, *args, **kwargs):
        ttk.Entry.__init__(self, textvariable=value, *args, **kwargs)

        vcmd = (self.register(self.on_validate), "%P")
        self.configure(validate="key", validatecommand=vcmd)

    def disallow(self):
        self.bell()

    def on_validate(self, new_value):
        try:
            if new_value.strip() == "":
                return True
            value = int(new_value)
            if value < 1 or value > 100:
                self.disallow()
                return False
        except ValueError:
            self.disallow()
            return False


class LabelEntry:

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
        self._frame.grid(**options)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._field = ttk.Entry(
            master=self._frame, width=6, textvariable=self.__value)
        self._text = ttk.Label(master=self._frame, text=self.__label)
        self._field.grid()
        self._text.grid()
