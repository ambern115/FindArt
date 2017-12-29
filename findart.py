#This program takes one imput, a spotify song link, finds it's
#corresponding album art, the saves it in my album art folder

from tkinter import *
import urllib.request
import webbrowser
import os      #needed for saving to a specific place

def stringIsLink(a_string):
    link = "https://open.spotify.com/track/"
    if link in a_string:
        return True
    return False

def findArt():
    songlink = enter.get()
    enter.delete(0, END)

    if (len(songlink) != 53) or (stringIsLink(songlink)==False):
        status_label.config(text="Invalid Input")
        print("Invalid Input")
    else:
        try:
            page = urllib.request.urlopen(songlink)
            page = page.read().decode("utf-8")
            text = str(page.split("\n"))
            artlink = ""  

            #searches for the image link
            if "https://i.scdn.co/image/" in text:
                start = text.find("https://i.scdn.co/image/")
                end = (text[start:]).find('"')+start
                artlink = text[start:end]

                #saves the file
                filename = artlink.split('/')[-1]
                #If the art was already saved
                if os.path.exists('C:/Users/Amber2/Pictures/Song Art/'+filename+".jpg"):
                    status_label.config(text="You already saved this art. File name copied to clipboard.")
                    master.clipboard_append(filename+".jpg")
                else:
                    try:
                        urllib.request.urlretrieve(artlink, 'C:/Users/Amber2/Pictures/Song Art/'+filename+".jpg")
                        #checks to make sure it saved
                        if os.path.exists('C:/Users/Amber2/Pictures/Song Art/'+filename+".jpg"):
                            status_label.config(text="Success. File name copied to clipboard.")
                            master.clipboard_append(filename+".jpg")
                        else:
                            status_label.config(text="Failed to save album art")
                    except PermissionError:
                        status_label.config(text="You already saved this art")
            else:
                status_label.config(text="Invalid input, or broken link")
        except:
            status_label.config(text="Invalid input, or broken link")    
        
        #webbrowser.open(artlink)

def clipboardSearch():
    data = master.clipboard_get()
    if isinstance(data, str):
        enter.insert(0,data)
        findArt()
    else:
        status_label.config(text="Clipboard data invalid (must be only text)")

master = Tk()
master.title("Spotify Album Art Saver")
status_text = " "
Label(master, text="Spotify Link:").grid(row=0)

enter = Entry(master, width=100)
enter.grid(row=0, column=1)

Button(master, text="Go", command=findArt).grid(row=0, column=2, sticky=W)
Button(master, text="Go Directly From Clipboard", command=clipboardSearch).grid(row=1, column=1)


#img1 = PhotoImage(Image.open("sampleImg1.jpg"))
#img2 = PhotoImage(file="sampleImg2.jpg")
#img3 = PhotoImage(file="sampleImg3.jpg")
#Frame1 = Frame(master, bg="red")
#Frame1.grid(row=4, column=0)                           
#Label(Frame1, image=img1).grid(row=0, column=0)

status_label = Label(master, text=status_text)
status_label.grid(row=2, column=1, sticky=N, pady=15)
mainloop()

#while True:
#    songlink = input("Song URL:")
#    findArt(songlink)


#needed so python can view the source code of the webpage
    #user_agent = "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
    #headers = {'User-Agent' : user_agent }
    
    


    
