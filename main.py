class DuplicatesFinder:
    """
    Класс для поиска любых повторяющихся чисел в массиве из N + 2 целых чисел в диапазоне [1, N].
    """

    def __init__(self, array):
        """
        Инициализирует новый экземпляр класса DuplicatesFinder.

        Args:
            array (list): Массив из N + 2 целых чисел в диапазоне [1, N].
        """
        self.n = len(array) - 2
        self.array = array

    def find_duplicates(self):
        """
        Находит любое повторяющееся число в массиве.

        Returns:
            int или None: Значение повторяющегося числа в массиве, или None, если повторяющееся число не найдено.
        """
        for i in range(self.n + 2):
            index = abs(self.array[i]) - 1
            if self.array[index] > 0:
                self.array[index] = -self.array[index]
            else:
                return abs(self.array[i])
        return None


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 3]
    finder = DuplicatesFinder(array)
    duplicate = finder.find_duplicates()
    print(duplicate)
