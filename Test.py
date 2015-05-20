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
    def _id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def mass(self):
        return self.__mass
    
    #setter methods
    @_id.setter
    def _id(self, value):
        if not isinstance(value, int):
            raise TypeError("_id must be an Integer.")
        self.__id = value

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string.")
        self.__name = value

    @mass.setter
    def mass(self, value):
        if not isinstance(value, float):
            raise TypeError("Mass must be a float.")
        self.__mass = value

    # 1. Write setter and getter methods for all attributes.
    #    Use @property decorators as dicussed in the lecture
    # 2. In the setter methods check for the type of each attribute.

class Polymer(BioMolecule):
    """
    A polymer molecule that has a sequence attribute which is
    accessible via indexing the object. 

    @type id: int
    @type name: str
    @type sequence: str
    @type mass: float
    """
    def __init__(self, id, name, sequence, mass=None):
        # 3. Initialize the parent class correctly
        super(Polymer, self).__init__(id, name, mass)
        self._sequence = sequence

    # 4. Write getter and setter for sequence, again check for type
    @property
    def _sequence(self):
        return self.__sequence

    @_sequence.setter
    def _sequence(self, value):
        if not isinstance(value, str):
            raise TypeError("_sequence must be an string.")
        self.__sequence = value   
    # 5. run in ipython, instantiate this class, and test it
    def __getitem__(self, value):
        """
        Makes the sequence accessible via the indexing operators:
<        p[10] returns the tenth character in the sequence.
        """
        return self.sequence[value]

    def __setitem__(self, key, value):
        """
         Enables changing of sequence characters via the indexing operators.       
        """
        self.sequence[key] = value

class MRNA(Polymer):
    def __init__(self, id, name, sequence, mass=None):
        # 6. Initialize the parent class correctly
        super(MRNA, self).__init__(id, name, sequence, mass)
        # 7. Create a list that stores if a ribosome is bound for each
        # codon (triplet).
        self.binding = [] # use this attribute for 7.
        x=0
        while x < (len(sequence)/3):
            self.binding.append(False)
            #print self.binding[x]
            x=x+1
        #seqsplit=list(sequence)
        #print seqsplit
    def calculate_mass(self,sequence):
        NA_mass = {'A': 1.0, 'U': 2.2, 'G':2.1, 'C':1.3}
        # 8. calculate the mass for the whole sequence
        y=0
        calc=0
        while y < (len(sequence)):
            calc=calc+NA_mass[sequence[y]]
            y=y+1
        return calc

class Protein(Polymer):
    """Protein with Polymer features and mass calculation. A global class
    attribute counts the number of proteins that have been instantiated.
    
    A protein can be elongated using the "+" operator:
    
    >> protein = Protein(1, "prot", "MVFT")
    >> protein + "A"
    >> protein.sequence
    MVFTA

    
    
    """
    number_of_proteins = 0  # init instance counter

    def __init__(self, id, name, sequence, mass=None):
        super(Protein, self).__init__(id, name, sequence, mass)
        self.__class__.number_of_proteins += 1 #  increase instance counter
        self.mass = self.calculate_mass()

    # 9. implement the elongation feature described in the docstring. (__add__)
    def __add__ (self, AS):
        return (self._sequence + AS)

    def calculate_mass(self):
        AA_mass = {"A": 89.0929, "R": 175.208, "N": 132.118, "D": 132.094, "C": 121.158, "Q": 146.144,
                    "E": 146.121, "G": 75.0664, "H":155.154, "I":131.172, "L": 131.172, "K": 147.195,
                    "M": 149.211, "F": 165.189, "P": 115.13, "S": 105.092, "T": 119.119, "W": 204.225,
                    "Y":181.188, "V":117.146}
        for aa in self._sequence:
            self.mass += AA_mass[aa]
   
           

Prot = Protein(123 , 'protA' , 'AAAGC' , 30.0)
Prot = Prot + "A"
print Prot._sequence
#print Prot.calculate_mass(Prot._sequence)