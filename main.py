# main.py
import tkinter as tk
from bot import EvonyBot

if __name__ == "__main__":
    root = tk.Tk()
    bot = EvonyBot(root)
    root.mainloop()