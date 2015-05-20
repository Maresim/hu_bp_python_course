class BioMolecule(object):
    """
    A generic molecule that has basic attributes like id, name and
    mass.

    @type id: int
    @type name: str
    @type mass: float
    """
    def __init__(self, id, name, mass=None):
        self._id = id
        self.name = name
        self.mass = mass

    #getter methods
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.name

    @property
    def mass(self):
        return self.mass
    
    #setter methods
    @id.setter
    def id(self, value):
        self.__id = value

    @name.setter
    def name(self, value):
        self.name = value

    @mass.setter
    def mass(self, value):
        self.mass = value

    # 1. Write setter and getter methods for all attributes.
    #    Use @property decorators as dicussed in the lecture
    # 2. In the setter methods check for the type of each attribute.
