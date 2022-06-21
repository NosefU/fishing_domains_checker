from abc import abstractmethod, ABC
from typing import Generator


class AbstractMutator(ABC):
    """
    Абстрактный класс мутатора.
    Представляет из себя итератор, возвращающий одну мутацию ключевого слова за другой
    """
    def __init__(self, keyword: str):
        self.keyword = keyword

    def __iter__(self):
        return self.get_mutations()

    @abstractmethod
    def get_mutations(self) -> Generator[str, None, None]:
        """
        Генератор, в котором реализуются мутации ключевого слова

        :return: Изменённые ключевые слова, без исходного
        """
        pass
