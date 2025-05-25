import interface as i
from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk, Image

class GUI():
    def __init__(self):
        #Window
        self.app = Tk()
        self.app.title("BDPlanner")
        self.app.geometry("1200x900")
        self.app["bg"] = "#443b39"

        #Style
        self.style = Style()
        self.style.configure("W.TButton", 
                             background="#443b39",
                             foreground="#443b39"
                             )
        self.style.configure("BW.TFrame", 
                             background="#443b39",
                             foreground="#443b39"
                             )

        #Frames
        self.char_list_frame = Frame(self.app, style="BW.TFrame")
        self.char_list_frame.grid(row=0, column=0, sticky=NSEW)
        self.char_info_frame = Frame(self.app, style="BW.TFrame")
        self.char_info_frame.grid(row=0, column=0, sticky=NSEW)

        #Load characters
        self.char_list = self.character_dict_to_list()

        #Show Character Frame
        self.char_buttons = self.list_face_characters(self.char_list_frame)
        self.char_list_frame.tkraise()
        
        #Start app
        mainloop()

    def list_face_characters(self, win):
        d = self.get_character_list()
        l = []
        self.img = []
        r = 0
        c = 1
        
        for i in range(len(self.char_list)):
            path = f".img/face/{d[self.char_list[i]]['face_img']}"
            self.img.append(PhotoImage(file = path))
            Button(
                win, 
                text=self.char_list[i], 
                style="BW.TButton", 
                image=self.img[i], 
                command= lambda i = i: self.open_character_info(self.char_list[i])
                ).grid(row=r, column=c-1, sticky=W, pady=2)
            if(c % 4 == 0):
                c = 0
                r += 1
            c += 1
        return l


    def show_char_info(self, char):
        self.clear_frame(self.char_info_frame)
        Button(
            self.char_info_frame,
            text="Back",
            command= lambda: self.char_list_frame.tkraise()
        ).grid(row=0, column=0, sticky=W, pady=2)
        
        self.name_label = Label(self.char_info_frame,
            text=char
        ).grid(row=0, column=0, sticky=W, pady=2)

    def clear_frame(self, frame):
        for widget in frame.winfo_children():
            widget.destroy()

    def open_character_info(self, char):
        self.show_char_info(char)
        self.char_info_frame.tkraise()
        
    def get_character_list(self):
        return i.get_characters()

    def character_dict_to_list(self):
        return list(self.get_character_list().keys())
GUI()