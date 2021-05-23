import os, time
import pandas as pd
import logging, requests, re
import inline_district_keyboard as idk
from cowin_api import CoWinAPI
from datetime import datetime, date, timedelta

from telegram import Sticker, BotCommand, Bot, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram.ext import MessageHandler, Filters, CallbackContext


# REGEX
AGE_BUTTON_REGEX = r'^age: (?P<age_mg>\d+)'
CMD_BUTTON_REGEX = r'^cmd: (?P<cmd_mg>.+)'
STATES_LIST_BUTTON_REGEX = r'^option_selected:'

# Global variables
AGE = 45
ID = ""
USERNAME = ""
FIRSTNAME = ""
LASTNAME = ""
STATE = ""
STATEID = ""
DISTRICT = ""
DISTRICTID = ""
PINCODE = ""
CHATID = ""
DAYS = 0

NOTIFICATION = True
TIMEOUT = 10

# Generating logs
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
URL = 'https://selfregistration.cowin.gov.in/'

logger = logging.getLogger(__name__)
TOKEN = "YOUR_TOKEN_HERE"

def start(update, context):
    author = update.message.from_user.first_name
    reply = """ Hello *{}*! ✋

    I am *Cowin* help bot. 🤖
    I will assist you in finding *vaccination slot*.
    💉💉💉💉💉💉💉💉💉

    It is now easy to *search* 🔍 and setup *alerts* 🔔.
    */help* see all commands
            """.format(author)

    update.message.reply_text(reply, parse_mode="markdown")

    global FIRSTNAME
    global LASTNAME
    global ID 
    global USERNAME
    global CHATID

    FIRSTNAME = update.message.from_user.first_name
    LASTNAME = update.message.from_user.last_name
    ID = update.message.from_user.id
    USERNAME = update.message.from_user.username
    CHATID = update.message.chat_id

def help(update, context):
    text = f'''👨‍🚀 *HELP* 👨‍🚀
    It is our help section.
        
    This bot🤖 work on simple *commands*.
    To run any command put "/" then type your command.👨‍💻
    
    Below is a list of all commands you can use.
        *Commands* -
            1. */start:* to start the bot.
            2. */state:* to add your state.
            3. */pincode:* to add pincode of your region.
            4. */age:* to update your age preference.
            5. */help:* to see help menu.
            6. */slot_today:* to check slot today in your region.
            7. */slot_tomorrow:* to check slot tomorrow in your region.
        
        *Steps* -
            1. Start your bot using /start. 
            2. Add State or Pincode using /state or /pincode.
            3. Find available slots using */slot_today* or */slot_tomorrow*.

        ❗️ NOTE ❗️- To update your age preference use /age. 

    '''
    update.message.reply_text(text, parse_mode="markdown")

def echo_text(update, context):
    text = update.message.text
    if text[0] == '/':
        text = f'''You have entered an wrong command👨‍💻.
        ❌❌❌❌❌❌❌❌❌❌❌

        Please re-enter your command.
        '''
        update.message.reply_text(text)
        return

    output = f''''I am an echo-bot. 🤖
    📱I Will repeat whatever you say.📱

    Echo: '''+ text
    update.message.reply_text(output, parse_mode="markdown")

def district(update, context, STATE_ID, STATE):
    STATE_ID = int(STATE_ID)
    text = f'''👾 *Select District* 👾 
    
    👇👇👇👇👇👇👇👇👇
    '''
    if STATE_ID == 1:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_1(), parse_mode="markdown")
    elif STATE_ID == 2:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_2(), parse_mode="markdown")
    elif STATE_ID == 3:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_3(), parse_mode="markdown")
    elif STATE_ID == 4:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_4(), parse_mode="markdown")
    elif STATE_ID == 5:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_5(), parse_mode="markdown")
    elif STATE_ID == 6:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_6(), parse_mode="markdown")
    elif STATE_ID == 7:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_7(), parse_mode="markdown")
    elif STATE_ID == 8:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_8(), parse_mode="markdown")
    elif STATE_ID == 9:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_9(), parse_mode="markdown")
    elif STATE_ID == 10:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_10(), parse_mode="markdown")
    elif STATE_ID == 11:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_11(), parse_mode="markdown")
    elif STATE_ID == 12:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_12(), parse_mode="markdown")
    elif STATE_ID == 13:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_13(), parse_mode="markdown")
    elif STATE_ID == 14:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_14(), parse_mode="markdown")
    elif STATE_ID == 15:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_15(), parse_mode="markdown")
    elif STATE_ID == 16:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_16(), parse_mode="markdown")
    elif STATE_ID == 17:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_17(), parse_mode="markdown")
    elif STATE_ID == 18:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_18(), parse_mode="markdown")
    elif STATE_ID == 19:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_19(), parse_mode="markdown")
    elif STATE_ID == 20:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_20(), parse_mode="markdown")
    elif STATE_ID == 21:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_21(), parse_mode="markdown")
    elif STATE_ID == 22:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_22(), parse_mode="markdown")
    elif STATE_ID == 23:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_23(), parse_mode="markdown")
    elif STATE_ID == 24:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_24(), parse_mode="markdown")
    elif STATE_ID == 25:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_25(), parse_mode="markdown")
    elif STATE_ID == 26:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_26(), parse_mode="markdown")
    elif STATE_ID == 27:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_27(), parse_mode="markdown")
    elif STATE_ID == 28:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_28(), parse_mode="markdown")
    elif STATE_ID == 29:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_29(), parse_mode="markdown")
    elif STATE_ID == 30:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_30(), parse_mode="markdown")
    elif STATE_ID == 31:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_31(), parse_mode="markdown")
    elif STATE_ID == 32:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_32(), parse_mode="markdown")
    elif STATE_ID == 33:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_33(), parse_mode="markdown")
    elif STATE_ID == 34:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_34(), parse_mode="markdown")
    elif STATE_ID == 35:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_35(), parse_mode="markdown")
    elif STATE_ID == 36:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_36(), parse_mode="markdown")
    elif STATE_ID == 37:
        update.effective_chat.send_message(text, reply_markup=idk.get_district_37(), parse_mode="markdown")
 
