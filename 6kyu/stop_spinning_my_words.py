#Write a function that takes in a string of one or more words, and returns the same string, 
#but with all words that have five or more letters reversed. 
#Strings passed in will consist of only letters and spaces. 
#Spaces will be included only when more than one word is present.
#
#Examples:
#
#"Hey fellow warriors"  --> "Hey wollef sroirraw" 
#"This is a test        --> "This is a test" 
#"This is another test" --> "This is rehtona test"

#solution:

def spin_words(sentence):
    words = sentence.split()
    i=0
    for word in words:
        if len(word) >= 5:
            words[i]=word[::-1]
        i+=1
    text = ' '.join(words)
    return text

#tests

print(spin_words("Hey fellow warriors")) #Should be "Hey wollef sroirraw"
print(spin_words("This sentence is a sentence")) #Should be "This ecnetnes is a ecnetnes"