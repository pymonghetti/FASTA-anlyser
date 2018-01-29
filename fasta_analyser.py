sequence = input("Enter your sequence here: ") #User input

caps = sequence.upper() #uppercase sequence - FASTA files could potentially be mixed upper and lower.
length = len(sequence)

accepted_bases = ('G', 'C', 'T', 'A') #no ambiguity codes included yet

print("Sequence analysed:")
print("Sequence length =",length,"bp")

for bases in accepted_bases:
    count = caps.count(bases)
    content = round(((count/length)*100), 2)
    print(bases, "content is", content, "%")
