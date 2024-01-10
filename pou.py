class PouGame:
    def __init__(self):
        self.happiness = 100
        self.hunger = 0
        self.energy = 100

    def play(self):
        self.happiness += 10
        self.energy -= 5

    def eat(self):
        self.hunger -= 15
        self.happiness += 5

    def sleep(self):
        self.energy += 20
        self.happiness += 10

    def exit_game(self):
        print("¡Gracias por jugar a Pou Play, Eat, Sleep, Exit!")
        exit()

    def check_status(self):
        print(f"Estado actual de Pou:\nHappiness: {self.happiness}\nHunger: {self.hunger}\nEnergy: {self.energy}")

    def time_passes(self):
       self.happiness -= 5
       self.energy -= 10
    pass

pou_game = PouGame()

while True:
    pou_game.check_status()
    pou_game.time_passes()

    action = input("Selecciona una acción: play, eat, sleep, exit\n")

    if action == '1':
        pou_game.play()
    elif action == '2':
        pou_game.eat()
    elif action == '3':
        pou_game.sleep()
    elif action == '0':
        pou_game.exit_game()
    else:
        print("Acción no válida. Por favor, selecciona una acción válida.")
