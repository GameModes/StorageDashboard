import wmi
from tkinter import *

from PIL import Image, ImageTk
import turtle




def Gui(percentage, naamschijf):
  root = Tk()

  root.geometry('300x300')
  root.overrideredirect(True)
  root.overrideredirect(False)

  c = Canvas(root, height=250, width=300, bg="white", bd=0 ,highlightthickness=0, )


  originelheight = 100
  originelwidth = 250
  perwidth = originelwidth * percentage
  perheight = originelheight

  lbl = Label(root, text=naamschijf + " "+ str( (int(percentage * 100))) + "% used")

  def remove_func():
      emptyMenu = Menu(root)
      root.config(menu=emptyMenu)



  lbl.grid(column=0, row=1)

  remove_button = Button(root, text="Remove", command=remove_func)
  remove_button.grid(column=0, row=3)
  # x1, (l) y1,(u) x2, (r) y2 (d)
  rect = c.create_rectangle(10, 50, originelwidth, originelheight, fill='black')
  fillrect = c.create_rectangle(10, 50, perwidth, perheight, fill='red')

  c.grid(column=0, row=2)

  root.mainloop()


def vertical(): #heeft nog geen officiele functie
  print("hi")
  structure = 'test'

def horizontal(): #heeft nog geen officiele functie
  print('hi2')
  structure = 'test'



def diskcalculate():
  c = wmi.WMI ()
  for disk in c.Win32_LogicalDisk (DriveType=3):
      # percentage = (int (disk.FreeSpace) / int (disk.Size))
      # print(int(disk.FreeSpace) / int(disk.Size))
      percentage = (1 - (int(disk.FreeSpace) / int(disk.Size)))
      print(1 - (int(disk.FreeSpace) / int(disk.Size)))
      naamschijf = disk.caption
      print (disk.Caption, "%0.2f%% free" % (100.0 * int(disk.FreeSpace) / int(disk.Size)))
      Gui(percentage, naamschijf)
  return percentage, naamschijf

diskcalculate()
