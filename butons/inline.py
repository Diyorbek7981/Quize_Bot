from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


check_chnl = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='My chanel',callback_data='chan1'),
            InlineKeyboardButton(text='My chanel 2',callback_data='chan2')
        ],
        [
            InlineKeyboardButton(text='Obunani tekshirish✔️',callback_data='check_sub')
        ]
    ]
)

kitoblar_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Python dasturlash tili', callback_data='pdt'),
            InlineKeyboardButton(text='Python dasturlash asoslari', callback_data='pda'),
            InlineKeyboardButton(text='Effective Python', callback_data='ep'),
        ],
        [
            InlineKeyboardButton(text='Python Cookbook', callback_data='pcb'),
            InlineKeyboardButton(text='Flask Web Development', callback_data='fwd'),
            InlineKeyboardButton(text='Python machine learning', callback_data='pml'),
        ],
        [
            InlineKeyboardButton(text='Bosh Menu🏠', callback_data='bm')
        ]
    ]
)

test1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Mark Zuckerberk', callback_data='1x1'),
        ],
        [
            InlineKeyboardButton(text='Guido Van Rossum', callback_data='1to'),
        ],
        [
            InlineKeyboardButton(text='Stiv Jobs', callback_data='1x2'),
        ],
        [
            InlineKeyboardButton(text='Bil Geyts', callback_data='1x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='1old'),
        ],
    ]
)


test2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='1989 - yil', callback_data='2to'),
        ],
        [
            InlineKeyboardButton(text='1991 - yil', callback_data='2x1'),
        ],
        [
            InlineKeyboardButton(text='1994 - yil', callback_data='2x2'),
        ],
        [
            InlineKeyboardButton(text='2001 - yil', callback_data='2x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='2old'),
        ],
    ]
)


test3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='[1,2,3,4,5]', callback_data='3to'),
        ],
        [
            InlineKeyboardButton(text='(1,2,3,4,5)', callback_data='3x1'),
        ],
        [
            InlineKeyboardButton(text='(1,)', callback_data='3x2'),
        ],
        [
            InlineKeyboardButton(text='{1,2,3,4,5}', callback_data='3x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='3old'),
        ],
    ]
)



test4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='[1,2,3,4,5]', callback_data='4x1'),
        ],
        [
            InlineKeyboardButton(text='(1,2,3,4,5)', callback_data='4x2'),
        ],
        [
            InlineKeyboardButton(text='(1,)', callback_data='4x3'),
        ],
        [
            InlineKeyboardButton(text='{1,2,3,4,5}', callback_data='4to'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='4old'),
        ],
    ]
)



test5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Set', callback_data='5x1'),
        ],
        [
            InlineKeyboardButton(text='Dictionary', callback_data='5x2'),
        ],
        [
            InlineKeyboardButton(text='List', callback_data='5to'),
        ],
        [
            InlineKeyboardButton(text='Tuple', callback_data='5x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='5old'),
        ],
    ]
)


test6 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Set', callback_data='6to'),
        ],
        [
            InlineKeyboardButton(text='Dictionary', callback_data='6x1'),
        ],
        [
            InlineKeyboardButton(text='List', callback_data='6x2'),
        ],
        [
            InlineKeyboardButton(text='Tuple', callback_data='6x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='6old'),
        ]
    ]
)


test7 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Map moduli', callback_data='7x1'),
        ],
        [
            InlineKeyboardButton(text='Requests moduli', callback_data='7to'),
        ],
        [
            InlineKeyboardButton(text='Filtr moduli', callback_data='7x2'),
        ],
        [
            InlineKeyboardButton(text='Http moduli', callback_data='7x3'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='7old'),
        ]
    ]
)


test8 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='__sel__', callback_data='8x1'),
        ],
        [
            InlineKeyboardButton(text='__set__', callback_data='8x3'),
        ],
        [
            InlineKeyboardButton(text='__init__', callback_data='8x2'),
        ],
        [
            InlineKeyboardButton(text='__repr__', callback_data='8to'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='8old'),
        ]
    ]
)


test9 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Mavhumlash', callback_data='9x1'),
        ],
        [
            InlineKeyboardButton(text='Abstraksiya', callback_data='9x3'),
        ],
        [
            InlineKeyboardButton(text='Inkapsulatsiya', callback_data='9to'),
        ],
        [
            InlineKeyboardButton(text='Dannor metodlar', callback_data='9x2'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='9old'),
        ]
    ]
)



test10 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='FifoQueue', callback_data='10x1'),
        ],
        [
            InlineKeyboardButton(text='LiloQueue', callback_data='10x2'),
        ],
        [
            InlineKeyboardButton(text='StackQueue', callback_data='10x3'),
        ],
        [
            InlineKeyboardButton(text='LifoQueue', callback_data='10to'),
        ],
        [
            InlineKeyboardButton(text='Oldinga➡️', callback_data='10old'),
        ]
    ]
)


testnat = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Ha😁', callback_data='nx1'),
        ],
        [
            InlineKeyboardButton(text='Juda yoqdi🤩', callback_data='nx2'),
        ],
        [
            InlineKeyboardButton(text='Vashee zo\'r😎', callback_data='nx3'),
        ],
        [
            InlineKeyboardButton(text='Man shokdaman🤐', callback_data='nx4'),
        ],
    ]
)