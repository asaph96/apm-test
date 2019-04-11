class DNA(object):

    def __init__(self, alelos: list):
        self.__alelos = alelos

    @property
    def alelos(self) -> dict:
        alelos = dict()
        for gene in self.__alelos:
            alelos[f"gene{self.__alelos.index(gene)+1}"] = gene
        return alelos
