import interface as i
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

class GUI():
    def __init__(self):
        #Window
        self.width = 1200
        self.height = 900
        self.app = Tk()
        self.app.title("BDPlanner")
        self.app.geometry(f"{self.width}x{self.height}")
        self.app["bg"] = "#443b39"
        self.app.resizable(False, False)

        #Style
        self.style = Style()
        self.style.configure("W.TButton",
                             background="#443b39",
                             foreground="#443b39"
                             )
        self.style.configure("BW.TFrame",
                             background="#443b39",
                             foreground="#443b39",
                                highlightbackground="red", 
                                highlightthickness=2
                             )
        self.style.configure("BW.TCanvas",
                             background="#443b39",
                             foreground="#443b39"
                             )

        #Frames
        self.main_frame = Frame(
            self.app, 
            style="BW.TFrame",
            width=self.width, 
            height=self.height,
            )
        self.main_frame.grid(row=0, column=0)



        # self.char_info_frame = Frame(self.canvas, style="BW.TFrame")
        # self.char_info_frame.grid(row=0, column=0, sticky=NSEW)




        #Load characters
        self.char_list = self.character_dict_to_list()



        #Show Character Frame
        self.list_face_characters()
        

        #Start app
        mainloop()

    def list_face_characters(self):
        self.clear_frame(self.main_frame)

        #Canvas
        self.canvas = Canvas(
            self.main_frame, 
            width=self.width, 
            height=self.height, 
            background="#443b39",
            highlightbackground="blue", 
            highlightthickness=2
            )
        self.canvas.grid(row=0, column=0)

        #Frame
        self.char_list_frame = Frame(
            self.canvas, 
            style="BW.TFrame"
            )
        self.char_list_frame.grid(row=0, column=0, sticky=NS)
    
        

        d = self.get_character_list()
        self.img = []

        r = 1
        c = 1


        Button(
            self.char_list_frame,
            text="ID",
            style="BW.TButton",
            command=self.sort_by_id
            ).grid(row=0, 
                column=0,
                #columnspan=2, 
                #sticky=W, 
                pady=2)
        
        Button(
            self.char_list_frame,
            text="Name",
            style="BW.TButton",
            command=self.sort_by_name
            ).grid(row=0, 
                   column=1, 
                   #sticky=W, 
                   pady=2)
        
        Button(
            self.char_list_frame,
            text="Type",
            style="BW.TButton",
            command=self.sort_by_type
            ).grid(row=0, 
                   column=2, 
                   #sticky=W, 
                   pady=2)

        for i in range(len(self.char_list)):
            path = f".img/face/{d[self.char_list[i]]['face_img']}"
            self.img.append(PhotoImage(file = path))

            Button(
                self.char_list_frame,
                text=self.char_list[i],
                style="BW.TButton",
                image=self.img[i],
                command= lambda i = i: self.open_character_info(self.char_list[i])
                ).grid(row=r, column=c-1, sticky=W, pady=2)

            if(c % 4 == 0):
                c = 0
                r += 1
            c += 1

        scrollbar = Scrollbar(
            self.main_frame, 
            command=self.canvas.yview
            )


        self.char_list_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
            scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.char_list_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)


        scrollbar.grid(row=0, column=0, sticky="NES", padx=2)

        self.char_list_frame.tkraise()

    def on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    def sort_by_id(self):
        self.char_list = i.sort_by_id()
        self.list_face_characters()

    def sort_by_name(self):
        self.char_list = i.sort_by_name(self.char_list)
        self.list_face_characters()

    def sort_by_type(self):
        self.char_list = i.sort_by_type()
        self.list_face_characters()

    def filter_by_type():
        pass

    def show_char_info(self, char):
        self.clear_frame(self.main_frame)
        cur_char = i.get_character(char)

        #Canvas
        self.canvas = Canvas(
            self.main_frame, 
            width=self.width, 
            height=self.height, 
            background="#443b39",
            highlightbackground="blue", 
            highlightthickness=2
            )

        self.canvas.grid(
            row=0, 
            column=0)
        
        self.char_info_frame = Frame(
            self.canvas, 
            style="BW.TFrame"
            )
        
        

        self.char_info_frame.grid(
            row=0, 
            column=0, 
            sticky=NSEW)
        
        Button(
            self.char_info_frame,
            text="Back",
            command= self.list_face_characters
        ).grid(
            row=0, 
            column=0, 
            sticky=W, 
            pady=2)

        self.name_label = Label(
            self.char_info_frame,
            text=char
        ).grid(
            row=1, 
            column=0, 
            sticky=W, 
            pady=2)
        c = 2
        for item in cur_char.keys():

            Label(
                self.char_info_frame,
                text=f"{item}: {cur_char[item]}"
            ).grid(row=c, column=0, sticky=W, pady=2)
            c+=1


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

    def get_char_id(self, char):
       return i.get_char_id(char)
GUI()