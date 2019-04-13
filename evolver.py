from p5 import random_uniform, Vector, remap, PI
from geneticMaterial import DNA
import names

class Evolver(object):

    __total_evolvers = 0
    __mutation_rate = 0.1
    __radius = 5
    __maxspeed = 5
    __maxforce = 0.5
    __clone_rate = 0.02

    def __init__(self, x, y, dna: DNA = None):
        self.pos = Vector(x,y)
        self.vel = Vector(0,-2)
        self.acc = Vector(0,0)
        self.rad = 10
        self.__name = [names.get_first_name(), names.get_last_name(), names.get_last_name()]
        self.__dna = dna
        self.__total_evolvers += 1

    def __str__(self):
        __str = f"""
        Name: {self.name}
        Position: ({self.pos.x},{self.pos.y})
        Velocity: {self.vel}
        Acceleration: {self.acc}
        DNA: {self.dna}
        """
        return __str
    
    @property
    def dna(self):
        if self.__dna == None:
            self.__dna = Evolver.generate_random_dna()
            return self.__dna
        else:
            return DNA(self.__dna).alelos

    @property
    def name(self):
        return f"{self.__name[0]} {self.__name[1]} {self.__name[2]}"

    @staticmethod
    def generate_random_dna():
        alelos = [random_uniform(-1,1) for _ in range(4)]
        dna = DNA(alelos)
        return dna
        