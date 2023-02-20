class ZeroDivisionError(Exception):
    text = "Внимание!!! Деление на ноль запрещено!!! Продолжайте согласно правилам деления на ноль!!!"

    def __str__(self):
        return self.text


class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise ZeroDivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input("Введите делимое и делитель через пробел: ").split())
            print(dividend / divider)
        except ZeroDivisionError as w:
            print(w)
        except ValueError as w:
            print(w)
            break
