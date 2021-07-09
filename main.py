from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3


engine=pyttsx3.init() #creating of engine class

voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)

#########funcpart
def search():
    data=json.load(open("data.json"))
    word=enterwordentry.get()
    word=word.lower()
    print(word)
    if word in data:
        meaning=data[word]
        print(meaning)
        textarea.delete(1.0,END)
        for item in meaning:
            textarea.insert(END,u'\u2022'+item+'\n\n')

    elif len(get_close_matches(word,data.keys()))>0:
        close_match=get_close_matches(word,data.keys())[0]
        res=messagebox.askyesno("Confirm",f'Did you mean {close_match} instead?')
        print(res)
        if res==True:
            enterwordentry.delete(0,END)
            enterwordentry.insert(END,close_match)
            meaning=data[close_match]

            textarea.delete(1.0,END)
            for item in meaning:
                textarea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error','The word doesnot exist,Please double check it. ')
            enterwordentry.delete(0,END)
            textarea.delete(1.0,END)

    else:
        messagebox.showinfo('Information','The word doesnot exist.')
        enterwordentry.delete(0,END)
        textarea.delete(1.0,END)
def clear():
    enterwordentry.delete(0,END)
    textarea.delete(1.0,END)


def iexit():
    res=messagebox.askyesno('Confirm','Do you want to exit?')
    if res==True:
        root.destroy()

    else:
        pass
def wordaudio():
    engine.say(enterwordentry.get())
    engine.runAndWait()

def meaningaudio():
    engine.say(textarea.get(1.0,END))
    engine.runAndWait()()


















root=Tk()    #creating window

root.geometry("1000x626+100+30")                 #Giving width and hight to the window
root.title("Speaking Word Book By Nimra~Ayesha~Asra")       #Giving title to the window here

root.resizable(0,0)                                          #Disabling maximize button

bgimage=PhotoImage(file='bg.png')                             #Importing image and creating object name
bgLabel=Label(root,image=bgimage)                              #creating label, placing label in the root, pass bg image in image argument
bgLabel.place(x=0,y=0)                                         #giving position to image






bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
enterwordLabel = Label(root, text='Enter Word', font=('castellar', 30, 'bold'), fg='red3', bg='whitesmoke')  #creating label to add text,  adding label to root window, then adding text,then providing font,foreground keyword argument for color, bg argumnt for backgroud color of label
enterwordLabel.place(x=530, y=20)    #giving distance where the label will be shown

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=6, relief=GROOVE, justify=CENTER) #Creating entry field placing in root window,giving font,justify for the cursor,bd for border,releif for style the border
enterwordentry.place(x=510, y=80)            #giving path where to place this entry filed


searchimage = PhotoImage(file='seo (1).png')  #Before adding images we import the iamge here
searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',command=search) #Creating a button to search,placing button into root window,add image,bd=0 for remove border,bg for background color,cursor argument for convert arrow into hand,activebackground is: the color when you click on the button
searchButton.place(x=620, y=150)    #giving path where to place this search button

root.resizable(0,0)
micimage=PhotoImage(file='mic(4).png')  #importing mic image
micButton=Button(root,image=micimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=wordaudio) #creating mic button, adding it to root window,adding image,bd for remove border, bg for background color,activebg for chnging color when click,curser for converting arrow to hand,
micButton.place(x=710,y=153) #placing button where to shown


meaninglabel=Label(root,text='Meaning',font=('castellar',29,'bold'),fg='red3',bg='whitesmoke') #creating label for text Meaning
meaninglabel.place(x=580,y=240) #where to place

textarea=Text(root,width=34,height=8,font=('arial',18,'bold'),bd=8,relief=GROOVE) #text area where meaning will be shown,placing into root window,giving height and width,giving font,bd for border,releif for styling the border
textarea.place(x=460,y=300) #where to place this text area

audioimage=PhotoImage(file='mic(4).png') #importing audio image
audioButton=Button(root,image=audioimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=meaningaudio) #creating audio button
audioButton.place(x=530,y=555) #where to place this audio button

clearimage=PhotoImage(file='x.png') #importing clear image
clearButton=Button(root,image=clearimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=clear) #creating clear button
clearButton.place(x=660,y=555) #where to place this clear button

exitimage=PhotoImage(file='exit.png') #importing exit image
exitButton=Button(root,image=exitimage,bd=0,bg='whitesmoke',activebackground='whitesmoke',cursor='hand2',command=iexit) #creating exit button
exitButton.place(x=790,y=555) #where to place this exit button

def enter_function(event):
    searchButton.invoke()

root.bind('<Return>',enter_function)


root.mainloop()

