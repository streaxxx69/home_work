class Animal:
    def speak(self):
        print("Животное говорит!")


class Dog:
    def speak(self):
        print("гав-гав")

print("----------------------")


dog = Dog()
dog.speak()

class Small_dog:
    def speak(self):
        print("тяв-тяв")


dog = Dog()
dog.speak()

class Big_dog:
    def speak(self):
        print("Вуф-Вуф")

dog = Dog()
dog.speak()
class Robotdog(Small_dog):

    def speak(self):
        print("Звучит как робот гав-гав")

dog = Dog()
dog.speak()

class BigAngruDog(Big_dog):
    def speak(self):
        print("Очень злой взгляд!!!")
        Big_dog.speak(self)
        print("хмурится")

sharik = BigAngruDog
sharik.speak()
animal = Animal()
animal.speak()

