from tkinter import Tk, ttk, constants, Menu, filedialog, StringVar
from decimal import Decimal
from ui.tab_1x import Tab1X
from ui.tab_gl import TabGL
from file.file import write_recipe, read_recipe
from units.coffee import Coffee
from units.water import Water
from units.recipe import Recipe


class UI:
    def __init__(self, root: Tk):
        self._root = root

        self._coffee_var = StringVar()
        self._water_var = StringVar()
        self._recipe_var = StringVar()

        self._coffee_var.set("15")
        self._water_var.set("250")
        self._recipe_var.set("60")

        self._tabs = ttk.Notebook(root)
        self._tab1 = Tab1X(self._tabs, self._coffee_var,
                           self._water_var, self._recipe_var)
        self._tab2 = TabGL(self._tabs, self._coffee_var,
                           self._water_var, self._recipe_var)

        self._menubar = Menu(self._root)
        self._root.config(menu=self._menubar)
        self._file_menu = Menu(self._menubar)

    def start(self):
        self._file_menu.add_command(
            label="Save as...", command=self._save_recipe)
        self._file_menu.add_command(label="Open...", command=self._open_recipe)
        self._file_menu.add_command(label="Exit", command=self._root.destroy)
        self._menubar.add_cascade(
            label="File", menu=self._file_menu, underline=0)
        self._tabs.pack(fill=constants.BOTH, expand=True)
        self._tabs.add(self._tab1.frame, text=self._tab1.label)
        self._tabs.add(self._tab2.frame, text=self._tab2.label)

    def _save_recipe(self):
        file = filedialog.asksaveasfile(defaultextension=".ratio", filetypes=[
                                        ("Recipe files", "*.ratio")])

        coffee = Coffee(self._coffee_var.get())
        water = Water(Decimal(self._water_var.get()))
        recipe = Recipe(grams_litre=Decimal(self._recipe_var.get()))

        write_recipe(file, coffee, water, recipe)

    def _open_recipe(self):
        file = filedialog.askopenfile(multiple=False, filetypes=[
                                      ("Recipe files", "*.ratio")])

        coffee, water, recipe = read_recipe(file)

        self._coffee_var.set(str(coffee.grams))
        self._water_var.set(str(water.grams))
        self._recipe_var.set(str(recipe.grams_litre))
