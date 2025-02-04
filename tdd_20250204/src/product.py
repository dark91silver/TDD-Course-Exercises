class Product():
    id: int
    nome: str
    prezzo: float
    quantità: int = 0

    def __init__(self, id: int, nome: str, prezzo: float, quantità: int):
        self.id = id
        self.nome = nome
        self.prezzo = prezzo
        self.quantità = quantità