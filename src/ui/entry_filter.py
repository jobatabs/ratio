from tkinter import ttk

class EntryFilter(ttk.Entry):
    pass

class RatioEntry(ttk.Entry):
    def __init__(self, *args, **kwargs):
        ttk.Entry.__init__(self, *args, **kwargs)

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

class CoffeeEntry:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def display(self, **options):
        self._frame.grid(**options)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._field = ttk.Entry(master=self._frame, width=6)
        self._text = ttk.Label(master=self._frame, text="Coffee")
        self._field.grid()
        self._text.grid()

class WaterEntry:
    def __init__(self, root):
        self._root = root
        self._frame = None
        self._initialize()

    def display(self, **options):
        self._frame.grid(**options)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        self._field = ttk.Entry(master=self._frame, width=6)
        self._text = ttk.Label(master=self._frame, text="Water")
        self._field.grid()
        self._text.grid()
