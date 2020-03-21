import wmi
from tkinter import *

from PIL import Image, ImageTk
import turtle




def Gui(percentage, naamschijf):
  root = Tk()
  root.geometry('300x300')

  c = Canvas(root, height=250, width=300, bg="white")

  originelheight = 100
  originelwidth = 250
  perwidth = originelwidth * percentage
  perheight = originelheight

  lbl = Label(root, text=naamschijf + " "+ str( (int(percentage * 100))) + "% used")

  lbl.grid(column=0, row=1)
  # x1, (l) y1,(u) x2, (r) y2 (d)
  rect = c.create_rectangle(10, 50, originelwidth, originelheight, fill='black')
  fillrect = c.create_rectangle(10, 50, perwidth, perheight, fill='red')

  c.grid(column=0, row=2)

  root.mainloop()


def vertical():
  print("hi")
  structure = 'test'

def horizontal():
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