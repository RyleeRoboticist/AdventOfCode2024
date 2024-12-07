import tkinter
import tkinter.ttk

from tkinter.filedialog import askopenfile

root = tkinter.Tk()
root.geometry('200x100')
 
def PromptOpenFile():
    file = askopenfile(mode='r', filetypes=[('Text Files','*.txt')])

    if file is not None:
        return False

    return file

def ConvertFileTo2DArray(file):
    returnArray = []
    for line in file:
        returnArray.append(line)

    return returnArray

def ConvertFileToBigAssString(file):
    returnString = ""
    for line in file:
        returnString += line

    return returnString