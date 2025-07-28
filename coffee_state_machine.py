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
        if self.state = CoffeeState.IDLE :
            self.state = HEATING
            return "Heating..."
    

    def brew(self, drink):
        self.state = CoffeeState.BREWING
        return "Brewing. . ."

    def complete(self, drink):
        self.state = CoffeeState.COMPLETE
        return "ready!"

    def reset(self):
        self.state = CoffeeState.IDLE
        return "Idle"

    def get_state(self)
        return self.state.name

        