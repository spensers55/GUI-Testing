import tkinter          # TkInter is a framework for building GUIs in python
import os

def main():
    scene = tkinter.Tk()    # how to do this from tutorialspoint.com

    def quitButton():
        scene.destroy() # closes window
    

    def readIn(fileName):
        fullList = []
        File = open(fileName)
        line = File.readline()
        listEntry = ""
        for i in line:
            if(i != "#"):
                listEntry = listEntry + i
            else:
                fullList.append(listEntry)
                listEntry = ""
        print(fullList)


    tkinter.Label(scene, text="Read which file?").grid(row=0,column=0) # heading label

    folderIterator = os.scandir("Testing Files")    # scanning directory for filenames
    r = 1
    for files in folderIterator:
        tkinter.Label(scene, text=files).grid(row = r, column = 0) # prints text as a label in the grid
        # vvv creates a button that calls the ReadFile function
        tkinter.Button(scene, text = "Choose this file", command = lambda files=files: readIn(files)).grid(row = r, column = 1)
        r = r+1
        # quit button here vvv
    tkinter.Button(scene, text = "Quit", command = lambda : quitButton()).grid(row = r+1, column = 0)


    scene.mainloop()


main()