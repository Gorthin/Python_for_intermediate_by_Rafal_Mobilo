#!/usr/bin/env python3
import types

'''
Your nice colleague from another team has prepared a function to export the data:

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

Assign this function to the Cake class with the name export_1_cake_to_html
Modify the function export_1_cake_to_html as appropriate and then assign it
as a class function to the Cake class. The name of the new function is
export_all_cakes_to_html. Its job is to export all the baked goods stored
in the bakery_offer variable. Because now you have more cakes to export,
in original function you have to write a loop which will add cake after cake to html file.

One last thing. Modify the original function accordingly and assign it to each
cake object at the instance level. To do this, go through the list of all
objects in bakery_offer and assign the function to each object.
Name the function export_this_cake_to_html. Then write a second loop
that will go through the list of all the baked goods and export each
one to HTML to a file with a name that matches the name of the cake (replace spaces with "_")
'''


def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)


def export_all_cakes_to_html(cls, path):
    template_header = """
<table border=1>"""
    template_data = """
     <tr>
       <th colspan=2>{}</th>
     </tr>
     <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>"""
    template_footer = """</indent>
</table>"""
    with open(path, "w") as f:
        f.write(template_header)
        for c in cls.bakery_offer:
            content = template_data.format(c.name, c.kind, c.taste, c.additives, c.filling)
            f.write(content)
        f.write(template_footer)


def export_this_cake_to_html(self, path):
    template = """
<table border=1>
     <tr>
       <th colspan=2>{}</th>
     </tr>
       <tr>
         <td>Kind</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Taste</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Additives</td>
         <td>{}</td>
       </tr>
       <tr>
         <td>Filling</td>
         <td>{}</td>
       </tr>
</table>"""

    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)


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
            print('>>>>>Text can be set only for cake ({})'.format(name))

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return __text

    def __set_text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))

    Text = property(__get_text, __set_text, None, 'Text on the cake')


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, 'Good luck!')

# static method:
Cake.export_1_cake_to_html = export_1_cake_to_html
Cake.export_1_cake_to_html(cake01, 'D:\\1_PYTHON_PROJEKTY\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\cake01.html')

# class method:
Cake.export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.export_all_cakes_to_html('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\all_cakes.html')

# instance method:
for c in Cake.bakery_offer:
    c.export_this_cake_to_html = types.MethodType(export_this_cake_to_html, c)
for c in Cake.bakery_offer:
    c.export_this_cake_to_html('D:\\1_PYTHON_PROJEKTY\\Python_for_intermediate_by_Rafal_Mobilo\\Chapter5_Classes\\{}.html'.format(c.name.replace(' ', '_')))