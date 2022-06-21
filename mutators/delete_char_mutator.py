from . import AbstractMutator


class DeleteCharMutator(AbstractMutator):
    """
    Мутатор, который удаляет из ключевого слова по одному символу,
    например: 'abc' -> 'bc', 'ac', 'ab'
    """
    def get_mutations(self):
        for i in range(len(self.keyword)):
            yield self.keyword[:i] + self.keyword[i + 1:]