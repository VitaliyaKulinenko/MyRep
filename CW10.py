class Number:
    def __init__(self, string: str):
        self.string = string.strip()
        self.sign = self.sign_test()
        self.type = self.type_test()
        self.incorrect = self.incorrect_test()
        # self.new_string = self.new_string_test()
    def test (self):
        return f'Вы ввели {self.sign}{self.type}{self.incorrect} число: {self.string}'
    def sign_test(self):
        if self.string[0]=='-':
            return 'Negative'
        else:
            return 'Positive'

    def type_test(self):
        count_dot= self.string.count('.')
        if count_dot ==0:
            return 'integer'
        elif count_dot ==1:
            return 'float'

    def incorrect_test(self):
        if self.sign == 'Negative' or self.sign == 'float':
            if self.string.replace('-','',1).replace('.', '', 1).isdigit():
                return "Correct"
            else:
                return "Incorrect"
        elif self.string.isdigit():
            return "Correct"
        else:
            return "Incorrect"




b = Number()
print (b.test)



