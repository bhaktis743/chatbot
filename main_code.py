from tkinter import *
from tkinter import ttk                 
from PIL import Image,ImageTk           #pip install pillow
import script

class ChatBot():
    def __init__(self,root):
        self.root = root                  #open new window
        self.root.title('Chat With Me')     #give name to window
        self.root.geometry('830x700+0+0')     #set size of window

        main_frame= Frame(self.root,bd=5,bg='light blue',width=650)
        main_frame.pack()

        img_Chatbot = Image.open('chat.jpg')
        img_Chatbot = img_Chatbot.resize((200,80),Image.LANCZOS)      
        self.img = ImageTk.PhotoImage(img_Chatbot)

        title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=750,compound=LEFT,image=self.img,
        text='RISE WITH ME',font=('araia',50,'bold'),fg='red',bg='white')
        title_label.pack(side=TOP)

        self.scroll= ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text= Text(main_frame,width=65,height=20,bd=5,relief=RAISED,font=('arial',14),
        yscrollcommand=self.scroll.set)
        self.scroll.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame = Frame(self.root,bd=4,bg='white',width=780)
        btn_frame.pack()

        label = Label(btn_frame,text='Type Something',font=('araia',25,'bold'),fg='red',bg='white')
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry= ttk.Entry(btn_frame,width=30,font=('times new roman',17,'bold'))
        self.entry.grid(row=0,column=1,padx=5,sticky=W)

        self.send= Button(btn_frame,text='send>>',command=self.send,font=('araia',20,'bold'),fg='black',bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)
        
        self.clear= Button(btn_frame,text='CLEAR',font=('araia',20,'bold'),fg='white',bg='black')
        self.clear.grid(row=1,column=0,padx=5,sticky=W)  

        self.msg = " "
        self.label_1 = Label(btn_frame,text=self.msg,font=('arial',14,'bold'),fg='red',bg='white')
        self.label_1.grid(row=1,column=1,padx=5,sticky=W)

    def send(self):
        user_input = self.entry.get()
        send= '\t\t'+'You: '+ user_input
        self.text.insert(END,'\n'+ send) 

        if user_input == "":
            self.msg = 'Please enter some input'
            self.label_1.config(text=self.msg,fg='red')
        
        else:
            self.msg= ""
            self.label_1.config(text=self.msg,fg='red')

        if "hello" in user_input.lower() or "hi" in user_input.lower() or "hey" in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.greet() )

        if "college information"in user_input.lower() or "information" in user_input.lower() or "college" in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.college_info())
        
        if "stream"in user_input.lower() or "streams" in user_input.lower() or "courses" in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.streams())
            
        if "engineering"in user_input.lower() or "engi." in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.Engineering())

        if "science"in user_input.lower() or "sci." in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.Science())

        if "arts"in user_input.lower() or "art" in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.Arts())

        if "commerse"in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.Commerse())

        if "contact"in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.contact())

        if "admission"in user_input.lower() or "admission process"in user_input.lower() or "application process"in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.admission())

        if "address"in user_input.lower() or 'location' in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.address())

        if "bye"in user_input.lower() or 'good bye' in user_input.lower():
            self.text.insert(END,'\n\n'+f'Shiksha : ' + script.goodbye())


if __name__ == '__main__':
    root=Tk()
    obj= ChatBot(root)
    root.mainloop()

