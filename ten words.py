import matplotlib.pyplot as plt

def count_elements(input_list):
    count = {}
     
    for element in input_list:
        if element in count:        
            count[element] += 1 
        else:
            count[element] = 1 
    return count

def get_file_txt(filename):
    txt = open (filename, 'r').read() #read file
    
    txt = txt.lower() #make everything lower case so all common words can be removed (e.g. The and the)
    
    symbols = ['\n','*',',','.','(',')','[',']','_','-','\ufeff','&','!','?','"',':','0','1','2','3','4','5','6','7','8','9'] 
    
    for n in range (len(symbols)): #getting rid of the irrelevent symbols in the txt file
        if symbols[n] in txt:
            txt = txt.replace(symbols[n],'')
    
    return txt

def get_word_count(text):
    txt = text.split(' ')
    
    count = {}
     
    for element in txt:
        if element in count:        
            count[element] += 1 
        else:
            count[element] = 1 
    return count

common_words= ['a','an','but','the','of','and','in','is','are','was','were','that','there','this','for','to','as','it','with','not','he','she','or','by','from','his','her','him','i','on','you','at','be','all','they','them','could','should','up','He','','we','its','will','any','very','had','have','has','so','which','could','would','when','how','if','their','my','me','who','our','can','where','been','said','one','every']

 #converting

def remove_common_words(word_dict):
    for key in word_dict.copy(): #if encounter one of the common words, remove it #how do you make sure He and The are also excluded
        if key in common_words:
            del word_dict[key]
        else:
            continue
    return word_dict #return a dictionary with only non-common words

def sort(txt):
    sorted_values = sorted(txt.values()) # Sort the values, but it would only return a list of the sorted values
    
    sorted_dict = {}

    for i in sorted_values: #turn into a sorted dictionary based on the size of the value
        for k in txt.keys():
            if txt[k] == i:
                sorted_dict[k] = txt[k]
                
    return sorted_dict


def get_word_sequences(text):
    
    if type(text)== dict:
        t = tuple(text) #turning the list of each word in text into a tuple
    if type(text)== str:
        t = tuple(text.split(' '))
    
    l=[]
    for n in range (len(t)): #making a list of all of the word sequences
        b = t[n:n+2]       
        l.append(b)
    
    new_dict = count_elements(l) #count the occurences of each sequences
    
    for key in new_dict.copy(): #eliminating keys with only one word in tuple
        if len(key) < 2:
            del new_dict[key]
        else:
            continue
        
    return new_dict 

'Don Sturdy in the Tombs of Gold, by Victor Appleton.txt'
'Outposts of Asia, by Morilla Maria Norton.txt'
'Bolo the cave boy, by Katherine Atherton Grimes.txt'

#10 most commonly occurring word sequences

def ten_words(filename):
    txt = remove_common_words(get_word_count(get_file_txt(filename)))
    
    sorted_dict = sort(txt) 
                    
    bar_x = list(sorted_dict.keys())[-10:] #x values of bar garph
    bar_y = list(sorted_dict.values())[-10:] #y values of bar garph

    plt.bar(bar_x, bar_y)
    plt.title("10 most commonly occurring words")
    plt.show()
    

def ten_word_sequences(filename):
    txt = get_word_sequences(remove_common_words(get_word_count(get_file_txt(filename))))

    sorted_dict = sort(txt) #sort the dictionary
             
    bar_x = list(sorted_dict.keys())[-10:] #all the keys (tuple) to a list, x values in type tuple
    
    for n in range (len(bar_x)): #convert the tuples into string with the form (a,b)
        bar_x[n] = '(' + str(bar_x[n][0]) + ',' + str(bar_x[n][1]) + ')'
    
    bar_y = list(sorted_dict.values())[-10:]#all the y value
    
    plt.bar(bar_x, bar_y)
    plt.title("10 most commonly occurring word sequences")
    plt.show()
    
    
