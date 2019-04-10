# import Tkinter as tk
from Tkinter import *
# from Mp3Data import Mp3Data


# class Mp3InfoWindow:
#    def __init__(self, mp3_data, popup_msg):
#       self.root = Tk()
#       self.mp3_data = mp3_data

#       Label(self.root, text=popup_msg).grid(row=0)
#       Label(self.root, text="Name").grid(row=1)
#       Label(self.root, text="Artist").grid(row=2)
#       Label(self.root, text="Album").grid(row=3)
#       Label(self.root, text="Albumart URL").grid(row=4)

#       e1 = Entry(self.root)
#       e2 = Entry(self.root)
#       e3 = Entry(self.root)
#       e4 = Entry(self.root)
#       e5 = Entry(self.root)
#       e6 = Entry(self.root)

#       e1.grid(row=1, column=1)
#       e2.grid(row=2, column=1)
#       e3.grid(row=3, column=1)
#       e4.grid(row=4, column=1)
#       e5.grid(row=5, column=0)
#       e6.grid(row=5, column=1)

#       e1.insert(0, mp3_data.track)
#       e2.insert(1, mp3_data.artist)
#       e3.insert(2, mp3_data.album)
#       e4.insert(3, mp3_data.albumart_url)

#       self.e1 = e1
#       self.e2 = e2
#       self.e3 = e3
#       self.e4 = e4
#       self.e5 = e5
#       self.e6 = e6

#       button = Button(self.e5, text='Continue', command=self.quit)
#       button.pack()

#       button2 = Button(self.e6, text='Skip', command=self.skip)
#       button2.pack()

#       print("Please enter info manually")
#       self.root.mainloop()

#    def quit(self):
#       self.mp3_data.track = unicode(self.e1.get())
#       self.mp3_data.artist = unicode(self.e2.get())
#       self.mp3_data.album = unicode(self.e3.get())
#       self.mp3_data.albumart_url = unicode(self.e4.get())
#       self.root.destroy()

#    def skip(self):
#       self.mp3_data.track = u''
#       self.mp3_data.artist = u''
#       self.mp3_data.album = u''
#       self.mp3_data.albumart_url = u''
#       self.root.destroy()

def fetch(root, ents, mp3_data):
      print("Called fetch!")
      entries = [];
      for entry in ents:
            field = entry[0]
            text  = entry[1].get()
            entries.append(text)
      mp3_data.track = unicode(entries[0], "utf-8")
      mp3_data.artist = unicode(entries[1], "utf-8")
      root.quit
      root.destroy()
      

def makeform(root, fields, popup_msg):
      row = Frame(root)
      lab = Label(row, width=30, text=popup_msg, anchor='w')
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      entries = []
      for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
      row = Frame(root)
      lab = Label(row, width=15, text="YT title", anchor='w')
      ent = Entry(row)
      ent.insert(0,"This is a title!")
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
      return entries


def fill_name_artist(mp3_data, popup_msg):
      root = Tk()
      fields = 'Name', 'Artist'
      ents = makeform(root, fields, popup_msg)
      root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
      # b1 = Button(root, text='Show',
      #     command=(lambda e=ents: fetch(e)))
      # b1.pack(side=LEFT, padx=5, pady=5)
      b2 = Button(root, text='Quit', command=(lambda: fetch(root, ents, mp3_data)))
      b2.pack(side=LEFT, padx=5, pady=5)
      root.mainloop()
      return mp3_data





