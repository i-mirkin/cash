class Base:
    def price(self):
        return 10
class InterFoo(Base):
    def price(self):
        # return super().price() * 1.1
        return Base.price(self) * 1.1


InterFooObj = InterFoo()
print (InterFooObj.price())

