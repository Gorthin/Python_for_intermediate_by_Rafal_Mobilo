#!/usr/bin/python3
import pickle
import glob

'''
Our task is to save on disk information about the products of our confectionery. 
Cake class objects are already a bit complicated, so to export them to disk 
and import from disk we will use pickle module. 
(A few words about the module and a link to the documentation can be found below), and here is a brief summary:

You can import the module with the command
import pickle
If f is a file handle and obj is an object, you can save it to disk with the command:
pickle.dump(obj, f)
And if you then want to read that object, you can do it like this:
new_obj = pickle.load(f)
So here's what to do.
Add the save_to_file function to the class. The function should work at the instance level
The function should take path argument indicating the file path
Open the file for writing in binary mode and using pickle.dump save the current object to the file
Test the function by writing cake01 and cake02 to files. Give the files a bakery extension
Add the read_from_file function to the class. This function should take as argument the path to the file
Open the file to read in binary mode and load a Cake class object from the file using pickle.load
Add a new object to the bakery_offer class variable and return that object
Test the function by loading the file from the previous example 
into a new object such as cake05. To test if everything worked, call for this new object from the show_info function
Okay, but if we know the path to a directory and there are files with the extension 
bakery in that directory, we would like to have a function that returns a list of such files. 
You can find an almost ready-made function for this in the glob module:
import glob
To get a list of files with txt extension from the c:/temp directory, you can call the function
glob.glob('c:/temp/*.txt')
Add to Cake class static function get_bakery_files, which takes as argument directory name
The function will return a list of files with the extension bakery from the directory
Test the function
'''


class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print("The text will only fit on the cake.")

    def show_info(self):
        print("Name: {}".format(self.name).upper())
        print("Taste : {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("- {}".format(a))
        if len(self.filling) > 0:
            print("Filling:")
            print("- {}\n".format(self.filling))
        print("Texr on a cake : {}".format(self.__text))
        print("Gluten : {}".format(self.__gluten_free))
        print('=' * 30)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')

    def save_to_file(self, path):
        with open(path,'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(catalog):
        return glob.glob(catalog + '/*.bakery')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

cake01.save_to_file('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\cake01.bakery')
cake02.save_to_file('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\cake02.bakery')

cake05 = Cake.read_from_file('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\cake01.bakery')
cake05.show_info()

print(Cake.get_bakery_files('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes'))
