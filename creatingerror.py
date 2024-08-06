class EligileError(Exception):
    def __init__(self, value):
        pass


class Sample:
    def eligible(self, age, percentage):
        if age < 18 or percentage < 60:
            raise EligileError("Not Eligible for Registration")
        else:
            print("Registration success")


obj1 = Sample()
try:
    obj1.eligible(16, 65)
except EligileError as e:
    print(e)
print("End of Program")
