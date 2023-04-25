from tkinter import ttk, constants
from ui.tab_1x import Tab_1X
from ui.tab_gl import Tab_GL

class UI:
    def __init__(self, root):
        self._root = root
        self._tabs = ttk.Notebook(root)
        self._tab1 = Tab_1X(self._tabs)
        self._tab2 = Tab_GL(self._tabs)

    def start(self):
        self._tabs.pack(fill=constants.BOTH, expand=True)
        self._tabs.add(self._tab1.frame, text=self._tab1.label)
        self._tabs.add(self._tab2.frame, text=self._tab2.label)
