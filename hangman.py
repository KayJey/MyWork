import random 
print(" 								HANGMAN GAME ")
#this program is a game where the user has to guess the word from the given letter 
l = ["hello" , "candy" , "balls" , "fishs" , "dolls" ,"milks" ,"sunny"] #this is our word library 
word = random.randint(0,4) #randoly pick a word from library 
que = l[word] #the randomised word

listofletter = [ i for i in que]
index = list (range(0,7))
missing = (1,3)
missingdict = dict(zip( missing , ("_" , "_")))
assin1 = dict( zip (index , listofletter)) #the dict of letters corresponing to their index 
assin2 = { key : assin1[key] for key in missing }  #the dict of letters that are  missing , corresponding to their index
aasin3 = { key : assin1[key] for key in [0,2,4] } 
aasin3.update(missingdict) #the dict of letters that are  not missing , corresponding to their index
temp1 = sorted(aasin3)

print ( " 					you have to guess this word in 10 chances")
w=""
for i in temp1 :
	w = w + (aasin3[temp1[i]])
print(f"					{w}")



for i in range(0,9):
	print(f"Attempt {i+1} ................................................................................................................")
	inp = input("					 Enter ur guess: ")


	if inp in assin2.values() :
		print(" right guess !!!")
		for j in assin2.keys():
			if assin2[j] == inp :
				n = j
		inp_letter = inp
		inp_index = n
		assin2.pop(inp_index) 
		aasin3[inp_index] = inp_letter
		temp = sorted(aasin3)
		w=""
		for i in temp :
			w = w + (aasin3[temp[i]])
		print(f"					{w}")

		if w== que :
			break

	else :
		print( " wrong guess!!!!")

if w == que :
	print( "							C O N G R A T S  Y O U  W O N   :) ")
else :
	print( " 							O O P S  Y O U  L O S T  :(  ")

