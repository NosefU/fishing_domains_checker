from itertools import product
from typing import List, Type, Generator

from mutators import AbstractMutator


class FishingDomainsGenerator:
    def __init__(self, keyword: str, mutators: List[Type[AbstractMutator]], domain_zones: List[str]):
        self.keyword = keyword.lower()
        self.mutators = mutators
        self.domain_zones = domain_zones

    def __iter__(self):
        return self.gen()

    def gen(self) -> Generator[str, None, None]:
        """
        Прогоняет ключевое слово через все мутаторы (по одному) и комбинирует мутации с доменными именами

        :return: Доменные имена: все мутации в каждой доменной зоне
        """
        for mutator in self.mutators:
            mutations = mutator(self.keyword)
            for hostname, domain_zone in product(mutations, self.domain_zones):
                yield '{}.{}'.format(hostname, domain_zone)
