class CompoundInterest():
    def __init__(self, input_principle, input_rate):
        self.P = input_principle
        self.R = input_rate
        self.years = 1
        self.times_compounded = 12
        self.A = 0

    # Methods:
    def calculate_amount(self, input_years):
        exponent = input_years * self.times_compounded
        brackets = (1 + (self.R/ self.times_compounded))
        almost_total = brackets ** exponent
        self.A = round(self.P * almost_total, 2)
        return self.A

