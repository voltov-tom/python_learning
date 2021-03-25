class Matrix:
    def __init__(self, *args):
        self.args = args
        for line in args:
            for a in line:
                print(a)


M = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9, 10]])
