#Main Language dictionary
D = {
'Minus':'-',
'Plus':'+',
'ShiftR':'>',
'ShiftL':'<',
'Bracket[':'[',
'Bracket]':']',
'Out':'.',
'In':',',
'NewLine':'\n',
'Whitespace':' '
}

Br = []
MemSize = 16
Skip = False
BrAmount = 0
#Memory array
M = [0]*MemSize

Adr= 0
filename = input("What file to execute?\n: ")
with open(filename,'r') as file:
    prog = file.read()
    #prog.replace('\n',' ') #remove all newline symbols



    pos = -1
    while pos < len(prog) - 1:
        pos +=1
        if prog[pos] in D.values():
            if prog[pos] == D['Bracket]']:
                if len(Br) > 0:
                    if not Skip and M[Adr] > 0:
                        pos = Br[-1] # Go back to start of the loop
                    else: 
                        Br.pop(-1) # pop last element
                        Skip = False

            elif prog[pos] == D['Bracket[']:
                Skip = M[Adr] == 0
                Br.append(pos)

            elif not Skip:
                if prog[pos] == D['Minus']:
                    M[Adr] -= 1
                    if M[Adr] < 0:
                        M[Adr] = 255
                elif prog[pos] == D['Plus']:
                    M[Adr] += 1
                    if M[Adr] > 255:
                        M[Adr] = 0
                elif prog[pos] == D['ShiftL']:
                    if Adr > 0:
                        Adr -= 1
                    else:
                        raise IndexError
                elif prog[pos] == D['ShiftR']:
                    if Adr < MemSize:
                        Adr += 1
                    else:
                        raise IndexError
                elif prog[pos] == D['Out']:
                    print(chr(M[Adr]),end='')
                elif prog[pos] == D['In']:
                    M[Adr] = ord(input()[0])




        else:
            print('Look at this bad symbol!  -->',prog[pos])
            raise KeyError


    print('\n' + '-' * len(str(M)))
    print(M)
    print('-' * len(str(M)))
