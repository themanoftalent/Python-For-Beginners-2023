class Eggs:

    def __init__(self, kind='Frying'):
        self.kind = kind

    def whatSort(self):
        return self.kind


def main():
    frying = Eggs()
    scrambled = Eggs("Scrambled")
    lessFrying = Eggs("Not fried")

    print(frying.whatSort())
    print(scrambled.whatSort())
    print(lessFrying.whatSort())


if __name__ == '__main__':
    main()
