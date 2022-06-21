from . import AbstractMutator


class HomoglyphMutator(AbstractMutator):
    """
    Мутатор, который заменяет символы похожими,
    например: 'aol' -> 'ao1', 'a0l', 'a01'
    """
    # предположим, что нам доступны только латиница и цифры
    # для добавления кириллицы достаточно расширить карту
    replacing_map = {
        '0': ['o', ],
        '1': ['i', 'l'],
        'd': ['cl', ],
        'i': ['l', 'j', '1'],
        'j': ['i', ],
        'l': ['1', ],
        'm': ['rn', ],
        'o': ['0', ],
        'w': ['vv', ],
    }

    def get_replacements(self, substr: str):
        """
        Рекурсивно заменяет символы слова в соответствии с таблицей замен

        :param substr: исходная строка
        :return: изменённые строки, начиная с исходной, например: 'aol' -> 'aol', 'ao1', 'a0l', 'a01'
        """
        if not substr:
            yield ''
            return

        for repl_char in [substr[0], ] + self.replacing_map.get(substr[0], []):
            for replacement in self.get_replacements(substr[1:]):
                yield repl_char + replacement

    def get_mutations(self):
        # первой идёт исходная строка, поэтому её исключаем
        mutations = self.get_replacements(self.keyword)
        next(mutations)
        yield from mutations
