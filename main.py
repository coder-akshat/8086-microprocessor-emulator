import tkinter as tk
from src.gui import EmulatorGUI

def main():
    root = tk.Tk()
    app = EmulatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
