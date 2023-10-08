from tkinter import *

root = Tk()
root.title('CODSOFT TASK-1 CHATBOT')
def send():
    user_input=entry.get() 
    entry.delete(0,END)
    text.config(state=NORMAL)
    text.insert(END,f"\nYou:{user_input}")
    text.config(state=DISABLED)
    if user_input.lower()=='hi':
        response="ChatBot:hello"
    elif user_input.lower()=='hello':
        response="ChatBot:hi"
    elif user_input.lower()=='how are you?':
        response="ChatBot:I am fine, and you?"
    elif user_input.lower()=='i am fine too':
        response="ChatBot:Nice to hear that.. How can i assist you today?"
    elif user_input.lower()=='what can you do':
        response="ChatBot:I can answer questions, provide information, and have general conversations."
    elif user_input.lower()=='bye':
        response="ChatBot:Goodbye! If you have more questions, feel free to ask anytime."
    else:
        response="ChatBot: Sorry, I didn't get it."
    text.config(state=NORMAL)
    text.insert(END,"\n" +response)
    text.config(state=DISABLED)
def set_watermark(event):
    if entry.get()=="Enter a message...":
        entry.delete(0,END)
        entry.config(fg='black')
def clear_watermark(event):
    if entry.get()=="":
        entry.insert(0,"Enter a message...")
        entry.config(fg='grey')
entry=Entry(root,width=80,fg='grey')
entry.insert(0,'Enter a message...')
entry.bind("<FocusIn>",set_watermark)
entry.bind("<FocusOut>",clear_watermark)
entry.grid(row=1, column=0)

send_button=Button(root,text='Send', bg='blue', width=20, command=send)
send_button.grid(row=1,column=1)

text=Text(root,bg='light blue', state=DISABLED)
text.grid(row=0, column=0, columnspan=2)
root.mainloop()