import tkinter as tk
from gui import CookieClickerApp

def main():
    root = tk.Tk()
    app = CookieClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()