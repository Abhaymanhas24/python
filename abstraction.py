from abc import ABC, abstractmethod


class Account:
    def saving(self):
        print("zero balance account")


class Cards(ABC):
    @abstractmethod
    def cashback(self):
        pass

    def easypay(self):
        pass


class Cards1(Cards):
    def cashback(self):
        print("cashback cerid card")
