# FASTA-anlyser
Python script to display G, C, T, A content and length of genetic sequence

A really basic script I wrote to analyse a dan sequence provided in text/FASTA format. This script is nothing new as there are countless software and online resources that can do the same thing. However, as an exercise to get my feet wet, this was great. I am writing this retrospectively and as such, plan to add more to it. The ability to incorporate ambiguous nucleotides would also be great.

My overall aim will be to develop a GUI with multiple features for analysing sequences. This would be one module to work with that GUI.

#*****************Script********************************

sequence = input("Enter your sequence here: ")

caps = sequence.upper()
length = len(sequence)

accepted_bases = ('G', 'C', 'T', 'A')

print("Sequence analysed:")
print("Sequence length =",length,"bp")

for bases in accepted_bases:
    count = caps.count(bases)
    content = round(((count/length)*100), 2)
    print(bases, "content is", content, "%")

