# coffee_hmi_simulator/main.py
# Simulates an HMI interface for a professional coffee machine

import tkinter as tk
from tkinter import messagebox

class CoffeeHMI:
    def __init__(self, master):
        self.master = master
        master.title("Coffee HMI Simulator")
        master.geometry("400x350")

        self.status = tk.StringVar()
        self.status.set("Idle")

        # Title
        tk.Label(master, text="Coffee Machine Control", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Coffee selection buttons
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        self.create_button(button_frame, "Espresso", self.make_espresso)
        self.create_button(button_frame, "Latte", self.make_latte)
        self.create_button(button_frame, "Cappuccino", self.make_cappuccino)

        # Status
        tk.Label(master, text="Status:").pack(pady=5)
        self.status_label = tk.Label(master, textvariable=self.status, font=("Helvetica", 12), fg="green")
        self.status_label.pack()

        # Settings (static)
        tk.Label(master, text="Settings:").pack(pady=10)
        self.settings_text = tk.Label(master, text="Temp: 92°C | Cup Size: Medium")
        self.settings_text.pack()

        # Exit button
        tk.Button(master, text="Exit", command=master.quit).pack(pady=20)

    def create_button(self, frame, text, command):
        tk.Button(frame, text=text, width=12, command=command).pack(side=tk.LEFT, padx=5)

    def make_espresso(self):
        self.brew("Espresso")

    def make_latte(self):
        self.brew("Latte")

    def make_cappuccino(self):
        self.brew("Cappuccino")

    def brew(self, drink):
        self.status.set(f"Brewing {drink}...")
        self.status_label.config(fg="orange")
        self.master.after(3000, lambda: self.finish_brew(drink))
        self.log_brew(drink)

    def finish_brew(self, drink):
        self.status.set(f"{drink} ready!")
        self.status_label.config(fg="green")

    def log_brew(self, drink):
        with open("brew_log.txt", "a") as file:
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] Brewed: {drink}\n")


if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeHMI(root)
    root.mainloop()
