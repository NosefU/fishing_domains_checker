from mutators import AbstractMutator


class LastCharMutator(AbstractMutator):
    """
    Мутатор, который добавляет к ключевому слову ещё один символ либо цифру,
    например: 'aol' -> 'aola', 'aolb', ..., 'aolz', 'aol0', ..., 'aol9'
    """
    def get_mutations(self):
        for char_code in range(ord('a'), ord('z') + 1):
            yield self.keyword + chr(char_code)
        for i in range(10):
            yield self.keyword + str(i)
        return
