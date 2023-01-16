class Calculator:
    def __init__(self, op: str):
        self.string = op
        self.operations = ['**', '*', '/', '+', '-']
        self.l_string = []
        oper = ''
        numb = ''

        for sym in self.string:
            if sym.isdigit():
                if numb:
                    numb+=sym
                else:
                    self.add_to_l_string(oper)
                    oper = ''
            else:
                if oper:
                    oper+=sym
                else:
                    self.add_to_l_string(numb)
                    numb = ''
        else:
            self.add_to_l_string(numb)


    def add_to_l_string(self, seq: str):
        if seq:
            if seq.isdigit():
                seq = int(seq)
            self.l_string.append(seq)

    def process(self):
        result = self.l_string
        return result


ariphmetic = input("Provide us with ariphmetic string:".replace(" "," "))

calc = Calculator(ariphmetic)
result = calc.process()


print("Result is", result)