def get_states_kb() -> InlineKeyboardMarkup:
    keyboard = [
                [
            InlineKeyboardButton("Andaman and Nicobar Islands", callback_data='option_selected:Andaman and Nicobar Islands:1'),
            InlineKeyboardButton("Andhra Pradesh", callback_data='option_selected:Andhra Pradesh:2'),
        ],
        [
            InlineKeyboardButton("Arunachal Pradesh", callback_data='option_selected:Andhra Pradesh:3'),
            InlineKeyboardButton("Assam", callback_data='option_selected:Assam:4'),
        ],
        [
            InlineKeyboardButton("Bihar", callback_data='option_selected:Bihar:5'),
            InlineKeyboardButton("Chandigarh", callback_data='option_selected:Chandigarh:6'),
        ],
        [
            InlineKeyboardButton("Chhattisgarh", callback_data='option_selected:Chhattisgarh:7'),
            InlineKeyboardButton("Dadra and Nagar Haveli", callback_data='option_selected:Dadra and Nagar Haveli:8'),
        ],
        [
            InlineKeyboardButton("Daman and Diu", callback_data='option_selected:Daman and Diu:37'),
            InlineKeyboardButton("Delhi", callback_data='option_selected:Delhi:9'),
        ],
        [
            InlineKeyboardButton("Goa", callback_data='option_selected:Goa:10'),
            InlineKeyboardButton("Gujarat", callback_data='option_selected:Gujarat:11'),
        ],
        [
            InlineKeyboardButton("Haryana", callback_data='option_selected:Haryana:12'),
            InlineKeyboardButton("Himachal Pradesh", callback_data='option_selected:Himachal Pradesh:13'),
        ],
        [
            InlineKeyboardButton("Jammu and Kashmir", callback_data='option_selected:Jammu and Kashmir:14'),
            InlineKeyboardButton("Jharkhand", callback_data='option_selected:Jharkhand:15'),
        ],
        [
            InlineKeyboardButton("Karnataka", callback_data='option_selected:Karnataka:16'),
            InlineKeyboardButton("Kerala", callback_data='option_selected:Kerala:17'),
        ],
        [
            InlineKeyboardButton("Ladakh", callback_data='option_selected:Ladakh:18'),
            InlineKeyboardButton("Lakshadweep", callback_data='option_selected:Lakshadweep:19'),
        ],
        [
            InlineKeyboardButton("Madhya Pradesh", callback_data='option_selected:Madhya Pradesh:20'),
            InlineKeyboardButton("Maharashtra", callback_data='option_selected:Maharashtra:21'),
        ],
        [
            InlineKeyboardButton("Manipur", callback_data='option_selected:Manipur:22'),
            InlineKeyboardButton("Meghalaya", callback_data='option_selected:Meghalaya:23'),
        ],
        [
            InlineKeyboardButton("Mizoram", callback_data='option_selected:Mizoram:24'),
            InlineKeyboardButton("Nagaland", callback_data='option_selected:Nagaland:25'),
        ],
        [
            InlineKeyboardButton("Odisha", callback_data='option_selected:Odisha:26'),
            InlineKeyboardButton("Puducherry", callback_data='option_selected:Puducherry:27'),
        ],
        [
            InlineKeyboardButton("Punjab", callback_data='option_selected:Punjab:28'),
            InlineKeyboardButton("Rajasthan", callback_data='option_selected:Rajasthan:29'),
        ],
        [
            InlineKeyboardButton("Sikkim", callback_data='option_selected:Sikkim:30'),
            InlineKeyboardButton("Tamil Nadu", callback_data='option_selected:Tamil Nadu:31'),
        ],
        [
            InlineKeyboardButton("Telangana", callback_data='option_selected:Telangana:32'),
            InlineKeyboardButton("Tripura", callback_data='option_selected:Tripura:33'),
        ],
        [
            InlineKeyboardButton("Uttar Pradesh", callback_data='option_selected:Uttar Pradesh:34'),
            InlineKeyboardButton("Uttarakhand", callback_data='option_selected:Uttarakhand:35'),
        ],
        [
            InlineKeyboardButton("West Bengal", callback_data='option_selected:West Bengal:36'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def states_list(update, context):
    text = f'''👾 *Select State* 👾 
    
    👇👇👇👇👇👇👇👇👇
    '''
    update.effective_chat.send_message(text, reply_markup=get_states_kb(), parse_mode="markdown")
    return

def states_list_callback(update, context):
    query = update.callback_query
    query.answer()
    text = query.data

    global STATE
    global STATEID
    
    if text[-2] == ':':       
        STATE = text[16:-2]
        STATEID = text[-1:]
    else:    
        STATE = text[16:-3]
        STATEID = text[-2:]

    text = f''' *Selected State* 

    ✔️✔️✔️✔️✔️✔️✔️✔️

    >  Successful: 👍🏻
    >  STATE: {STATE}
    >  STATE ID: {STATEID}
    
    ✔️✔️✔️✔️✔️✔️✔️✔️
    '''
    query.edit_message_text(text, parse_mode="markdown")
    
    district(update, context, STATEID, STATE)

def echo_sticker(update, context):
    text = update.message.text
    update.message.reply_sticker(sticker=update.message.sticker.file_id)

def error(update, context):
    logger.warning('Update "%s" caused  "%s"', update, context.error)

def get_age_kb() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("18+", callback_data='age: 1'),
            InlineKeyboardButton("45+", callback_data='age: 2'),
        ]
    ]
    return InlineKeyboardMarkup(keyboard)

def age_command(update, context):
    text = f'''👾 *Select Age* 👾 
    
    👇👇👇👇👇👇👇👇👇
    '''
    update.effective_chat.send_message(text, reply_markup=get_age_kb(), parse_mode="markdown")
    return

def age_callback(update, context):
    query = update.callback_query
    query.answer()

    global AGE
    if query.data == 'age: 1':
        AGE = 18
    elif query.data == 'age: 2':
        AGE = 45

    text = f''' *Selected Age*

    ✔️✔️✔️✔️✔️✔️✔️✔️

    >  Successful: 👍🏻
    >  New Age: {AGE}

    ✔️✔️✔️✔️✔️✔️✔️✔️
    '''
    query.edit_message_text(text, parse_mode="markdown")
    
def button(update, context):
    query = update.callback_query
    query.answer()

    global DISTRICT
    global DISTRICTID

    text = query.data
    if text[-2] == '-':       
        DISTRICT = text[:-2]
        DISTRICTID = text[-1:]
    elif text[-3] == '-':  
        DISTRICT = text[:-3]
        DISTRICTID = text[-2:]
    elif text[-4] == '-':  
        DISTRICT = text[:-4]
        DISTRICTID = text[-3:]
    else:
        DISTRICT = text[:-5]
        DISTRICTID = text[-4:]

    text = f''' *Selected District*

    ✔️✔️✔️✔️✔️✔️✔️✔️

    >  Successful: 👍🏻
    >  DISTRICT: {DISTRICT}
    >  DISTRICT ID: {DISTRICTID}
    
    ✔️✔️✔️✔️✔️✔️✔️✔️
    '''
    query.edit_message_text(text)
    age_command(update, context)

def pincode_command(update, context):
    text = f'''👾 *Pincode Section* 👾 
    
    👇👇👇👇👇👇👇👇👇
        This Section is under-construction.
        You can use /state command.

    '''
    update.effective_chat.send_message(text, parse_mode="markdown")
    return

def get_slot_today(update, context):
    if len(DISTRICTID) == 0  and len(PINCODE) == 0:
        text = f"NOT ENOUGH DETAILS!!!! {DISTRICTID}:{PINCODE}"
        update.message.reply_text(text)
        
    else:
        cowin = CoWinAPI()
        today =  date.today()
        DATE = today.strftime("%d-%m-%Y") 
        if len(DISTRICTID) > 0:
            available_centers = cowin.get_availability_by_district(DISTRICTID, DATE, AGE)
        elif len(PINCODE) > 0:
            available_centers = cowin.get_availability_by_pincode(PINCODE, DATE, AGE)

    UPDATE = False
    if len(available_centers["centers"]) > 0:       
        URL = 'https://selfregistration.cowin.gov.in/'
        for x in available_centers["centers"]:
            center_name = x["name"]
            center_address = x["address"]
            center_district = x["district_name"]
            center_pincode = x["pincode"]
            center_fee = x["fee_type"]
            
            for items in x["sessions"]:
                vaccines = []
                if items["available_capacity_dose1"]>0 and items["available_capacity_dose2"]>0:
                    if items['vaccine'] not in vaccines:
                        vaccines.append(items['vaccine'])

                    DOSE1 = items["available_capacity_dose1"]
                    DOSE2 = items["available_capacity_dose2"]
                    MIN_AGE_LIMIT = items["min_age_limit"]

                    text = f"Name: {center_name}\nDistrict: {center_district}\nAddress: {center_address}\nPincode:{center_pincode}\n\nFees: {center_fee}\nDate: {DATE}\nDose1: {DOSE1}\nDose2: {DOSE2}\nAge Limit: {MIN_AGE_LIMIT}\n{URL}"
                    update.message.reply_text(text)
                    UPDATE = True

    if not UPDATE:
        text = f"No Slot Available on {DATE} in your region.\n\nFor more information \n{URL}"
        update.message.reply_text(text)

def get_slot_tomorrow(update, context):
    if len(DISTRICTID) == 0  and len(PINCODE) == 0:
        text = f"NOT ENOUGH DETAILS!!!! {DISTRICTID}:{PINCODE}"
        update.message.reply_text(text)
        
    else:
        cowin = CoWinAPI()
        today =  date.today() + timedelta(1)
        DATE = today.strftime("%d-%m-%Y") 
        if len(DISTRICTID) > 0:
            available_centers = cowin.get_availability_by_district(DISTRICTID, DATE, AGE)
        elif len(PINCODE) > 0:
            available_centers = cowin.get_availability_by_pincode(PINCODE, DATE, AGE)

    UPDATE = False
    if len(available_centers["centers"]) > 0:       
        URL = 'https://selfregistration.cowin.gov.in/'
        for x in available_centers["centers"]:
            center_name = x["name"]
            center_address =  x["address"]
            center_district = x["district_name"]
            center_pincode = x["pincode"]
            center_fee = x["fee_type"]
            
            for items in x["sessions"]:
                vaccines = []
                if items["available_capacity_dose1"]>0 and items["available_capacity_dose2"]>0:
                    if items['vaccine'] not in vaccines:
                        vaccines.append(items['vaccine'])

                    DOSE1 = items["available_capacity_dose1"]
                    DOSE2 = items["available_capacity_dose2"]
                    MIN_AGE_LIMIT = items["min_age_limit"]

                    text = f"Name: {center_name}\nDistrict: {center_district}\nAddress: {center_address}\nPincode:{center_pincode}\n\nFees: {center_fee}\nDate: {DATE}\nDose1: {DOSE1}\nDose2: {DOSE2}\nAge Limit: {MIN_AGE_LIMIT}\n{URL}"
                    update.message.reply_text(text)
                    UPDATE = True

    if not UPDATE:
        text = f"No Slot Available on {DATE} in your region.\n\nFor more information \n{URL}"
        update.message.reply_text(text)
    
def main():
    bot = Bot(TOKEN)
    bot.set_my_commands([
        BotCommand(command='start', description='start the bot session'),
        BotCommand(command='help', description='provide help in using bot'),
        BotCommand(command='state', description='update your state and district'),
        BotCommand(command='pincode', description='update pincode'),
        BotCommand(command='age', description='update age preference'),
        BotCommand(command='slot_today', description='Check slot for today in your region'),
        BotCommand(command='slot_tomorrow', description='Check slot for tomorrow in your region'),
    ])

    updater = Updater(TOKEN, use_context=True)

    dispacher_obj = updater.dispatcher

    dispacher_obj.add_handler(CommandHandler("start", start))
    dispacher_obj.add_handler(CommandHandler("help", help))
    dispacher_obj.add_handler(CommandHandler("state", states_list))
    dispacher_obj.add_handler(CommandHandler("slot_today", get_slot_today))
    dispacher_obj.add_handler(CommandHandler("slot_tomorrow", get_slot_tomorrow))
    dispacher_obj.add_handler(CommandHandler("age", age_command))
    dispacher_obj.add_handler(CommandHandler("pincode", pincode_command))

    dispacher_obj.add_handler(CallbackQueryHandler(age_callback, pattern=AGE_BUTTON_REGEX))
    dispacher_obj.add_handler(CallbackQueryHandler(states_list_callback, pattern=STATES_LIST_BUTTON_REGEX))

    dispacher_obj.add_handler(CallbackQueryHandler(button))
    dispacher_obj.add_handler(MessageHandler(Filters.text, echo_text))
    dispacher_obj.add_handler(MessageHandler(Filters.sticker, echo_sticker))

    dispacher_obj.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
