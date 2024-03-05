class LenghtConverter:
    def __init__(self,meter, inch, feet):
        self.__distance_in_meter = meter
        self.distance_in_inch = inch
        self.distance_in_feet = feet
    @property
    def meter(self):
        return self.__distance_in_meter
    @meter.setter
    def meter(self):
        return self.__distance_in_meter
    
    @property
    def inch(self):
        self.distance_in_inch = self.__distance_in_meter*393.701
        return self.distance_in_inch
    @inch.setter
    def inch(self):
        self.__distance_in_meter = self.distance_in_inch/393.701
        return self.__distance_in_meter
    
    @property
    def feet(self):
        pass