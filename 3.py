class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


if __name__ == '__main__':
    my_listwow = []

    while True:
        user_input = input("Введите число для заполнения списка, или введите '#' для выхода: ")

        if user_input == "#":
            break

        try:
            if not user_input.isdigit():
                raise NotNumberError(f"'{user_input}' не введено число или введен не верный символ!!")

            my_listwow.append(int(user_input))
        except NotNumberError as e:
            print(e)

    print(my_listwow)
