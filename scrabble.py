from wordscore import score_word
import string


def run_scrabble(rack):
    """Find all valid Scrabble words that can be constructed from the rack. 
    Args:
    - rack (str): A string containing 2 to 7 characters (A-Z, a-z and/or wildcards: '*' and '?'. 

    Returns:
    - list of tuples where each tuple contains:
    1. a possible word based on the rack
    2. the score for that word
    sorted by score and then by word alphabetically.
    """
    #user input
    #rack = input("Enter upper or lower case letters. At least 2 and no more than 7.").upper()
    
    #validate input for scrabble rack
    if len(rack) <= 1 or len(rack) >= 8:
        return("Input Error. Please enter between 2 and 7 alphabetic characters.")
    if not all(char in string.ascii_letters + '*?' for char in rack):
        return("Input Error. Rack contains invalid characters. Use only (A-Z), (a-z), * or ?.")

    #counts wildcards in the rack and returns false ifthere are more than 2 
    wildcard_count = rack.count('*') + rack.count('?') 
    if wildcard_count > 2: 
        return("Error! There are more than 2 wild cards.")
    
    #read file of possible English scrabble words
    with open("sowpods.txt", "r") as infile: 
        raw_input = infile.readlines()
        word_list = [datum.strip('\n').upper() for datum in raw_input]
   
    
    #checking to see if words from word list can be formed using rack
        valid_words = [] #list of (score, word) tuples
   
    #create copy of rack 
        for word in word_list:
            rack_copy = [i.upper() for i in rack]
       
     
    #count characters removed from rack
            counter = 0 
            wildcard_chars = []

            for char in word:
                if char in rack_copy:
                    rack_copy.remove(char)
                    counter += 1
                elif '*' in rack_copy:
                    rack_copy.remove('*')
                    counter += 1
                    wildcard_chars.append(char)
                elif '?' in rack_copy:
                    rack_copy.remove('?')
                    counter += 1
                    wildcard_chars.append(char)
                else:
                    break
        
            
            if len(word) == counter:
                    valid_words.append(word) #note to self - removed .lower() from here
         
       
    #score words and create list of tuples
    score_list = []
    
    score_list = [(score_word(word,rack), word) for word in valid_words]
    
    # for word in valid_words:
    #     score_list.append(score_word(word, rack), word.upper()])
         
    #sorting sort list by score first, then alphabetically by word
    sorted_valid_words = sorted(score_list, key=lambda x: (-x[0],x[1]))
    return sorted_valid_words, len(sorted_valid_words)
    

# result, total_words = run_scrabble("ab")
# print(result)
#     # for word in sorted_valid_words: 
#     #     print(f"{score_word(word, rack)}, {word})")
#     # total_words = len(sorted_valid_words)
# print("Total words:", total_words)

    

    