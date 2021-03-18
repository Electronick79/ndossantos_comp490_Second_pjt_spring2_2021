from tkinter.filedialog import *
from tkinter.messagebox import *

import pandas as pd
import numpy as np


# When your program first starts up, with the python GUI, allow the user to choose to either
# update the data run the data visualization

class Notepad:

    __root = Tk()

    # default window width and height
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)

    # To add scrollbar
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None


    def __init__(self, **kwargs):

        # Set icon
        try:
            self.__root.wm_iconbitmap("Excel.ico")
        except:
            pass

        # Set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        # Set the window text
        self.__root.title("Untitled - Excel")

        # Center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        # For left-alling
        left = (screenWidth / 2) - (self.__thisWidth / 2)

        # For right-allign
        top = (screenHeight / 2) - (self.__thisHeight / 2)

        # For top and bottom
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth,
                                              self.__thisHeight,
                                              left, top))

        # To make the textarea auto resizable
        self.__root.grid_rowconfigure(0, weight=1)
        self.__root.grid_columnconfigure(0, weight=1)

        # Add controls (widget)
        self.__thisTextArea.grid(sticky=N + E + S + W)

        # To open new file
        self.__thisFileMenu.add_command(label="New",
                                        command=self.__newFile)

        # To open a already existing file
        self.__thisFileMenu.add_command(label="Open",
                                        command=self.__openFile)

        # To save current file
        self.__thisFileMenu.add_command(label="Save",
                                        command=self.__saveFile)

        # To create a line in the dialog
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Exit",
                                        command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="File",
                                       menu=self.__thisFileMenu)

        # To give a feature of cut
        self.__thisEditMenu.add_command(label="Cut",
                                        command=self.__cut)

        # to give a feature of copy
        self.__thisEditMenu.add_command(label="Copy",
                                        command=self.__copy)

        # To give a feature of paste
        self.__thisEditMenu.add_command(label="Paste",
                                        command=self.__paste)

        # To give a feature of editing
        self.__thisMenuBar.add_cascade(label="Edit",
                                       menu=self.__thisEditMenu)

        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="About Excel",
                                        command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Help",
                                       menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT, fill=Y)

        # Scrollbar will adjust automatically according to the content
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)

        # ////////////////////////////////////////////////////////////////////////////////////////////////
        # When your program first starts up, with the python GUI, allow the user to choose to either
        # update the data run the data visualization
        from bokeh.io import output_file, output_notebook
        from bokeh.plotting import figure, show
        from bokeh.models import ColumnDataSource
        from bokeh.layouts import row, column, gridplot
        from bokeh.models.widgets import Tabs, Panel

        # Determine where the visualization will be rendered
        output_file('filename.html')
        output_notebook()  # Render inline in a Jupyter Notebook

        # Set up the figure(s)
        fig = figure()

        df = pd.read_xlsx(r'C:\Users\Electronick\OneDrive\Desktop\COMP_490\COMP490_SPRING_3.xlsx')
        # Create an empty string called ticker_string
        ticker_string = ''
        # Loop through every element of `tickers` and add them and a comma to ticker_string
        for ticker in tickers:
            ticker_string += ticker
            ticker_string += ','
        # Drop the last comma from `ticker_string`
        ticker_string = ticker_string[:-1]

        # Create the endpoint and years strings
        endpoints = 'chart'
        years = '5'
        #   When updating the data: let the user choose the file name for the excel file
        def writer(header, data, filename, option):
            with open(filename, "w", newline="") as xlsxfile:
                if option == "write":

                    movies = xlsxfile.writer(csvfile)
                    movies.writerow(header)
                    for x in data:
                        movies.writerow(x)
                elif option == "update":
                    writer = xlsx.DictWriter(csvfile, fieldnames=header)
                    writer.writeheader()
                    writer.writerows(data)
                else:
                    print("Option is not known")


        # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

    def __quitApplication(self):
        self.__root.destroy()

    # exit()

    def __showAbout(self):
        showinfo("Excel", "Mrinal Verma")

    def __openFile(self):

        self.__file = askopenfilename(defaultextension=".xlsx",
                                      filetypes=[("All Files", "*.*"),
                                                 ("Xlsx Documents", "*.xlsx")])

        if self.__file == "":

            # no file to open
            self.__file = None
        else:

            # Try to open the file
            # set the window title
            self.__root.title(os.path.basename(self.__file) + "r'C:\ Users\Electronick\OneDrive\Desktop\COMP_490\COMP490_SPRING_4.xlsx ")
            self.__thisTextArea.delete(1.0, END)

            file = open(self.__file, "r")

            self.__thisTextArea.insert(1.0, file.read())

            file.close()

    def __newFile(self):
        self.__root.title("Untitled - Excel")
        self.__file = None
        self.__thisTextArea.delete(1.0, END)

    def __saveFile(self):

        if self.__file == None:
            # Save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.xlsx',
                                            defaultextension=".xlsx",
                                            filetypes=[("All Files", "*.*"),
                                                       ("Exel Documents", "*.xlsx")])

            if self.__file == "":
                self.__file = None
            else:

                # Try to save the file
                file = open(self.__file, "w")
                file.write(self.__thisTextArea.get(1.0, END))
                file.close()

                # Change the window title
                self.__root.title(os.path.basename(self.__file) + " - Excel")


        else:
            file = open(self.__file, "w")
            file.write(self.__thisTextArea.get(1.0, END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        # Run main application
        self.__root.mainloop()

    # Run main application


Excel = excel(width=600, height=400)
excel.run()