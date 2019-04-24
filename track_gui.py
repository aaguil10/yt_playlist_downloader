from Tkinter import *

def fetch(root, ents, form_dict):
      entries = [];
      for entry in ents:
            field = entry[0]
            text  = entry[1].get()
            form_dict[field] = unicode(text, "utf-8")
      root.destroy()
      

def makeform(root, form_dict):
      entries = []
      print(form_dict.keys()[::-1])
      for field in form_dict.keys()[::-1]:
            row = Frame(root)
            lab = Label(row, width=15, text=field, anchor='w')
            ent = Entry(row)
            ent.insert(0, form_dict[field])
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



def buildPopUp(form_dict):
      root = Tk()

      row = Frame(root)
      lab = Label(row, width=30, text=form_dict['msg'], anchor='w')
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)

      form_dict.pop("msg")
      ents = makeform(root, form_dict)
      root.bind('<Return>', (lambda event, e=ents: fetch(e)))

      b2 = Button(root, text='Done', command=(lambda: fetch(root, ents, form_dict)))
      b2.pack(side=LEFT, padx=5, pady=5)
      root.mainloop()
      return form_dict





