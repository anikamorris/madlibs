blanks = {"past tense verb": [], "occupation": [], "verb ending in -ing": [], "noun": [], "verb": [], 
            "adjective": []}

# INPUT
def user_input(prompt):
    # display message in terminal and wait for user input
    user_input = input(prompt)
    return user_input

def get_words():
    # ask user for word that matches key, then append value
    
    for k, v in blanks.items():
        # handles "a" vs "an"
        if k[0] == "o" or k[0] == "a":
            response = user_input("Enter an " + k + ": ")
            v.append(response)
        else:
            response = user_input("Enter a " + k + ": ")
            v.append(response)

    # gets duplicate words
    verb2 = user_input("Enter another verb ending in -ing: ")
    blanks["verb ending in -ing"].append(verb2)

    for i in range(3):
        noun = user_input("Enter another noun: ")
        blanks["noun"].append(noun)

def populate_mad_libs():
    print(" I just " + blanks["past tense verb"][0] + " a DNA test, turns out I'm 100% that "
         + blanks["occupation"][0] + "\n Even when I'm " + blanks["verb ending in -ing"][1] + """ crazy  
 Yeah, I got """ + blanks["noun"][2] + " problems, that's the human in me \n Bling bling, then I "
         + blanks["verb"][0] + " 'em, that's the " + blanks["noun"][0] + " in me \n You coulda had a "
         + blanks["adjective"][0] + " " + blanks["noun"][3] + ", non-commital \n Help you with your "
         + blanks["noun"][1] + """ just a little \n You're supposed to hold me down, but you're holding me back
 And that's the sound of me not """ + blanks["verb ending in -ing"][0] + " you back")
    
get_words()
populate_mad_libs()