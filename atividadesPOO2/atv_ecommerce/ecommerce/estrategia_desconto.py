from abc import ABC, abstractmethod
from functools import total_ordering
class EstrategiaDesconto(ABC):
    @abstractmethod
    def calcular(self, total: float) -> float:
        ...
class SemDesconto(EstrategiaDesconto):
    def calcular(self, total) -> float:
        return total
class DescontoPercentual(EstrategiaDesconto):
    def __init__(self, percentual: float) -> None:
        if not 0 <= percentual <= 100:
            raise ValueError("O percentual de desconto deve estar entre 0 e 100")
        self._percentual = percentual
    def calcular(self, total) -> float:
        return total - (total * self._percentual / 100.0)