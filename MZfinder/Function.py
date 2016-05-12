import string, os
import matplotlib.pyplot as plt
from Class import Species

def test_for_number(stringtotest):

    string_of_numchars = ''
    for char in stringtotest:
        if char.isdigit():
            string_of_numchars = string_of_numchars + char
       
    if len(string_of_numchars) == 0:
        return False
    
    else:
        if int(string_of_numchars) > 100:
            return True
        else:
            return False

def number_only(numstring):
    list_of_numchars = ''
    for char in numstring:
        if char.isdigit() or char == '.':
            list_of_numchars = list_of_numchars + char

    print list_of_numchars
    return float(list_of_numchars)


def read_input_file(filename, mz_file):
    
    fp = open(filename)
    important_nums_p = open(mz_file)

    all_species = []
    lines = important_nums_p.readlines()

    for line in lines:
        if not test_for_number(line):
            if line != lines[0]:
                all_species.append(species)
            species = Species(line.strip('\n'))
            
        else:
            species.add_mz(number_only(line))
        
    # Don't forget to add the last one!
    all_species.append(species)

    #for species in all_species:
    #    print species.get_name(), ":", species.get_first_mz()

    lines = fp.readlines()

    mz_Int_dict = {}

    for line in lines:
        parts = line.split('\t')
        if len(parts) == 2:
            mz_Int_dict[float(parts[0])] = float(parts[1].strip('\n'))
        else:
            pass
    
    #for key,value in mz_Int_dict.iteritems():
    #    if float(key) < 150:
    #        print key, ":", value

    #print "Species : reference mz : found mz : intensity"

    # Below code catches all mz values around the desired values
    # Later code catches only one for each desired M/Z value

    #for species in all_species:
    #    for mz in species.get_mz_list():
    #        for key, value in mz_Int_dict.iteritems():
    #            if key-0.05 < mz and key+0.05 > mz:
    #                print species.get_name(),':', mz,":", key, ":", value
    #                species.add_found_mz(key)
    #                species.add_found_intensity(value)

    for species in all_species:
        for mz in species.get_mz_list():
            possible_match_mz = 0.0
            possible_match_int = 0.0
            for key, value in mz_Int_dict.iteritems():
                if key-0.05 < mz and key+0.05 > mz:
                    if value > possible_match_int:
                        possible_match_mz = key
                        possible_match_int = value
            species.add_found_mz(possible_match_mz)
            species.add_found_intensity(possible_match_int)
            #print species.get_name(),':', mz,":", \
            #    possible_match_mz, ":", possible_match_int 

    return all_species


def plot_mzs(all_species):
    for species in all_species:
        fig = plt.figure()
        ax = fig.add_subplot(111)

        mzs = species.get_found_mzs()
        print "len mzlist",len(mzs)
        intensities = species.get_found_intensities()
        print "len Intensity list", len(intensities)
        mz_plot = plt.bar(mzs, intensities, width=0.001)

        fig.canvas.draw
        plt.show()

def write_output(species_list, outfilename):
    
    op = open(outfilename, 'w')
    op.write('mz, intensity\n')
    for species in species_list:
        mzs = species.get_found_mzs()
        ints = species.get_found_intensities()
        for i, mz in enumerate(mzs):
            if mz > 0.0:
                op.write(str(mz) + ',' + str(ints[i]) + "\n")
            
    op.close()

def get_input_filenames():
    fileslist = []
    for file in os.listdir("."):
        if file.endswith(".txt") and 'output' not in file \
           and "important" not in file:
            fileslist.append(file)
    print "filenames are:", fileslist

    return fileslist

if __name__ == "__main__":
    fileslist = get_input_filenames()
    for file in fileslist:
        outfilename = file.strip('.txt') + "_output.csv"
        species_list = read_input_file(file, "important_values.csv")
        write_output(species_list, outfilename)

        
