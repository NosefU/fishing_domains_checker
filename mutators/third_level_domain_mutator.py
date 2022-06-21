from . import AbstractMutator


class ThirdLevelDomainMutator(AbstractMutator):
    """
    Мутатор, который добавляет точку в ключевое слово,
    например: 'abcd' -> 'a.bcd', 'ab.cd', 'abc.d'
    """
    def get_mutations(self):
        for i in range(1, len(self.keyword)):  # точка в начале и конце хостнейма нам не нужна
            if self.keyword[i-1] == '.' or self.keyword[i] == '.':  # две точки подряд нам тоже не нужны
                continue
            yield '{}.{}'.format(self.keyword[:i], self.keyword[i:])
