#!/usr/bin/env python3

'''
Write a context manager that generates HTML.
Call it HtmlCM
In the __init__ method, do nothing
In the __enter__ method, display the HTML table header, more or less like this:

<TABLE>
 <TR>
     <TH>Number</TH><TH>Description</TH>.
 </TR>
In the __exit__ method, display a closing tag for the table, roughly like this:

</TABLE>.

Use the new context manager by using the appropriate with ...
Inside the context manager display 2 rows of the table, more or less like this:

 <TR>
     <TD>1</TD><TD>Say hello!</TD)
 </TR>
 <TR>
     <TD>2</TD><TD>Say good bye!</TD)
 </TR>
'''


class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print("<TABLE>")
        print(" <TR>")
        print("     <TH>Number</TH><TH>Description</TH>")
        print(" </TR>")
        return self

    def __exit__(self, type, value, traceback):
        print("</TABLE>")


with HtmlCM() as html:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")