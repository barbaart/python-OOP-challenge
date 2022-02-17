from abc import ABC, abstractmethod
import random

# hints:
# create a basic abstract class with ABC link
# Put the shared functions in this base class
class Radio(ABC):

    def __init__(self):
        self.volume = 1
        self.power = False

    def increaseVolume(self):
        """increase volume. The volume level can be between 1-10"""
        if self.volume != 10:
            self.volume += 1
            return "volume set to {}".format(self.volume)
        else:
            return "max volume"

    @abstractmethod
    def powerSwitch(self):
        """Turn on/off. This is a Boolean state"""
        if self.power:
            self.power = False
            print("turned off")
        else:
            self.power = True
            print("turned on")

    def sayHello(self):
        """sayHello. Prints the type of object to the console"""
        print(type(self))


class PortableGhettoblaster(Radio):

    def __init__(self):
        self.__batteryPercentage = self.__batteryPower()
        super().__init__()

    # In case the percentage is < 5 => the ghetto blaster won't turn on
    def powerSwitch(self):
        if self.__batteryPercentage >= 5:
            return super().powerSwitch()
        else:
            return "battery low!"

    # Only the portable ghetto blaster has the function battery power which returns (random) value of 0-100 of the battery percentage. 
    def __batteryPower(self):
        return random.randint(0, 100)


class HomeStereo(Radio):

    def powerSwitch(self):
        return super().powerSwitch()