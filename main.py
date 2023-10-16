from aiogram import executor
from config import dp, bot
from aiogram.dispatcher import FSMContext,filters
from aiogram.types import Message, CallbackQuery, ContentType, ChatType
from butons.reply import start_button, menu_button,quiz_button,tug_button
from butons.inline import kitoblar_button,check_chnl,test1,test2,test3,test4,test5,test6,test7,test8,test9,test10,testnat
from states.register import PersonalData
from config import CHANELS
import subscribe



@dp.message_handler(commands="start")
async def show_channels(message: Message):
    photo = open('others/photo_2023-08-01_21-57-56.jpg', 'rb')
    text = f'Botdan foydalanish uchun quyidagi kanallarga obuna bo\'ling:📢'
    await  message.answer_photo(photo, caption=text, reply_markup=check_chnl)


@dp.callback_query_handler(text='chan1')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('@my_chanel_for_bot')
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='chan2')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('@my_chanel_for_bot2')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text="check_sub")
async def checker(call: CallbackQuery):
    await call.answer()
    result = str()
    chan=0
    for channel in CHANELS:
        status = await subscribe.check(user_id=call.from_user.id, channel=channel)
        channel = await bot.get_chat(channel)
        if status:
            result += f"✅{channel.title} kanaliga obuna bo'lgansiz!\n\n"
            chan+=1
        else:
            invite_link = await channel.export_invite_link()
            result += (f"❌{channel.title} kanaliga obuna bo'lmagansiz. "
                       f"{invite_link}  Obuna bo'ling\n\n")
    await call.message.answer(result, disable_web_page_preview=True)
    if chan==2:
        photo = open('others/photo_2023-07-30_16-51-03.jpg', 'rb')
        text = f'Salom {call.from_user.full_name} Quize botga hush kelibsz🫡'
        await  call.message.answer_photo(photo, caption=text, reply_markup=start_button)



@dp.message_handler(text='Help📝')
async def help(message: Message):
    photo = open('others/photo_2023-07-30_16-57-01.jpg', 'rb')
    text = f'📝Ushbu botda siz o\'z bilimlaringizni sinashingiz va ularni oshirishingiz mumkun\n👨🏽‍💻Murojat uchun @gfdksdgfjsdhfg adminga yoki\n☎️ +9923792835925 raqamiga murojat qilishingiz mumkun'
    await  message.answer_photo(photo, caption=text)


@dp.message_handler(text='Start⬅️')
async def help(message: Message):
    photo = open('others/photo_2023-07-30_18-36-24.jpg', 'rb')
    text = f'Kerakli bo\'limni tanlang'
    await  message.answer_photo(photo, caption=text, reply_markup=menu_button)


@dp.message_handler(text='Books📚')
async def book(message: Message):
    photo = open('others/photo_2023-07-30_17-45-29.jpg', 'rb')
    text = f'Kerakli kitobni tanlang📕'
    await  message.answer_photo(photo, caption=text, reply_markup=kitoblar_button)


@dp.callback_query_handler(text='pdt')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('https://library.samdu.uz/files/2573a73b9b93e25a26281ce87100b6ff_PYTHON%20TILIDA%20DASTURLASH%20ASOSLARI%20(I-QISM).pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='pda')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('https://bilimlar.uz/wp-content/uploads/2021/02/k100001.pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='ep')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('https://ptgmedia.pearsoncmg.com/images/9780134034287/samplepages/9780134034287.pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='pcb')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('http://bedford-computing.co.uk/learning/wp-content/uploads/2015/10/Python-Cookbook-3rd-Edition.pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='fwd')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('https://coddyschool.com/upload/Flask_Web_Development_Developing.pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='pml')
async def pyt_found(call: CallbackQuery):
    await call.message.answer('https://falksangdata.no/wp-content/uploads/2022/07/python-machine-learning-and-deep-learning-with-python-scikit-learn-and-tensorflow-2.pdf')
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='bm')
async def bosh_m(call: CallbackQuery):
    await call.message.answer(f'Bosh Menu🏠',reply_markup=start_button)
    await call.answer(cache_time=10)


@dp.message_handler(text='Programming📋')
async def full(message: Message):
    await message.answer('👨🏽‍💻Ismingizni to\'liq kiriting')
    await PersonalData.fullname.set()


@dp.message_handler(state=PersonalData.fullname)
async def email(msg: Message, state: FSMContext):
    name = msg.text
    await state.update_data(
        {'name': name}
    )
    await msg.answer('🌐Emailingizni kiriting')
    await PersonalData.next()


@dp.message_handler(state=PersonalData.email)
async def phone(msg: Message, state: FSMContext):
    email = msg.text
    await state.update_data(email=email)
    await msg.answer('☎️Telefon raqamni kiriting')
    await PersonalData.phone.set()


