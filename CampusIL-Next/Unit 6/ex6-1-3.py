__author__ = "Omer" 


from email.mime import image
import tkinter as tk



def main():
    root = tk.Tk()
    message = tk.Label(root, text = "What\'s my favorite video?")
    message.pack()
    button = tk.Button(root, text = "Click here to find out", command = show_image(root))
    button.pack()
    root.mainloop()

def show_image(my_root):
    print ("abd")

    
if __name__ == "__main__":
    main()