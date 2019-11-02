class Doctor:
    """This class is a template for a Doctor type of data."""
    toString = """
    Doctor:
        Name: \033[1m{}\033[m
        Specialty: \033[1m{}\033[m
        Skills: \033[1m{}\033[m
    Address/Contact:
        State: \033[1m{}\033[m
        City: \033[1m{}\033[m
        Phone: \033[1m{}\033[m
    """

    def __init__(self,name="---",specialty="---",skills="---",\
            state="---",city="---",phone="---"):
        self.__name = name
        self.__specialty = specialty
        self.__skills = skills
        self.__state = state
        self.__city = city
        self.__phone = phone


    def getName(self):
        return self.__name

    def getSpecialty(self):
        return self.__specialty

    def getSkills(self):
        return self.__skills

    def getState(self):
        return self.__state

    def getCity(self):
        return self.__city

    def getPhone(self):
        return self.__phone

    def setName(self,name):
        self.__name = name.strip()

    def setSpecialty(self,specialty):
        self.__specialty = specialty.strip()

    def setSkills(self,skills):
        self.__skills = skills.strip()

    def setState(self,state):
        self.__state = state.strip()

    def setCity(self,city):
        self.__city = city.strip()

    def setPhone(self,phone):
        self.__phone = phone.strip()

    def __repr__(self):
        return Doctor.toString.format(
            self.getName(), self.getSpecialty(),
            self.getSkills(), self.getState(),
            self.getCity(), self.getPhone()
        )


    def __eq__(self,other):
        if self.getName().lower() == other.getName().lower() and \
            self.getSpecialty().lower() == other.getSpecialty().lower() and \
            self.getSkills().lower() == other.getSkills().lower() and \
            self.getState().lower() == other.getState().lower() and \
            self.getCity().lower() == other.getCity().lower() and \
            self.getPhone().lower() == other.getPhone().lower():
            return True
        return False






