from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [ 
         KeyboardButton(text="🇺🇿Uzbek"),
        KeyboardButton(text="🇷🇺Russian"),
        KeyboardButton(text="🇬🇧English"),
        ],
        [
        KeyboardButton(text="🇫🇷French"),
        KeyboardButton(text="🇩🇪German"),
        KeyboardButton(text="🇸🇦Arabic"),
        ],
        [ 
        KeyboardButton(text="🇰🇷Korean"), 
        KeyboardButton(text="🇮🇹Italian") ,
        KeyboardButton(text="🇪🇸Spanish") ,
        ]
      
    ],
    resize_keyboard=True
)