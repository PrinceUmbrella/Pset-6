import string

### DO NOT MODIFY THIS FUNCTION ###
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

### DO NOT MODIFY THIS FUNCTION ###
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

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    #print(story)
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
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
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        #pass #delete this line and replace with your code here
        try:
            
            alpha = string.ascii_lowercase
            alpha_List = []
            cap_alpha = []
            for i in alpha:
                alpha_List.append(i)
                cap_alpha.append(i.upper())   
            
            
            def Encryptt(listt, shift):
                cut_list = listt[-(26-shift):]# cuts everything from behind  
                new_list = listt[:-(26-shift)]# cuts until -shift
                combList = cut_list + new_list
                return(combList)
            
            
            beta_list = Encryptt(alpha_List,shift)  
            delta_list = Encryptt(cap_alpha,shift)
            #print(beta_list)
            #print(delta_list)
            #print(alpha_List)
            shift_guide = dict(zip(alpha_List,beta_list))
            shift_guide2 = dict(zip(cap_alpha,delta_list))
            shift_guide.update(shift_guide2)
            return(shift_guide)
        except IndexError:
            raise Exception("The list cant be shift any thing i < -26 and i>25")

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
        guide = self.build_shift_dict(shift)
        chiper_message = []
        #add test case or error handling
        for i in self.message_text:
            if i in string.ascii_lowercase:
                chiper_message.append(guide[i])
            elif i in string.ascii_uppercase:
                chiper_message.append(guide[i].upper())
                #print(i)
                
            else:
                chiper_message.append(i)
                
        encrypt_message = ''.join(chiper_message)
        
            
        return(encrypt_message)
        

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

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self,text)
        self.shift = shift

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        #pass #delete this line and replace with your code here
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        #pass #delete this line and replace with your code here
        self.encrypting_dict = self.build_shift_dict(self.shift)
        x = self.encrypting_dict.copy()
        return x

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        #pass #delete this line and replace with your code here
        self.message_text_encrypted = self.apply_shift(self.shift)
            
        
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        #pass #delete this line and replace with your code here
        self.shift = shift
        self.build_shift_dict(self.shift)
        self.apply_shift(self.shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        #pass #delete this line and replace with your code here
        Message.__init__(self,text)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are  equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        #pass #delete this line and replace with your code here
        
        self.encrypted_list = self.message_text.split(" ")
        #print(self.encrypted_list)
        self.message_text_copy = self.message_text
        self.get_message_text()
        shift_num = None
        maxium = 0
        for i in range(1,27):
            countt = 0
            
            s = []
            for j in self.encrypted_list:
                self.message_text = j
                word = self.apply_shift((26-i))
                if (is_word(self.get_valid_words(), word)):
                    countt += 1
                    s.append(word)
                    #print(countt)
                    #print(s)
                        
                    if countt > maxium:
                        maxium = countt
                        shift_num = 26-i
                        #print(shift_num)
        if shift_num == None:
            #print(countt)
            #print(s)
            return 1
            #pass
        else:
            self.message_text = self.message_text_copy
            self.message_text_copy = "".join(self.apply_shift(shift_num))
            self.message_text = self.message_text_copy
            self.shift = 26-shift_num
            ree = self.message_text
            re = self.shift
#            x = (self.shift, self.message_text )
            #print (x)
            
            return (re, ree)

##Example test case (PlaintextMessage)
#plaintext = PlaintextMessage('hello', 2)
#print('Expected Output: jgnnq')
#print('Actual Output:', plaintext.get_message_text_encrypted())
#    
##Example test case (CiphertextMessage)
#ciphertext = CiphertextMessage('pm ol ohk hufaopun av zhf, ol dyval pa pu jpwoly, aoha pz, if zv johunpun aol vykly vm aol slaalyz vm aol hswohila, aoha uva h dvyk jvbsk il thkl vba.')
#print('Expected Output:', (7, 'If he had anything to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out.'))
#print('Actual Output:', ciphertext.decrypt_message())
#            
def decrypt_story():
    decrypted = CiphertextMessage(get_story_string())
    print(decrypted.get_message_text())
    print(decrypted.decrypt_message())
    
    #return x
#
print(decrypt_story())