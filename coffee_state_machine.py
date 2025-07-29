# State Machine for Coffee machine 
#States:
#Idle
#Heating
#Brewing
#Complete

#coffee_state_machine.py

from enum import Enum, auto

class CoffeeState(Enum):
    IDLE = auto()
    HEATING = auto()
    BREWING = auto()
    COMPLETE = auto()

class CoffeeMachineFSM:

    def __init__(self):
        self.state = CoffeeState.IDLE

    def start_brew(self, drink):
        if self.state == CoffeeState.IDLE :
            self.state = CoffeeState.HEATING
            return f"Starting {drink}: Heating..."
        return f"Cannot start. Current state:{self.state.name}"
    

    def brew(self, drink):
        if self.state == CoffeeState.HEATING:
            self.state = CoffeeState.BREWING
            return f"{drink} is Brewing. . ."
        return f"Cannot brew. Current state: {self.state.name}"

    def complete(self, drink):
        if self.state == CoffeeState.BREWING:
            self.state = CoffeeState.COMPLETE
            return f"{drink} is Ready!"
        return f"Cannot complete. Current state: {self.state.name}"

    def reset(self):
        if self.state == CoffeeState.COMPLETE:
            self.state = CoffeeState.IDLE
            return "Click to select drink!"
        return f"Cannot reset. Current state: {self.state.name}"

    def get_state(self):
        return self.state.name