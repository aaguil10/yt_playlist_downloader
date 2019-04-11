from Tkinter import *

def fetch(root, ents, mp3_data):
      entries = [];
      for entry in ents:
            field = entry[0]
            text  = entry[1].get()
            entries.append(text)
      mp3_data.track = unicode(entries[0], "utf-8")
      mp3_data.artist = unicode(entries[1], "utf-8")
      root.destroy()
      

def makeform(root, fields):
      entries = []
      for field in fields:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            row.pack(side=TOP, fill=X, padx=5, pady=5)
            lab.pack(side=LEFT)
            ent.pack(side=RIGHT, expand=YES, fill=X)
            entries.append((field, ent))
      return entries

def showLines(root, fields):
      num_lines = 6
      for field in fields:
            if num_lines == 0:
                  break
            else:
                  num_lines -= 1
            row = Frame(root)
            ent = Entry(row)
            ent.insert(0,field)
            row.pack(side=TOP, fill=X)
            ent.pack(side=RIGHT, expand=YES, fill=X)



def fill_name_artist(info, mp3_data, popup_msg):
      print(info[u'description'])
      root = Tk()

      row = Frame(root)
      lab = Label(row, width=30, text=popup_msg, anchor='w')
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)

      fields = 'Name', 'Artist'
      ents = makeform(root, fields)
      root.bind('<Return>', (lambda event, e=ents: fetch(e)))

      row = Frame(root)
      lab = Label(row, width=5, text="YT title", anchor='w')
      ent = Entry(row)
      ent.insert(0,info[u'title'])
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      
      descr_lines = info[u'description'].splitlines()
      form_line = showLines(root, descr_lines)

      b2 = Button(root, text='Done', command=(lambda: fetch(root, ents, mp3_data)))
      b2.pack(side=LEFT, padx=5, pady=5)
      root.mainloop()
      return mp3_data





