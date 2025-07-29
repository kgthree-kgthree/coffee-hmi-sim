#PyQt

import tkinter as tk
from tkinter import messagebox
from coffee_state_machine import  CoffeeMachineFSM
from datetime import datetime

cm = CoffeeMachineFSM()

class CoffeeApp():

    def __init__(self, root):
        self.root = root
        self.root.title("Coffee HMI")
        self.root.geometry("500x250")

        self.fsm = CoffeeMachineFSM()
        self.current_drink = None

        self.create_widgets()
        
    def create_widgets(self):
        tk.Label(self.root, text=f"☕ Start your day with coffee ☕", font=("Helvetica",16)).pack(pady=10)
        
        self.status_label = tk.Label(self.root, text=f"Status:{self.fsm.get_state()}", font = ("Helvetica", 12), fg = "green")
        self.status_label.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        for drink in ["Espresso", "Latte", "Cappuccino"]:
            tk.Button(button_frame, text=drink, width=12,
                      command=lambda d=drink: self.start_brew(d)).pack(side=tk.LEFT, padx=5)

        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=10)

    def update_status(self, drink, color="Black"):
        self.status_label.config(text=f"Status: {drink}", fg=color)


    
    def start_brew(self, drink):
        if self.fsm.get_state() != "IDLE":
            messagebox.showwarning("Busy", f"Machine is {self.fsm.get_state().lower()}")
            return

        self.current_drink = drink
        msg = self.fsm.start_brew(drink)
        self.update_status(msg, "orange")
        self.root.after(2000, self.brew)
    

    def brew(self):
        msg = self.fsm.brew(self.current_drink)
        self.update_status(msg, "brown")
        self.root.after(3000, self.complete)

    def complete(self):
        msg = self.fsm.complete(self.current_drink)
        self.update_status(msg, "green")
        self.log_brew(self.current_drink)
        self.root.after(2000, self.reset)

    def reset(self):
        msg = self.fsm.reset()
        self.update_status(msg, "green")

    def log_brew(self, drink):
        with open("brew_log.txt", "a") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"[{timestamp}] Brewed: {drink}\n")


        

if __name__ == "__main__":
    root = tk.Tk()
    app = CoffeeApp(root)
    root.mainloop()