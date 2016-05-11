class Species(object):
    def __init__(self, name):
        self.__name = name
        self.__mzs = []
        self.__found_mzs = []
        self.__found_intensities = []

    def add_mz(self, mz):
        #print "adding", mz,'to', self.__name
        self.__mzs.append(float(mz))

    def add_found_mz(self, found_mz):
        self.__found_mzs.append(float(found_mz))

    def add_found_intensity(self, found_intensity):
        self.__found_intensities.append(float(found_intensity))

    def get_name(self):
        return self.__name

    def get_first_mz(self):
        return self.__mzs[0]

    def get_mz_list(self):
        return self.__mzs
        
    def get_found_mzs(self):
        return self.__found_mzs

    def get_found_intensities(self):
        return self.__found_intensities
