class Flight:
    def fly(self):
        print('fly')
class Airplane(Flight):
    def fly(self):
        print('Airplane flies.')
class Bird(Flight):
    def fly(self):
        print('Bird flies.')
class PaperAirplane(Flight):
    def fly(self):
        print('Paper airplane flies.')
flight=Flight()
air=Airplane()
bird=Bird()
paper=PaperAirplane()

flight.fly()
flight=air
flight.fly()
flight=bird
flight.fly()
flight=paper
flight.fly()