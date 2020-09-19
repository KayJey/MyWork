  
''' this prgram performs Caesers Chiper , encrypting the given text with a given shift number '''


import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation
    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise
    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):

    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text


    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        has 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26
        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        Ulist = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
        num = list(range(1,27))
        Llist = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
        udict = { Ulist[i] : num[i] for i in range(0,26)}
        ldict = { Llist[i] : num[i] for i in range(0,26)}

        def count(n , shift) :
            newindex = n + shift 
            if newindex > 26 :
                newindex =  newindex - 26
            return newindex

        def newchar(c, shift):
            if c.islower():
                oldindex = ldict[c]
                newindex = count(oldindex , shift)
                return  Llist[newindex-1]
            elif c.isupper():
                oldindex = udict[c]
                newindex = count(oldindex , shift)
                return  Ulist[newindex-1]
            else :
                return c       

        ULlist = Ulist + Llist
        shift_dict = {i : newchar(i , shift) for i in ULlist}
        return shift_dict

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26
        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        dict_ = Message.build_shift_dict(self, shift)
        result = ""
        for i in self.message_text :
            if i in dict_.keys():
                result += dict_[i]
            else :
                result += i
        
        return result



class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message
        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)
        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        d = self.encrypting_dict.copy()

        return d



    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        d = ""+ self.message_text_encrypted 

        return d
        
        

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26
        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text
        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self , text)
        
        

    def decrypt_message(self):
        '''
        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        
        returnlist = []
        truecount = 0
        tcountlist = []
        for count in range ( 0 , 26):
            t = Message.apply_shift(self, count)
            returnlist.append(t)
        
        

        for msg in range( 0 ,len(returnlist)):
            msgwordlist = returnlist[msg].split(" ")
            truecount = 0
            for word in msgwordlist :
                if (is_word(self.valid_words, word)):

                    truecount+= 1
            tcountlist.append(truecount)
        maxi = max(tcountlist)
        indexi = tcountlist.index(maxi)
         
        decryttext = Message.apply_shift(self, indexi)

        return( ((26 - indexi) , decryttext))


        

code = input('Enter the text u want to encrypt:')
shit = int(input('enter the shift:'))
plaintext = PlaintextMessage(code, shit)
print('encrypted mesaage:', plaintext.get_message_text_encrypted())


