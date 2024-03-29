from random import randint
import qrcode
import telebot
from telebot import types
import gtts
import datetime
from persiantools.jdatetime import JalaliDate

random_numbers = {}


bot = telebot.TeleBot("7162319400:AAFNJgpETKxWNgJm8h8-IXmngbHr0DeadSM")

# markup = types.ReplyKeyboardMarkup(row_width=4)
# itembtn1 = types.KeyboardButton('start')
# itembtn2 = types.KeyboardButton('game')
# itembtn3 = types.KeyboardButton('age')
# itembtn4 = types.KeyboardButton('voice')
# itembtn5 = types.KeyboardButton('max')
# itembtn6 = types.KeyboardButton('argmax')
# itembtn7 = types.KeyboardButton('qrcode')
# itembtn8 = types.KeyboardButton('help')

# markup.add(itembtn1, itembtn2, itembtn3,itembtn4, itembtn5, itembtn6, itembtn7, itembtn8)

@bot.message_handler(commands=['start'])
def start_chat(message):
    first_name = message.from_user.first_name
    bot.send_message(message.chat.id, f'{first_name} خوش آمدی  ...')

## new button    
game_markup=  types.ReplyKeyboardMarkup(row_width=1)  
key1 = types.KeyboardButton('new_game')
game_markup.add(key1)
## new button

@bot.message_handler(commands=['game'])
def start_game(message):
    print(message.from_user.username)
    username = message.from_user.username
    random_numbers[username] = randint(0, 100)
    msg = bot.send_message(message.chat.id, f'Enter Your Number (1, 100)...', reply_markup=game_markup)
    bot.register_next_step_handler(msg, game)

##function  
def game(message):
    print(message.from_user.username)
    username = message.from_user.username
    try:
        user_input = int(message.text)
        if user_input > random_numbers[username]:
            msg = bot.send_message(message.chat.id, 'Your Number is Bigger...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
        elif user_input < random_numbers[username]:
            msg = bot.send_message(message.chat.id, 'Your Number is Smaller...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
        else:
            msg = bot.send_message(message.chat.id, 'You Win...', reply_markup=game_markup)
            bot.register_next_step_handler(msg, game)
    except:
        pass
        # msg = bot.send_message(message.chat.id, 'Invalid Input...', reply_markup=game_markup)
        # bot.register_next_step_handler(msg, game)



@bot.message_handler(commands=['age'])
def age(message):
    msg = bot.send_message(message.chat.id, f'Enter Your Age Forexample 1385/12/02 ...')
    bot.register_next_step_handler(msg, age_calculation)
    ## daryafte dade az karbar
    print(message.from_user.username)

##function    
def age_calculation(message):
    print(message.from_user.username)
    try:
        year, month, day = str(message.text).split('/')
        year, month, day = int(year), int(month), int(day)
        miladi_date = JalaliDate(year, month, day).to_gregorian()
        ekhtelef_miladi_date = datetime.date.today() - miladi_date
        user_age = ekhtelef_miladi_date.days // 365
        bot.send_message(message.chat.id, f'Your Age is {user_age}')

    except:
        msg = bot.send_message(message.chat.id, 'Invalid Input...')
        bot.register_next_step_handler(msg, age_calculation)

@bot.message_handler(commands=['voice'])
def make_voce(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Text ...')
    bot.register_next_step_handler(msg, get_voice)

##function
def get_voice(message):
    print(message.from_user.username)
    user_text = message.text
    # az text user estefade mikone
    voice = gtts.gTTS(user_text, lang="en")
    voice.save("faeze_voice.mp3")
    with open("faeze_voice.mp3", "rb") as file:
        bot.send_voice(message.chat.id, file)
        
@bot.message_handler(commands=['max'])
def age(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Arrays like 12,14,17, ...')
    bot.register_next_step_handler(msg, compare) 

##function
def compare(message):
    print(message.from_user.username)
    user_list = str(message.text).split(',')
    user_list = list(map(lambda text: text.strip(), user_list))
    bot.send_message(message.chat.id, f'Max Arg is {max(user_list)}')
              
@bot.message_handler(commands=['argmax'])
def age(message):
    print(message.from_user.username)
    msg = bot.send_message(message.chat.id, f'Enter Your Arrays like 12,14,17, ...')
    bot.register_next_step_handler(msg, compare_arg) 
    
##function
def compare_arg(message):
    print(message.from_user.username)
    user_list = str(message.text).split(',')
    user_list = list(map(lambda text: text.strip(), user_list))
    bot.send_message(message.chat.id, f'Index of Max Arg is {user_list.index(max(user_list))}')
               
@bot.message_handler(commands=['qrcode'])
def age(message):
    msg = bot.send_message(message.chat.id, f'Enter a Sentence ...')
    bot.register_next_step_handler(msg, qrcode_maker) 

##function
def qrcode_maker(message):
    print(message.from_user.username)
    user_text = message.text
    img = qrcode.make(user_text )
    type(img)  # qrcode.image.pil.PilImage
    img.save("qrcode_text.png")
    with open("qrcode_text.png", "rb") as file:
        bot.send_photo(message.chat.id, file)

@bot.message_handler(commands=["help"])
def help(message):
    print(message.from_user.username)
    text = '''1- /start -> start \n2- /game -> Number Game\n3- /age -> Calculate Age With Year Of Birth\n4- /voice -> Convert Text To Voice\n5- /max -> Find The Largest Value\n6- /argmax -> Find The Largest Index Value\n7- /qrcode -> Get QRcode With Text\n8- /help -> Show Help\n
        '''
    bot.send_message(message.chat.id, text)
    
    
bot.infinity_polling()