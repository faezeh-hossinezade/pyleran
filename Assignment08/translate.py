import os
import gtts
# result=os.listdir("e:/pylearn/Assignment08/translate.py")
# print (os.listdir())
# print (result)

def read_file():
    global words_bank
    result = os.listdir('e:/pylearn/Assignment08')
    if "Translate.txt" in result:
        words_bank=[]
        with open("Translate.txt", "r") as main_file:
            big_string=main_file.read().split("\n")
        for i in range(0,len(big_string),2):
            my_dict={'en':big_string[i],'fa': big_string[i+1]}
            words_bank.append(my_dict)
        
    else:
        print ("No bank exists in directory")
    
        # print(words_bank)
            
        # print(big_string)
        # for line in main_file.readlines():
        #     words=[]
        #     words.append(line)
                
        #     print(words)
            

def show_menu():
    print("Welcome to the Translator")
    print("1- Traslate English to Persian")
    print("2- Traslate Persion to English")
    print("3- Add a new word to the Database")
    print("4- exit")


def translate_english_to_persian():
    user_text=input("Please enter your text: ")
    user_words=user_text.split(" ")
    output=""
    for word in user_words:
        for worrds in words_bank:
            if word==worrds["en"]:
                output=output+worrds["en"]+" "
                print(worrds["fa"], " " ,end="")
                break
        else:
            output=output+word+""
            print(word, " ", end="")
    translate_sound = gtts.gTTS(output, lang='ar')
    translate_sound.save('translate_to_persian.mp3')

def translate_persion_to_english():
    user_text=input("Please enter your text: ")
    user_words=user_text.split(" ")
    output=""
    for word in user_words:
        for worrds in words_bank:
            if word==worrds["fa"]:
                output=output+worrds["en"]+" "
                print(worrds["en"], " " ,end="")
                break
        else:
            output=output+word+""
            print(word, " ", end="")
    translate_sound = gtts.gTTS(output, lang='ar')
    translate_sound.save('translate_to_english.mp3')
 
def add_new_word():
    with open("Translate.txt", "r") as main_file:
        big_string=main_file.read().split("\n")
        for i in range(0,len(big_string),2):
            my_dict={'en':big_string[i],'fa': big_string[i+1]}
            words_bank.append(my_dict)
            user_text=input("Please enter your text: ")  
            result_new=user_text.split(' ')
            words_dict_new={'en':result_new[0], 'fa':result_new[1]}
            words_bank.append(words_dict_new)
            
    
    
    
def exit_translate():
        exit()          

        
read_file()   
while True:
    show_menu()
    choice=int(input("Please Enter Your Choice: "))
    if choice==1:
        translate_english_to_persian()
    elif choice==2:
        translate_persion_to_english()
    elif choice==3:
        add_new_word()
    elif choice==4:
        exit_translate()
