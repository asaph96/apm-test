from p5 import random_uniform
from geneticMaterial import DNA

class Evolver(object):

    __total_evolvers = 0

    def __init__(self, x, y, r, dna: DNA = None):
        self.x = x
        self.y = y
        self.r = r
        self.__dna = dna
        self.__total_evolvers += 1
    
    @property
    def dna(self):
        if self.__dna == None:
            return Evolver.generate_random_dna()
        else:
            return self.__dna

    @staticmethod
    def generate_random_dna():
        alelos = [random_uniform(1,0) for _ in range(4)]
        dna = DNA(alelos)
        return dna
        
