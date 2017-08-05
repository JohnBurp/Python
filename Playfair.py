import math
w = 5
h = 5
playfair = [[0 for i in range(w)] for x in range(h)]
letter = 97
unvalidcharacters = []
characters = []
letpos = []
cipher = []
appendable = True
appendable2 = True

cipherold = input("Please enter your cipher")
key2 = input("Please enter your key")

def makePlayfair(key):

#remove any letters that repeat
    unvalidcharacters.append(ord(key[0]))
    for s in range(1, len(key)):
        for f in range(len(unvalidcharacters)):
            if ord(key[s]) != unvalidcharacters[f]:
                appendable = True
            else:
                appendable = False
                break
        if appendable:
            unvalidcharacters.append(ord(key[s]))
    for z in range(len(unvalidcharacters)):
        print(chr(unvalidcharacters[z]), end = "")

        
#remove extrannious characters to conform to letter table
    for jj in range(len(unvalidcharacters)):
        if unvalidcharacters[jj] > 96 and unvalidcharacters[jj] < 123:
            characters.append(unvalidcharacters[jj])


#find rows and collumns filled to, then append letters not already used to the rest of that row, unless the row is filled
    for ko in range(len(characters) % 5, 5):
        for uo in range(26):
            for so in range(5):
                for lo in range(5):
                    if (uo + 97) not in characters:
                        characters.append(97 + uo)


# remove all v and print for debug
    if len(characters) > 25:
        characters.remove(ord("v"))



# insert key into the 2d array at intervals of 5
    b = 0
    for c in range(5):
        for m in range(5):
            if b < (len(characters)):
                playfair[c][m] = characters[b]
                b += 1
        


# print the 2d array
    for g in range(5):
        print("")
        for o in range(5):
            print(chr(playfair[g][o]), end = "")
    print("")

def finishPlayfair(cipherold):
    #remove extrannious characters from the cipher, so that the algorithm does not improperly make an even cipher odd
    for oo in range(len(cipherold)):
        if ord(cipherold[oo]) > 96 and ord(cipherold[oo]) < 123:
            cipher.append(cipherold[oo])


    #make sure the cipher is an even number
    if len(cipher) % 2 != 0:
        cipher.append("x")

    #break the cipher into pairs of two letters, then store their numerical value into variables
    for d in range(1, len(cipher), 2):
        for y in range(5):
            for g in range(5):
                if ord(cipher[d - 1]) == playfair[y][g]:
                    let1 = ord(cipher[d - 1])
                elif ord(cipher[d]) == playfair[y][g]:
                    let2 = ord(cipher[d])


    #Find the position of the cipher's pairs of letters in the 2d array
        for gg in range(5):
            for r in range(5):
                if playfair[gg][r] == let1:
                    letpos.append(gg)
                    letpos.append(r)
        for hh in range(5):
            for kk in range(5):
                if playfair[hh][kk] == let2:
                    letpos.append(hh)
                    letpos.append(kk)


    #Using the positions of the pairs, find the position of the relative location and print the characters
        if letpos[1] == letpos[3]:
            if letpos[0] != 4 and letpos[2] != 4:
                print(chr(playfair[letpos[0] + 1][letpos[1]]), end = "")
                print(chr(playfair[letpos[2] + 1][letpos[3]]), end = "")
            elif letpos[0] == 4:
                print(chr(playfair[0][letpos[1]]), end = "")
                print(chr(playfair[letpos[2] + 1][letpos[3]]), end = "")
            elif letpos[3] == 4:
                print(chr(playfair[0][letpos[3]]), end = "")
                print(chr(playfair[letpos[0] + 1][letpos[1]]), end = "")
        elif letpos[0] == letpos[2]:
            if letpos[1] != 4 and letpos[3] != 4:
                print(chr(playfair[letpos[0]][letpos[1] + 1]), end = "")
                print(chr(playfair[letpos[2]][letpos[3] + 1]), end = "")
            elif letpos[1] == 4:
                print(chr(playfair[letpos[0]][0]), end = "")
                print(chr(playfair[letpos[2]][letpos[3] + 1]), end = "")
            elif letpos[2] == 4:
                print(chr(playfair[letpos[2]][0]), end = "")
                print(chr(playfair[letpos[0]][letpos[1] + 1]), end = "")
        else:
            print(chr(playfair[letpos[0]][letpos[3]]), end = "")
            print(chr(playfair[letpos[2]][letpos[1]]), end = "")



    #clear the list of letter coordinates, so that the next pair can come through
        for ff in range(len(letpos)):
                letpos.pop()

makePlayfair(key2)
finishPlayfair(cipherold)

#I never made a decrypt function for this, but I imagine it would not be difficult.

            
                
        
        
                