@dp.message_handler(state=PersonalData.phone)
async def info(msg: Message, state: FSMContext):
    phone = msg.text
    await state.update_data(phone=phone)

    data = await state.get_data()
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')

    msgs = "👨🏽‍💻Quyidagi ma'lumotlar qabul qilindi:\n\n"
    msgs += f"Ism: {name}\n"
    msgs += f"Email: {email}\n"
    msgs += f"Phone: {phone}\n"
    await msg.answer(msgs,reply_markup=quiz_button)

    await state.reset_state(with_data=False)
    await state.finish()

@dp.message_handler(text='Bosh Menu🏠')
async def bosh_m(message:Message):
    await message.answer(f'Bosh Menu🏠',reply_markup=start_button)


@dp.message_handler(text='Orqaga⬅️')
async def bosh_m(message:Message):
    await message.answer(f'Orqaga⬅️',reply_markup=menu_button)


@dp.message_handler(text='Qayta boshlash🔄️')
async def qayta(message:Message):
    global nat
    global lis
    nat=0
    l=[]
    await message.answer(f'1️⃣.Python dasturlash tili muallifi kim?',reply_markup=test1)


# //////////////////////////////////////////////////////////////////////////////////////////////////////////
@dp.message_handler(text='Testni boshlash👨🏽‍💻')
async def bosh_m(message:Message):
    await message.answer(f'Ommad!',reply_markup=tug_button)
    global nat
    global lis
    nat=0
    lis=[]
    await message.answer('1️⃣.Python dasturlash tili muallifi kim?',reply_markup=test1)

#/////////////////////////////////////*******************************************************
# nat = 0



@dp.callback_query_handler(text='1to')
async def fin(call: CallbackQuery):
    global nat
    nat +=1
    await call.message.edit_text('2️⃣.Python dasturlash tili qachon yaratilgan?', parse_mode='Markdown', reply_markup=test2)
    await call.answer(cache_time=10)

@dp.callback_query_handler(text='2to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('3️⃣.List typini ko\'rsating?', parse_mode='Markdown', reply_markup=test3)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='3to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('4️⃣.Set typini k\'rsating?', parse_mode='Markdown', reply_markup=test4)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='4to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('5️⃣.Qaysi datatype o\'zgarmas,tartiblangan (indekslangan) va dublikatlatga ruhsat beradi?', parse_mode='Markdown', reply_markup=test5)
    await call.answer(cache_time=10)


@dp.callback_query_handler(text='5to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('6️⃣.Tartiblanmagan, indekslanmagan,dublikatlarga ruhsat bermaydigan va o\'zgarmas datatype qaysi?', parse_mode='Markdown', reply_markup=test6)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='6to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('7️⃣. Http so\'rovlarini yuboruvchi va api lar bilan ishlovchi modul', parse_mode='Markdown', reply_markup=test7)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='7to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('8️⃣. Classlarda Obyektni o\'zi murojat qilganda manzil emas qandaydir qiymat qaytaruvchi dannor metodi qaysi? ', parse_mode='Markdown', reply_markup=test8)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='8to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('9️⃣. Classlarda metodlarga va o\'zgaruvchilarga kirishni cheklash uchun nima ishlatiladi', parse_mode='Markdown', reply_markup=test9)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='9to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('🔟.Queueni Stack tarzida ishlash korinishi?', parse_mode='Markdown', reply_markup=test10)
    await call.answer(cache_time=10)



@dp.callback_query_handler(text='10to')
async def fin(call: CallbackQuery):
    global nat
    nat += 1
    await call.message.edit_text('Testimiz sizga yoqdimi🤔😁', parse_mode='Markdown', reply_markup=testnat)
    await call.answer(cache_time=10)


# //////////////////////////////////**********************************************************


