from tkinter import *

root = Tk()
root.title("FASTA analyser")
topframe = Frame(root)

MH_numbers_label = Label(root, text="Copy and paste FASTA sequence here:")
MH_numbers_label.pack(padx=2, pady=2)

MH_number_entry = Entry(root)
MH_number_entry.pack(padx=2, pady=2)

button1 = Button(root, text="Find sequences", bg="lightgreen")
button1.pack(padx=2, pady=2)



#sequence = input("Enter your sequence here: ") #User input

#caps = sequence.upper() #uppercase sequence - FASTA files could potentially be mixed upper and lower.
#length = len(sequence)

#accepted_bases = ('G', 'C', 'T', 'A') #no ambiguity codes included yet

#print("Sequence analysed:")
#print("Sequence length =",length,"bp")

#for bases in accepted_bases:
    #count = caps.count(bases)
    #content = round(((count/length)*100), 2)
    #print(bases, "content is", content, "%")

root.mainloop()