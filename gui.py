import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from predictions import PredictionGenerator

class CookieClickerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Cookie Clicker")

        self.clicks = 0
        self.prediction_limit = 3
        self.predictions_made = 0

        self.prediction_generator = PredictionGenerator()

        self.cookie_image = self.load_cookie_image()
        self.cookie_button = tk.Button(master, image=self.cookie_image, command=self.on_cookie_click)
        self.cookie_button.pack(pady=20)

        self.clicks_label = tk.Label(master, text=f"Нажатий: {self.clicks} / 10")
        self.clicks_label.pack(pady=20)

        self.prediction_label = tk.Label(master, text="")
        self.prediction_label.pack(pady=20)

    def load_cookie_image(self):
        image = Image.open("resources/cookie.jpg")
        image = image.resize((350, 350), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def on_cookie_click(self):
        if self.clicks < 10:
            self.clicks += 1
            self.clicks_label.config(text=f"Нажатий: {self.clicks} / 10")

            if self.clicks % 10 == 0 and self.predictions_made < self.prediction_limit:
                prediction = self.prediction_generator.get_prediction()
                self.prediction_label.config(text=prediction)
                self.predictions_made += 1
        else:
            messagebox.showinfo("Информация", "Вы уже сделали 10 нажиманий!")