@dp.callback_query_handler()
async def all(call: CallbackQuery):
    if call.message:
        if call.data == '1x1'or call.data == '1x2'or call.data == '1x3'or call.data == '1old' :
            lis.append(1)
            await call.message.edit_text('2️⃣.Python dasturlash tili qachon yaratilgan?', parse_mode='Markdown',reply_markup=test2)
        elif call.data == '2x1' or call.data == '2x2' or call.data == '2x3' or call.data == '2old':
            lis.append(2)
            await call.message.edit_text('3️⃣.List typini ko\'rsating?', parse_mode='Markdown', reply_markup=test3)
        elif call.data == '3x1' or call.data == '3x2' or call.data == '3x3' or call.data == '3old':
            lis.append(3)
            await call.message.edit_text('4️⃣.Set typini k\'rsating?', parse_mode='Markdown', reply_markup=test4)
        elif call.data == '4x1' or call.data == '4x2' or call.data == '4x3' or call.data == '4old':
            lis.append(4)
            await call.message.edit_text('5️⃣.Qaysi datatype o\'zgarmas,tartiblangan (indekslangan) va dublikatlatga ruhsat beradi?', parse_mode='Markdown', reply_markup=test5)
        elif call.data == '5x1' or call.data == '5x2' or call.data == '5x3' or call.data == '5old':
            lis.append(5)
            await call.message.edit_text('6️⃣.Tartiblanmagan, indekslanmagan,dublikatlarga ruhsat bermaydigan va o\'zgarmas datatype qaysi?', parse_mode='Markdown', reply_markup=test6)
        elif call.data == '6x1' or call.data == '6x2' or call.data == '6x3' or call.data == '6old':
            lis.append(6)
            await call.message.edit_text('7️⃣. Http so\'rovlarini yuboruvchi va api lar bilan ishlovchi modul',parse_mode='Markdown', reply_markup=test7)
        elif call.data == '7x1' or call.data == '7x2' or call.data == '7x3' or call.data == '7old':
            lis.append(7)
            await call.message.edit_text('8️⃣. Classlarda Obyektni o\'zi murojat qilganda manzil emas qandaydir qiymat qaytaruvchi dannor metodi qaysi? ',parse_mode='Markdown', reply_markup=test8)
        elif call.data == '8x1' or call.data == '8x2' or call.data == '8x3' or call.data == '8old':
            lis.append(8)
            await call.message.edit_text('9️⃣. Classlarda metodlarga va o\'zgaruvchilarga kirishni cheklash uchun nima ishlatiladi', parse_mode='Markdown', reply_markup=test9)
        elif call.data == '9x1' or call.data == '9x2' or call.data == '9x3' or call.data == '9old':
            lis.append(9)
            await call.message.edit_text('🔟.Queueni Stack tarzida ishlash ko\'rinishi?', parse_mode='Markdown', reply_markup=test10)
        elif call.data == '10x1' or call.data == '10x2' or call.data == '10x3' or call.data == '10old':
            lis.append(10)
            await call.message.edit_text('Testimiz sizga yoqdimi🤔😁', parse_mode='Markdown', reply_markup=testnat)
        elif call.data == 'nx1' or call.data == 'nx2' or call.data == 'nx3' or call.data == 'nx4':
            await call.message.edit_text('🏃🏽‍♂️Natijalarni bilish uchun📝\n\nTestni yakunlash🏁\n\nTugmasini bosing🚩🔚', parse_mode='Markdown')



@dp.message_handler(text='Testni yakunlash🏁')
async def tug(message: Message):
    await message.answer(f'⌛Test Yakunlandi\n\n{message.from_user.full_name} siz bu testda:\n✔️To\'g\'ri - {nat}\n❌Xato - {len(lis)}\nNatija ko\'rsatdingiz\n📝Tstlar soni 🔟ta\n👨🏽‍💻Siz {lis} savollarda xato qildingiz',reply_markup=quiz_button)

# ///////////////////////////////////////////////////////////////////////////////////////////////////////

@dp.message_handler(content_types=ContentType.PHOTO)
async def rasm(msg: Message):
    await msg.answer('Bu qanday rasm🤔')


@dp.message_handler(content_types=ContentType.VOICE)
async def rasm2(msg: Message):
    await msg.answer('Juda tushunarsz🙁')


@dp.message_handler(content_types=ContentType.CONTACT)
async def rasm3(msg: Message):
    await msg.answer('Kontaktingiz ko\'rib chiqildi☎️')


@dp.message_handler(content_types=ContentType.STICKER)
async def rasm4(msg: Message):
    await msg.answer('❌')


@dp.message_handler(content_types='audio')
async def rasm5(msg: Message):
    await msg.answer('Bu bot VKM bot emas📢 ')


@dp.message_handler(content_types=ContentType.LOCATION)
async def rasm3(msg: Message):
    await msg.answer('Locationningiz ko\'rib chiqildi📝')


@dp.message_handler(hashtags='money')
@dp.message_handler(cashtags=['eur', 'usd'])
async def hashtag_example(msg: Message):
    await msg.answer('💵')


@dp.message_handler(text_contains='Ahmoq')
async def text_example(msg: Message):
    await msg.reply("So'kish mumkin emas!")


@dp.message_handler(filters.Text(equals='Salom', ignore_case=True))
async def text_example(msg: Message):
    await msg.reply('Vaalaykum assalom')


@dp.message_handler(filters.Text(contains='Assalom', ignore_case=True))
async def text_example(msg: Message):
    await msg.reply('Vaalaykum assalom')


# IsReplyFilter
@dp.message_handler(is_reply=True, commands='user_id')
async def reply_filter_example(msg: Message):
    await msg.answer(msg.reply_to_message.from_user.id)

# IsSenderContact
@dp.message_handler(content_types='contact', is_sender_contact=True)
async def sender_contact_example(msg: Message):
    await msg.answer('Rahmat, kontaktingiz qabul qilindi✔️')

# ForwardedMessageFilter
@dp.message_handler(is_forwarded=True)
async def forwarded_example(msg: Message):
    await msg.answer('Boshqa joydan botga habar tashlamang❌')

# ChatTypeFilter
@dp.message_handler(filters.ChatTypeFilter(ChatType.PRIVATE), commands='shaxsiy')
async def chat_type_example(msg: Message):
    await msg.answer('Bu shaxsiy chat👨🏽‍💻')


if __name__ == '__main__':
    executor.start_polling(skip_updates=True, dispatcher=dp)
