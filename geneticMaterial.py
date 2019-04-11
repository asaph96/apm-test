class DNA(object):

    def __init__(self, alelos: list, gene_names: list = None):
        self.__alelos = alelos
        self.__genname = gene_names

    @property
    def alelos(self) -> dict:
        alelos = dict()
        if self.__genname == None:
            for gene in self.__alelos:
                alelos[f"gene{self.__alelos.index(gene)+1}"] = gene
        else:
            for gene, name in zip(self.__alelos, self.__genname):
                alelos[f"{name}"] = gene
        return alelos
