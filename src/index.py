"""Main executable file for the application.
"""

from tkinter import Tk
from ui.ui import UI


def main():
    """Main function that starts the application.
    """
    window = Tk()
    window.title("ratio")
    window.geometry("300x150")
    window.resizable(False, False)

    app_ui = UI(window)
    app_ui.start()

    window.mainloop()


if __name__ == "__main__":
    main()
