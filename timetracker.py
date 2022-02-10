import datetime
import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog as fd
from PIL import ImageTk, Image
import os
import analysis

data = []

class TimeTracker(tk.Frame):

    def __init__(self, master = None):
        tk.Frame.__init__(self, master) 
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        f = tkFont.Font(size = 16, family = "Courier New")
        
        self.LoadFileButton = tk.Button(self, text = "Choose a file", height = 1, width = 40, command = self.clickLoadFileButton, font = f)
        self.PlotButton = tk.Button(self, text = "plot!", height = 1, width = 5, command = self.clickPlotButton, font = f)
        self.MainCanvus = tk.Canvas(self, width = 800, height = 600, bg = "white")

        self.StartTimeLabel = tk.Label(self, text = "start date:", height = 1, width = 10, font = f)
        self.EndTimeLabel = tk.Label(self, text = "  end date:", height = 1, width = 10, font = f)
        self.StartTimeBox = tk.Text(self, height = 1, width = 15, font = f)
        self.StartTimeBox.insert("1.0", "2022-01-28-00-00")
        self.EndTimeBox = tk.Text(self, height = 1, width = 15, font = f)
        self.EndTimeBox.insert("1.0", "2022-01-28-23-59")
        
        self.LoadFileButton.grid(row = 0, rowspan = 2, column = 0, columnspan = 2, sticky = tk.NE + tk.SW)
        self.PlotButton.grid(row = 0, rowspan = 2, column = 2, sticky = tk.W)
        self.MainCanvus.grid(row = 2, column = 0, columnspan = 6, sticky = tk.NE + tk.SW)

        self.StartTimeLabel.grid(row = 0, column = 4, sticky = tk.E)
        self.EndTimeLabel.grid(row = 1, column = 4, sticky = tk.E)
        self.StartTimeBox.grid(row = 0, column = 5, sticky = tk.NE + tk.SW)
        self.EndTimeBox.grid(row = 1, column = 5, sticky = tk.NE + tk.SW)
    
    
    def clickLoadFileButton(self):
        global data
        filename = fd.askopenfilename()
        if(filename.split('/')[-1][-3::] == "csv"):
            self.LoadFileButton.config(text=filename.split('/')[-1])
            data = analysis.read_csv(filename)
        else:
            self.LoadFileButton.config(text="Not csv file")

    def clickPlotButton(self):
        start_time = datetime.datetime.strptime(self.StartTimeBox.get("1.0", tk.END).strip(), "%Y-%m-%d-%H-%M")
        end_time = datetime.datetime.strptime(self.EndTimeBox.get("1.0", tk.END).strip(), "%Y-%m-%d-%H-%M")

        pic_name = analysis.one_day_status(data, start_time, end_time)
        
    #     self.makeScatter(x, y)

        self.MainImage = Image.open(pic_name)
        # self.MainImage = self.MainImage.resize((800, 600), Image.ANTIALIAS)
        self.MainImage = ImageTk.PhotoImage(self.MainImage)
        self.MainCanvus.create_image(400, 300, image = self.MainImage, anchor = tk.CENTER)
    #     os.system("del temp.png")

    # def makeScatter(self, x, y): 
    #     fig = pyplot.figure()
    #     ax = fig.add_subplot(111)
        
    #     rangeX = max(x) - min(x)
    #     ax.set_xlim(min(x) - rangeX * 0.1, max(x) + rangeX * 0.1)
    #     rangeY = max(y) - min(y)
    #     ax.set_ylim(min(y) - rangeY * 0.1, max(y) + rangeY * 0.1)

    #     pyplot.plot(x, y, 'bo')

    #     for i, j in zip(x, y):
    #       ax.annotate(str(i) + ", " + str(j), xy = (i + 0.1, j + 0.1))

    #     pyplot.savefig("temp.png") 


tracker = TimeTracker()
tracker.master.title("Time Tracker")
tracker.mainloop()