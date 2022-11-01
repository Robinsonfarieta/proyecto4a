from abc import ABCMeta
class ModeloAbs(metaclass=ABCMeta):
    def __init__(self, datos):
        for clave,valor in datos.items():
            setattr(self,clave,valor)
