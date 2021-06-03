import tkinter as tk
import random
import time

List = [["This test is going to place me at the right level"],
       ["My favourite programming will always be python"],
       ["This is a test line"],
       ["The knight killed our king, we want revenge"]]



class Display(tk.Tk):
    def __init__(self,root):
        (tk.Tk).__init__(self)
        self.root = root
    
    #main Game part
    def game(self):
        #Main window part
        root.title("Typing Test")
        root.geometry("640x452")
        root.configure(background = "black")

        #Title Label part
        self.Title_Label = tk.Label(root, text = "Typing Speed Test", bd= 1, width = 30, height = 2, relief= "solid")
        self.Title_Label.pack(pady = 10, padx =10)
        self.Title_Label.configure(background = "black", fg = "yellow",font=("Courier",30))

        #Text to be entered part 
        self.String_Label = tk.Label(root, text = self.get_string(), bd=1, width = 70, height = 6, relief= "solid")
        self.String_Label.pack(pady = 10, padx =10)
        self.String_Label.configure(background = "black", fg = "white",font=("Courier",15))
        
        #Entry Widget Part
        self.v1 = tk.StringVar()

        self.Entry_Widget = tk.Entry(root, width = 70, textvariable = self.v1)
        self.Entry_Widget.pack(pady = 10, padx =10)
        self.Entry_Widget.configure(background = "black", fg = "white",font=("Courier",15))

        self.v1.trace_add('write', self.check())
        #not sure what it does
        #root.bind('<Return>', self.compare())

    
    def check(self, *args):
        #temp = self.v1.get()
        print("{} this is first print".format(self.v1.get()))
        #temp = len(temp)
        #print("{} this is second print".format(temp))
        #if temp > 0 and temp < 2:
            #self.start()
            #print("worked")

    #function to start the timer
    def start(self):
        self.start_time = time.time()

    #function to stop the timer
    def stop(self):
        self.end_time = time.time() - self.start_time
        print(self.end_time)

    def compare(self):
        self.Label_After_Entry = tk.Label(root,text="It worked", width = 70, height = 10)
        self.Label_After_Entry.pack()
        
    #Gets the string from the 2D List above    
    def get_string(self):
        String = random.choice(List)
        String = str(String)
        String = String.replace("[","")
        String = String.replace("]","")
        String = String.replace("'","")
        return String



if __name__ == "__main__":
    root = tk.Tk()
    Display(root).game()
    root.mainloop()
