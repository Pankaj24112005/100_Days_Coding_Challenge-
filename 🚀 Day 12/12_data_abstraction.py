# Day 12: Data Abstraction in Python

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


# Child class implementing abstract methods
class Car(Vehicle):

    def start(self):
        print("Car engine started")

    def stop(self):
        print("Car engine stopped")


class Bike(Vehicle):

    def start(self):
        print("Bike engine started")

    def stop(self):
        print("Bike engine stopped")


# Creating objects
car = Car()
bike = Bike()

car.start()
car.stop()

bike.start()
bike.stop()
