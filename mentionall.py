import random, os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config 


logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS


client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []
  

	
	
	
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.reply(f"**๐คSalam...๐ญ,**\nMษnim Adฤฑm [๐ฉ๐๐ฐ๐๐๐ฆ๐ฟ ๐๐๐๐๐๐ ๐๐ฐ๐ต](http://t.me/UstaTagbot)-u.\n**Qurupunuz'daki  bรผtรผn รผzvlษri taฤ etmษk sษlahiyyษtinษ sahibษm.\n\n๐คฦtraflฤฑ mรผษlumat รผรงรผn '๐ฦmrlษr' bรถlmษsinษ daxil olun.**", buttons=(
                     [Button.url('โ Mษni Qrupa ษlavษ et โ','http://t.me/UstaTagbot?startgroup=a')],
	             [Button.inline(f"๐ ฦmrlษr", data="help"),
	              Button.inline(f"๐ Tษkliflษr", data="reklam")],
	             [Button.url('Qrup๐ฌ', 'https://t.me/Bizim_Paytaxt'),
                      Button.url('๐๐๐๐ ๐๐๐๐๐๐ ๐จโ๐ป', 'https://t.me/ustabots')],
                    ),
                    link_preview=False)


  if event.is_group:
    return await client.send_message(event.chat_id, f"** [๐ฉ๐๐ฐ๐๐๐ฆ๐ฟ ๐๐๐๐๐๐ ๐๐ฐ๐ต](http://t.me/UstaTagbot)'un ฦmrlษr รผรงรผn?.Bot'a daxil olub.**", buttons=(
                     [Button.url('๐กBota Keรง','https://t.me/UstaTagbot?start=start')],
	             [Button.url('๐๐๐๐ ๐๐๐๐๐๐ ๐จโ๐ป','https://t.me/ustabots'),
		      Button.url('Qrup๐ฌ', 'https://t.me/Bizim_Paytaxt')],
                    ),
                    link_preview=False)



@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"**๐คSalam...๐ญ,**\nMษnim Adฤฑm [๐ฉ๐๐ฐ๐๐๐ฆ๐ฟ ๐๐๐๐๐๐ ๐๐ฐ๐ต](http://t.me/UstaTagbot)-u.\n**Qurupunuz'daki  bรผtรผn รผzvlษri taฤ etmษk sษlahiyyษtinษ sahibษm.\n\n๐คฦtraflฤฑ mรผษlumat รผรงรผn '๐ฦmrlษr' bรถlmษsinษ daxil olun.**", buttons=(
                     [Button.url('โ Mษni Qrupa ษlavษ et โ','http://t.me/UstaTagbot?startgroup=a')],
	             [Button.inline(f"๐ ฦmrlษr", data="help"),
	              Button.inline(f"๐ Tษkliflษr", data="reklam")],
	             [Button.url('Qrup๐ฌ', 'https://t.me/Bizim_Paytaxt'),
                      Button.url('๐๐๐๐ ๐๐๐๐๐๐ ๐จโ๐ป', 'https://t.me/ustabots')],
                    ),
                    link_preview=False)


@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):	
    await event.edit(f"** [๐ฉ๐๐ฐ๐๐๐ฆ๐ฟ ๐๐๐๐๐๐ ๐๐ฐ๐ต](http://t.me/UstaTagbot)-un Kรถmษk '๐ ฦmrlษr' Bunlardฤฑr.โคต**\n\n\nโขโโโโโโโโโขโขโขโโโโโโโโโข\n**๐คโช /tag <sษbษb> - 5-li Tag Atฤฑลlarฤฑ.**\n**๐คโช /etag <sษbษb> - Emoji ilษ etiketlษr.**\n**๐คโช /stag <sษbษb> - Sรถz'lรผ Tag etiketlษr.**\n**๐คโช /tektag <sษbษb> - รzvlษri Tษk-Tษk etiketlษr.**\n**๐คโช /usta <sษbษb> - usta Tag Bot'una aid Tag etiketlษr.**\n**๐คโช /admins <sษbษb> - ฤฐdarษรงilษr Tษk-Tษk etiketlษr.**\n**๐คโช /cancel - Tag ฦlษmษyi Dayandฤฑr.**\nโขโโโโโโโโโขโขโขโโโโโโโโโข", buttons=(
	             [Button.url('Qrup๐ฌ', 'https://t.me/Bizim_Paytaxt'),
                      Button.url('๐๐๐๐ ๐๐๐๐๐๐ ๐จโ๐ป', 'https://t.me/ustabots')],
	             [Button.inline(f"๐ Geri", data="start")]
                    ),
                    link_preview=False)

@client.on(events.callbackquery.CallbackQuery(data="reklam"))
async def handler(event):	
    await event.edit(f"**๐ [๐ฉ๐๐ฐ๐๐๐ฆ๐ฟ ๐๐๐๐๐๐ ๐๐ฐ๐ต](http://t.me/UstaTagbot)-un & ๐๐๐๐ ๐๐๐๐๐๐ ๐จโ Tษkliflษr รผรงรผn sahib'lษ ษlaqษ saxlaya bilษrsiniz...**", buttons=(
		     [Button.url('๐ Sahib', 'https://t.me/Nehmedov')],
	             [Button.url('Qrup๐ฌ', 'https://t.me/Bizim_Paytaxt'),
                      Button.url('๐๐๐๐ ๐๐๐๐๐๐ ๐จโ๐ป', 'https://t.me/ustabots')],
	             [Button.inline(f"๐ Geri", data="start")]
                    ),
                    link_preview=False)
	
    
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


emoji = "๐ ๐ต ๐ ๐ ๐ฆ ๐ ๐ ๐ฏ ๐ ๐ ๐ฑ ๐ ๐ ๐ถ ๐ ๐ ๐บ ๐ ๐ ๐ป ๐ฅญ ๐คฃ ๐จ ๐ ๐ญ ๐ผ ๐ ๐ ๐น ๐ถ ๐ ๐ญ ๐ ๐ ๐ฐ ๐ฅ ๐ ๐ฆ ๐ ๐ฅฐ ๐ฆ ๐ ๐คฉ ๐ฎ ๐ ๐ฅณ ๐ท ๐ ๐ค ๐ฝ ๐ ๐ ๐ ๐ฅ ๐ ๐ฆ ๐? โบ๏ธ ๐ฆ ๐ง ๐ ๐ด ๐ฝ ๐ ๐ธ ๐ฅฆ ๐ ๐ฒ ๐ฅ ๐ ๐ฆ ๐ฅฌ ๐คญ ๐ ๐ฅ ๐ถ ๐ฆ ๐ฅฏ ๐ ๐ฆ ๐ฅ ๐ ๐ข ๐ฅ ๐ ๐ ๐ ๐ ๐ ๐ฐ ๐ ๐ ๐ฅ ๐ ๐ ๐ง ๐ ๐ ๐ ๐คช ๐ฉ ๐ง ๐ค ๐ ๐ฅ ๐คจ ๐ฆฎ ๐ฅ ๐ง ๐โ๐ฆบ ๐ง ๐ ๐ ๐ฅ ๐ ๐ ๐ฅฉ ๐ค ๐ ๐ ๐? ๐ ๐ ๐คฌ ๐ ๐ฅ โน๏ธ ๐ ๐ฏ ๐ ๐ ๐ฎ ๐ ๐ ๐ ๐ ๐ ๐ ๐ฅบ ๐ ๐ฅจ ๐ณ ๐ฆ ๐ฅช ๐ฌ ๐ฆ ๐ญ ๐ค ๐ฆฅ ๐ ๐คซ ๐ฆ ๐ง ๐ฐ ๐ ๐ฅ ๐จ ๐ฆ ๐ ๐ง ๐ฆ ๐ฅซ ๐ฆ ๐ฆ ๐ฅฃ ๐ฎ ๐ ๐ฅ ๐ฏ ๐ฆ ๐ฒ ๐ฒ ๐ฆง ๐ ๐ฑ ๐ช ๐ ๐คฏ ๐ซ ๐ข ๐ข ๐ฟ๏ธ ๐ฅ ๐ฅ ๐ฆจ ๐ฑ ๐ ๐ฆก ๐ ๐ ๐ฆ ๐ฅก ๐ ๐ฆฆ ๐ค ๐ฃ ๐ฆ ๐ฃ ๐ฉ ๐ ๐ฆ ๐ซ ๐ ๐ฆช ๐คค ๐ฃ ๐ ๐ฅฑ ๐ค ๐ก ๐ด ๐ฅ ๐ฅ? ๐ช ๐ฆ ๐ฅฎ ๐คข ๐ฆ ๐ง ๐คฎ ๐ฆ ๐จ ๐คง ๐ฆ ๐ซ ๐ค ๐ชฑ ๐ช ๐ถโ๐ซ ๐๏ธ ๐ฅ ๐ค? ๐ฆข ๐ญ ๐ค ๐ฆฉ ๐ง ๐คค ๐ฆ ๐ฆ ๐ฅต ๐ฆ ๐ซ ๐ฅถ ๐ง ๐ฅ ๐ฅธ ๐ฆ ๐ฆ ๐ค ๐ณ ๐ณ ๐ ๐ ๐ฅง ๐คญ ๐ ๐ฅค ๐คซ ๐ฆ ๐จ".split(" ")
  


@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qruplar รผรงรผn etibarlฤฑdฤฑr!**")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmrdษn yalnฤฑz idarษรงilษr istifadษ edษ bilษr!**")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ฦvvษlki Mesajlara Cavab verษ Bilษrษm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur! **")
  else:
    return await event.respond("**Tag'a baลlamaq รผรงรผn sษbษb yazฤฑn...!**")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("** Tag ษmษliyyatฤฑ uฤurla dayandฤฑrฤฑldฤฑ!**")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)


@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qruplar รผรงรผn etibarlฤฑdฤฑr! ** ")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmrdษn yalnฤฑz idarษรงilษr istifadษ edษ bilษr! **")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ฦvvษlki Mesajlara Cavab verษ Bilษrษm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur! **")
  else:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur,yazฤฑn...! **")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond(" **Tag ษmษliyyatฤฑ uฤurla dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 5:   
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qruplar รผรงรผn etibarlฤฑdฤฑr! **")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmrdษn yalnฤฑz idarษรงilษr istifadษ edษ bilษr! ** ")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ฦvvษlki Mesajlara Cavab verษ Bilษrษm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur! **")
  else:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur,yazฤฑn...! **")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**โฏ [{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	

stag = (
"Bษzi insanlar yaฤฤฑลฤฑ hiss edษr, digษrlษri isษ sadษcษ islanar",
"Unutma; Hษr gษlษn sevmษz.. Vษ heรง bir sevgili getmษz",
"Heรง bir ruhun aฤrฤฑsฤฑ sษnin dษrdindษn az deyil",
"Mษn hษr ลeyi sฤฑnayฤฑram; amma bacardฤฑฤฤฑmฤฑ edirษm.",
"Sevgi bir qadฤฑnฤฑn hษyatฤฑnฤฑn bรผtรผn hekayษsidir vษ bir kiลinin yeganษ macษrasฤฑdฤฑr.",
"Xoลbษxtlik ilk nรถvbษdษ bษdษn saฤlamlฤฑฤฤฑndadฤฑr.",
"Nษ qษdษr yaลadฤฑฤฤฑmฤฑz deyil, necษ yaลadฤฑฤฤฑmฤฑzdฤฑr",
"Yer gรถy qurลaฤฤฑ, aฤฤฑl prizma, varlฤฑq isษ aฤ ลรผadฤฑr.",
"Hara getdiyinizi bilmirsinizsษ, hansฤฑ tษrษfษ getdiyinizin ษhษmiyyษti yoxdur.",
"Hษyatฤฑn ษn qiymษtli vaxtฤฑdฤฑr. Kimษ hษdiyyษ etdiyinizษ diqqษt edin.",
"Evin bรผtรผn pษncษrษlษrini sฤฑndฤฑrฤฑb, sonra qapฤฑnฤฑ dรถyษ bilmษzsษn.",
"Xoลbษxtlik yaลadฤฑฤฤฑn hษyat tษrzindษ deyil, hษyata baxฤฑล tษrzindษdir.",
"Unutma; Hษr gษlษn sevmษz.. Vษ heรง bir sevgili getmษz.",
"Bu hษyatda yarฤฑm nษfษs. Sevgidษn baลqa heรง nษ planlaลdฤฑrma...",
"Hษr kษsษ iรงindษki yaxลฤฑlar qษdษr yaxลฤฑ bir hษyat arzulayฤฑram.",
"Gรถzษlliyi gรถzษl edษn ษdษbdir, ษdษb isษ gรถzษlliyi sevmษk รผรงรผn sษbษbdir!",
"Qฤฑzฤฑlgรผlรผn ษtri qฤฑzฤฑlgรผl verษnin ษlindษ qalฤฑr",
"Axtardฤฑฤฤฑn ลey sษni axtarandฤฑr.",
"Hษtta bir quล da gรถydษ qanad รงฤฑrpar.",
"Kรถnรผl almaฤฤฑ bilmษyษnlษrษ hษyat ษmanษt deyil.",
"Dรผrรผst olmaqdan qorxma, ษn รงox itirษcษyiniz yanlฤฑล insanlar olacaq.",
"ฤฐnsan aฤac deyil, qฤฑrฤฑlanda sษs รงฤฑxararsan.",
"รyrษnmษk hษyatฤฑn yeganษ sรผbutudur.",
"Dรผnya ษhalisi artdฤฑqca insanlarฤฑn sayฤฑ azalฤฑr.",
"Layiq olmadฤฑฤฤฑnฤฑ dรผลรผndรผyรผnรผz insanlara ษsla hษqiqษti demษyin.",
"รox ลรผkรผr ki, gรถy hษlษ heรง bir pul kisษsinษ sฤฑฤmฤฑr.",
"รzรผn ol. Artฤฑq hamฤฑ gรถtรผrรผb.",
"Zษrษr รงษkdim, boฤazฤฑmdakฤฑ dรผyรผnlษri uddum.",
"O qษdษr gรถzษl gรผlรผmsษyirdi ki, sevmษsษydim boลuna olardฤฑ.",
"Onun sevdiyi men deyilem. Bunun aฤrฤฑsฤฑnฤฑ sizษ deyษ bilmษrษm.",
"Onun sevdiyi men deyilem. Bunun aฤrฤฑsฤฑnฤฑ sizษ deyษ bilmษrษm.",
"Zamanla hษr ลeyษ alฤฑลฤฑrsan, amma bitmir.",
"ฦgษr hษqiqษti deyirsษnsษ, heรง nษyi xatฤฑrlamaฤa ehtiyac yoxdur.",
"Hษqiqษti ilk sรถylษyษn siz olun... ฦks halda kimsษ sizin yerinizษ mรผtlษq hษqiqษti sรถylษyษcษk.",
"Kiลilษr daha gรผclรผ ola bilษr, amma qadฤฑnlar dรถzรผmlรผdรผrlษr.",
"Aฤrฤฑ รผรงรผn heรง bir resept yoxdur",
"Ardฤฑnca getmษyษ cษsarษtiniz varsa, bรผtรผn arzular gerรงษklษลษ bilษr.",
"Bu gizli sevgidir, heรง kimษ dษrdlษrimi deyษ bilmษrษm.",
"Sizcษ sevgi hษr ลeyi baฤฤฑลlayฤฑr?",
"Mษnษ dษ, sษnษ dษ siqaret lazฤฑmdฤฑr",
"Mษn sษndษn xรผsusi birini tanฤฑmฤฑrdฤฑm",
"Bir gรผn sevgi bitษr, xatirษlษr qalฤฑr",
"Sevmษk nษ qษdษr uzun bir sรถzdรผr!",
"Hatฤฑrladฤฑฤฤฑm en unutulasฤฑ ลeysin.",
"Birlikdษ gรผlmษk รผรงรผn darฤฑxdฤฑฤฤฑm insanlar var.",
"Xoลbษxtliyi sษndษ tapan sษnindir, รผstษlik qonaq.",
"รox sev, amma bษyษnmirsษnsษ mษcbur etmษ!",
"O  qษdษr  gรถzษl gรผlรผrdรผ ki, sevmษsษm ziyan olacaqdฤฑ.",
"vษ  insan insana yoldaล olmalฤฑ yaralarฤฑnฤฑ saฤalatmalฤฑ",
"Mษzarlฤฑq, ษsษb  uฤruna peลman olanlarla dolu",
"Eลq kรผlษk  kimidir gรถrmษzsษn ama hiss edษ bilษrsษn.",
"tษrษzi  var รถlรงรผ var , hษrลeyin bir vaxtฤฑ var",
"Yanฤฑltmasฤฑn sษni masum baxฤฑลlar, bษzฤฑlarฤฑnฤฑ ลeytan ayaqdษ alqฤฑลlar...",
"hษyat sabahฤฑ gรถzlษyษcษk qษdษr uzun deyil",
"Yaxลฤฑlar ษsla itirmษz , itirilir.",
"gรถrmษzden gษldiyin sevgiyษ mรถhtac qalman dilษyiylษ",
"Kaลki aฤฤฑl vermษk yerinษ hรผzur versษniz",
"Heรง bilmษdiyim o qoxunu รงox รถzlษyirษm",
"๐๐๐ฅ๐?ฬง๐ค ๐๐๐๐ ๐๐ก๐๐๐?๐๐๐ ๐๐๐ง๐๐ฤฑ๐",
"๐ดล๐๐ ๐๐๐๐๐ ๐๐ฬ๐งษ๐ ๐๐๐ ล๐๐ฆ ๐๐๐ ๐?๐๐ษ๐ษ ๐?ษnษ",
"๐ป๐๐ฬง๐๐๐ โ๐๐ฬง๐๐๐๐ ๐๐ก๐๐๐๐๐ง  ๐๐๐ษ๐ ๐๐ล๐๐๐?ฤฑ๐ฤฑ ๐ก๐๐๐๐, ๐๐๐๐๐ ๐ฬ๐ง๐ขฬ๐๐ขฬ",
"ร๐๐ฅ รถ๐ษ๐๐?ษ๐๐๐ ๐ลษ ๐ฆ๐๐๐๐๐๐ฤฑ ๐๐๐ก๐ค๐ ๐๐ล๐ฃ๐๐๐๐๐๐",
"ร๐๐รผ๐รผ๐งรผ ๐?๐ข๐?๐๐ข๐๐๐๐๐ค๐๐ค๐ง๐ค  ๐๐?ฬง๐๐๐๐ ๐๐๐๐๐ฆ๐ษ ๐๐รง๐๐๐๐",
"๐บรถ๐๐รผ๐รผ๐งษ  ๐๐๐ฤฑฤฤฑ๐ฤฑ๐ง ๐รถ๐๐รผ๐รผ๐งรผ ๐๐๐๐๐ฬฤฑ ๐๐๐๐?๐๐",
"๐ษ๐ รง๐๐ฅ ๐?๐๐ฃ ๐๐ ๐๐ข๐๐๐ฅฤฑ๐  ๐๐๐ษ๐ ๐ฆ๐๐ ๐ข๐ก๐๐๐?ฤฑ๐",
"๐๐๐ฅ๐?ฬง๐ค ๐๐๐๐ ๐๐ก๐๐๐?ษ๐ษ ๐๐๐ง๐๐ฤฑ๐",
"๐๐๐ฃ๐ล๐๐๐ฆฤฑ ๐๐ข๐๐๐ฅ๐ค๐๐๐  ๐๐ข๐๐ข ๐ฃ๐๐๐ ๐?๐๐ฆ",
"๐ษ ๐รง๐๐๐ษ๐๐ ๐๐ขฬ๐ฬงษ๐ษ๐ษ ๐?ฤฑฤ๐๐๐๐๐๐๐ ๐ษ ๐ษ ๐ฬง๐ฬ๐๐ษ๐๐ ๐รผ๐๐ฆ๐๐ฆ๐",                  
"๐ด๐๐กฤฑ๐ โ๐รง๐๐๐ ล๐๐ฆ ษ๐ฃ๐ฃษ๐๐๐ ๐๐๐๐ ๐๐๐ฆ๐๐ ๐ต๐ข๐๐ ๐ษ๐๐ษ ๐๐๐ฅ๐๐ษ๐",                
"๐ดล๐๐ ๐๐๐๐๐ ๐๐ฬ๐ง๐๐ ๐๐๐ ล๐๐ฆ ๐๐๐ ๐?๐๐ษ๐ษ ๐?ษ๐ษ",                 
"ฤฐ๐๐?๐๐ ๐๐๐๐๐ฤฑฤฤฑ ๐ฃ๐ ๐๐๐๐ลฤฑ๐๐ฤฑฤฤฑ ๐๐๐?๐๐๐๐ รง๐รงษ๐ ๐รง๐๐",
"๐๐๐ฅ๐?ฬง๐ค๐ฆ๐๐ ๐๐๐?ษ๐ ๐๐๐๐๐๐๐๐, ๐ ๐ษ๐ษ๐ ๐ฅษ๐ษ๐๐?๐๐ง ๐ษ๐๐ษ๐", 
"๐ธ๐ษ ๐๐ฬ๐งษ๐ ๐๐๐ฅ๐กฤฑ ๐๐ ๐ษ๐๐๐ ๐ษ ๐รผ๐รผลรผ ๐ษ๐ษ๐ ๐๐ฬ๐งษ๐ ๐?๐๐๐ฤฑล๐กฤฑ๐",
"๐ษ๐?๐๐ษ๐ษ๐ ๐๐๐๐ข๐๐๐ ๐ท๐๐ฆ๐๐, ฤฐรง๐๐๐ษ ๐ธ๐ ๐บรผ๐งษ๐ ๐๐๐๐ษ๐?ษ๐",
"ฤฐ๐๐?๐๐ ๐ษ๐งษ๐ ๐๐ฬ๐ฆรผ๐ ๐ฅษ๐ฆ๐๐๐๐๐๐ค๐๐ค ๐๐รง๐๐ ๐๐๐?๐๐๐๐๐๐๐ ๐ง๐๐ฆ๐๐ ๐๐ษ๐",
"๐ป๐๐ฬง๐๐๐ โ๐๐ฬง๐๐๐๐ ๐๐ก๐๐๐ษ๐ง ๐๐๐ษ๐ ๐๐ล๐๐๐?ฤฑ๐ฤฑ ๐ก๐๐๐๐  ๐๐๐๐๐ ๐ฬ๐ง๐ขฬ๐๐ขฬ",
"ร๐๐ฅ รถ๐ษ๐๐?ษ๐๐๐ ๐ลษ ๐ฆ๐๐๐๐๐๐ฤฑ ๐๐๐กฤฑ๐ ๐๐ล๐ฃ๐๐๐๐๐๐",              
"๐ต๐๐ รง๐รง๐๐๐๐ ๐รผ๐๐๐ ๐๐๐ฤฑ๐ ๐๐๐ ๐๐๐๐๐ โรผ๐งรผ๐",
"๐ปษ๐ ล๐๐ฆ๐ ๐๐๐ษ๐ ๐๐๐ฆ๐๐ ๐ฤฑ๐ฆ๐ษ๐ก ๐๐๐ษ๐ ๐๐๐?๐๐๐๐๐ ๐๐๐?๐ข๐ โษ๐ฆ๐๐กฤฑ๐ฤฑ๐ง๐๐",
"๐๐๐๐๐ษ๐ ๐ษ๐ฆษ๐๐๐ ๐๐๐๐๐๐๐ข ๐๐๐๐๐ฆฤฑ๐ ๐๐๐๐๐?๐ โษ๐๐๐๐๐ข๐",
"๐ษ๐?๐๐ษ ๐๐ฆ๐๐๐๐ ๐ษ โษ๐๐๐๐๐ ๐ล๐๐ ๐๐๐ข๐ ๐ษ ๐ษ ๐๐๐ฤฑ๐ฤฑ ๐?ฤฑ๐ฅ๐๐",                
"๐ปษ๐ฆ๐๐ก ๐rษl๐๐ฆษ ๐๐๐ฅฤฑ๐๐๐๐๐ ๐ฆ๐ล๐๐ฤฑ๐ ๐๐๐๐๐ฆษ  ๐๐๐ฅ๐๐๐๐ ๐๐๐๐ลฤฑ๐ฤฑ๐",
"๐ษ๐ รง๐๐ฅ ๐?๐๐ฃ ,  ๐๐๐ษ๐ ๐ฆ๐๐ ๐ข๐ก๐๐๐?ฤฑ๐",
"๐ต๐๐ ๐๐ฬ๐๐ขฬ๐งษ๐ฆษ ๐ธโ๐ก๐๐ฆ๐๐ฤฑ๐ ๐๐๐ ๐๐๐ ๐ปษ๐ฆ๐๐ก ๐ษ๐๐ ๐๐๐ลฤฑ๐๐ รฤฑ๐ฅ๐๐๐ฤฑ",
"ฤฐ๐๐?๐๐ ๐๐๐๐๐ฤฑฤฤฑ ๐ฃษ ๐๐๐๐ลฤฑ๐๐ฤฑฤฤฑ ๐๐๐?๐๐๐๐ รง๐รงษ๐ ๐รง๐๐",
"๐ขฬ๐ษ๐ฆ๐๐๐๐ ๐ก๐๐ ๐๐๐ก๐๐?ฤฑ๐๐๐ ๐๐ฬ๐ฆรผ๐ ๐๐๐                    ๐ฆ๐๐๐ฬ๐ข๐๐๐ข๐ ๐ฃ๐๐",
"๐ษ๐๐๐ ๐๐ฬ๐งษ๐ ๐๐๐๐ฤฑ๐ ๐รถ๐งรผ๐๐ษ๐ ๐ฆ๐ล ษ๐๐?๐๐ ๐๐๐๐๐ง๐ฤฑล",
"๐ปษ๐ ล๐๐ฆ๐๐ ๐๐๐ก๐๐๐ฆ๐ ๐ฆ๐๐๐ษ ๐ษ๐๐ษ ๐๐๐ก๐๐๐ ๐ษ๐ฆ๐ล๐๐๐ ๐๐๐ฆษ๐๐ษ๐๐๐ ษ๐?ษ๐๐๐ฆษ๐",
"๐บรผ๐ฃษ๐๐ษ๐ ๐?๐๐ฃ๐ษ๐๐ษ๐ ๐๐โ๐ ๐ษ๐ฆษ๐๐๐, ๐๐๐๐๐๐๐ ๐๐๐๐๐๐?ฤฑ๐",
"ฤฐ๐ล๐๐๐๐โ ๐?ษ๐๐๐ษ  ๐๐ฬ๐ง๐ษ๐๐๐ฆ๐๐ โ๐๐ ล๐๐ฆ ๐ขฬ๐ฬง๐ขฬ๐ ๐ฅ๐๐ฆ๐๐๐๐ ๐๐๐ ๐ฅษ๐ษ๐ ๐๐ฤฑ๐๐?ฤฑ๐",
"ฤฐ๐๐?๐๐ ๐ษ๐งษ๐ ๐๐ฬ๐ฆ๐ขฬ๐ ๐ฅษ๐ฆ๐๐๐๐๐๐ค๐๐ค ๐๐๐ฬง๐๐ ๐๐๐?๐๐๐๐๐๐๐ ๐ง๐๐ฆ๐๐ ๐๐ษ๐ ",
"ร๐๐ษ๐ ๐ต๐๐ ล๐๐ฆ ๐๐y๐๐ ๐ฆ๐ล๐๐๐๐๐๐ ๐๐๐๐ฅ๐ข๐๐",
"๐ปษ๐๐ษ๐?๐๐ ๐๐๐ ๐๐รง๐๐ล๐ ๐ฃ๐๐, ๐ต๐๐๐ษ ๐ฃ๐๐ง๐๐รง๐๐ล๐",
"๐บรผ๐๐รผ ๐รถ๐รผ๐ษ ๐๐๐ษ๐ษ๐ ๐๐๐ ๐๐๐๐           ๐ฆ๐๐๐ฬ๐ข๐๐๐",
"๐ปษ๐ฆ๐๐ก ๐ษ ๐๐๐ษ๐๐ ๐๐๐๐ ๐ษ๐ก๐๐๐๐ ๐ษ๐ษ ๐๐ก๐๐๐๐๐ฆ๐๐๐๐ง ๐ง๐๐๐๐ฤฑ ๐๐๐๐ ๐ษ๐ก๐๐๐๐",                   
"๐ธ๐๐๐๐ ๐๐โ๐๐ฤฑ ๐๐๐๐ ๐ข๐๐ข๐ง๐๐ข."
)	

@client.on(events.NewMessage(pattern="^/stag ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qruplar รผรงรผn etibarlฤฑdฤฑr! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmrdษn yalnฤฑz idarษรงilษr istifadษ edษ bilษr! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ฦvvษlki Mesajlara Cavab verษ Bilษrษm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur! **")
  else:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur,yazฤฑn...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(stag)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern="^/admins ?(.*)"))
async def tag_admin(event):
    chat = await event.get_input_chat()
    text = "โ๏ธAdminlษr Siyahฤฑsฤฑโ๏ธ"
    async for x in event.client.iter_participants(chat, 100, filter=ChannelParticipantsAdmins):
        text += f" \n โฏ [{x.first_name}](tg://user?id={x.id})"
    if event.reply_to_msg_id:
        await event.client.send_message(event.chat_id, text, reply_to=event.reply_to_msg_id)
    else:
        await event.reply(text)
    raise StopPropagation


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)

	
@client.on(events.NewMessage(pattern="^/usta ?(.*)"))

async def mentionall(event):

  global anlik_calisan
  if event.is_private:
    return await event.respond("**Bu ษmr qruplar รผรงรผn etibarlฤฑdฤฑr! ** ")

  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu ษmrdษn yalnฤฑz idarษรงilษr istifadษ edษ bilษr! ** ")

  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("**ฦvvษlki Mesajlara Cavab verษ Bilษrษm! **")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur! **")
  else:
    return await event.respond("**Baลlamaq รผรงรผn heรง bir sษbษb yoxdur,yazฤฑn...! **")

  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! **")
        return
      if usrnum == 1: 
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)

    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"โฏ [{random.choice(usta)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("**ฦmษliyyat Uฤurla Dayandฤฑrฤฑldฤฑ! ** ")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

usta = ('Buda kimmiล dษ miล miล๐๐๐','๐๐๐คฒAaฤil','๐ Sษn dediyim sรถzรผ elษdin? ๐','Hษyatฤฑmฤฑn dolmasฤฑ ๐ฅฒ nassฤฑn๐','Mษnษ niyษ elษ baxฤฑrsan? ๐','ฤฐkinci planda olmaqdansa, plana daxil olmamaฤฤฑ seรงษrษm.  ๐ฏ','sษni basqa qrublardada gรถrmรผsdรผm ','Ac olanda sษn o sษn deyilsษn','Niyษ yalan danฤฑลฤฑrsan adamฤฑn รผstรผndษ patalok var','Hษci necษsษn ficuuu ','kรถhnษ mษkanฤฑn yeni sakini ','gรผnรผn gรผnnษn durdun uzax de gรถrรผm haramฤฑ bษyษnmษdin','deyrlษr รถlรผbsษn๐ค','Gรผรงlรผyรผm... รรผnkรผ baลka seรงeneฤim yok dรผลersem tutanฤฑm olmayacak biliyorum...๐ฌ','gษl bir birimizi arka sokaklar bitษnษ qษdษr sevษkโค๏ธ','corona belษ bรถyรผdรผ sษn bรถyรผmษdin','corona belษ unduldu sษni unuda bilmษdim๐ฌ','sษni sevirษm sรถzรผndษ neรงษ dษnษ samit var','oฤlanlar niyษ az yaลayฤฑr','bitkilษr yaลlandฤฑqcamฤฑ รถlษr yoxsa baxฤฑmsฤฑzlฤฑqdanmฤฑ','isti havada รงay iรงirsษn hษlษdษ','allah rษhmษt elษsin','tez gษlin hษdiyyษli yarฤฑลฤฑmฤฑz basladฤฑ','Benim hayelerim kelebeฤin รถmrรผ kadar yaลar ๐๐ฅ','รiรงษklษrษ aลaฤฤฑdan baxmaฤa gedirษm..โฐ','susะผuล ะฒir qadฤฑn รผรงรผn... ะฒiัะผiล ะฒir adaะผsan.! ๐ค','๐ษ๐๐ษ๐๐๐๐ ๐ฬ๐ฃ๐ษ๐๐๐ษ ๐๐๐๐๐๐๐๐ฬ๐๐๐๐ฃ ๐ฬ๐ฬง๐ฬ๐ ๐ฬ๐ฃ๐๐๐๐๐๐ ๐๐ฬ๐๐๐๐๐๐ฃ ๐๐๐๐๐ ๐๐๐๐๐๐๐๐ ๐๐๐๐','Gรผclรผ olmaฤa mษndษn daha รงox ehtiyacฤฑn var, รงรผnki haqsฤฑz olduฤunu รผrษyinin bir yerindษ bilirsษn.๐ค','Makiyaj vษ รผz boyalarฤฑnฤฑza gรผvษnmษyin. Yollar da gรถzษldir, lakin altฤฑndan kanalizasiya keรงir.๐๐','๐ธฬ๐๐๐๐๐๐ข๐๐ ๐๐๐ก๐๐ ๐๐๐ข๐๐๐๐ ๐๐๐๐ษ๐๐๐ข๐๐ ๐๐๐๐ ๐๐ษ๐๐๐ข๐๐ ๐๐๐๐๐๐ข๐ ๐ษ ๐๐๐ฬง ๐๐๐ก๐ ๐๐ฬ๐ฃษ๐๐ษ ๐๐๐๐๐๐ขษ๐๐๐๐ษn๐','๐ฑ๐๐๐๐ฃ ๐๐๐๐๐ ๐๐ ๐๐๐ขe๐ษ๐ ๐๐๐๐ ๐ษ๐๐ ๐ษ ๐ฬงษ๐๐๐ ๐ษ๐ฃ๐๐ข๐ขษ๐๐ษ ๐๐๐ข๐๐๐ฬ ๐๐๐ษ๐๐๐ษ๐๐คง','ฤฐnsanlฤฑฤa dษvษt etdikdษ yolu soruลan insanlar var.๐ฅ๐','Qoyduฤum ลeylษri รถz yerindษ tapa bilmirษm. Bษzilษrini adam yerinษ qoydum, indi gษl tap gรถrรผn necษ tapฤฑrsanโ','Ayษ biri bunu aparsฤฑn๐ซข','ฦgษr bu hษyatda รถz tayฤฑnฤฑ tapa bilmirsษnsษ รผzรผlmษ, demษli sษn tayฤฑ bษrabษri olmayan birisษn.Qabriel Qarsia Markuez (Meksikalฤฑ yazฤฑรงฤฑ)๐ฅฒ','Xoล Gษldim Nษfษs๐ฅฒ','Gษlmirsษn Balaca๐','Kimษ Yazฤฑsan??? ๐คจ','รirkin รocuq Gษl๐','Cikolatam๐','Aaa Sษndษ Burdasan๐ณ','Al Sษnษ รikolata๐ค๐๐ซ','Sevmirsษn Mษni?๐ Onda Ol๐','Haa Dรผz derisษn?๐ง','Bu Kimdir๐','Gษl Dava Edษx๐๐ช','Bax Sษnษ Nษ Aldฤฑm๐๐๐','Nษ Gรถzษlsษn๐คข รirkin รrdษk Yavrusu','Sษn Kimsษn๐A Gษdษ๐','Gษl Sษnษ Sรผrpรผrรผzรผm var๐คซ','Ooo รox Gรถzษlsin๐ค๐คBal','ลษxsiyษ Yaz๐dรผnbษlษx','Gษl Gรถrรผm Hษlษ๐ง Nษ demisษn Mษnษ๐ฌ','Ayib Olsun๐ซ Niyษ Yazmฤฑrsan๐','Bezdim Sษndษn๐ฅฒ','Bu Neรงษdirโ๏ธ๐','Nรถmrษni ver dษ Vpda yazฤฑลa๐','๐๐ Gรถzรผn รฤฑxsฤฑn gษl๐','ฤฑmmm Gษl yogo yapalฤฑm๐งโโ๐คญ','gษl sษnษ bฤฑra sรผzdรผm๐ช๐ป','Aฤlฤฑmฤฑ Baลฤฑmdan ala ลษxs๐ตโ๐ซgษl mษnษ doฤru','Sษni gรถrdรผm qฤฑzmam qalxdษ๐ค',) 


@client.on(events.NewMessage(pattern='/offline'))
async def handler(event):
    # Kimsษ "Salam" vษ baลqa bir ลey deyษndษ cavab verin
    if str(event.sender_id) not in SUDO_USERS:
        return await event.reply("__Sษn mษnษ sahib deyilsษn!__")
    await event.reply('**Bot ฤฐลlษyir Narahat olmayฤฑn** \n https://t.me/DegGixM \n\nโญโโโโฎ \nโฐโฎโญโฎโโฑโฑโญโฎ\nโฑโโโโฃโโโโโโโณโฎโญโณโฎโญโฎ\nโฑโโโโโโโโซโญโฎโโฐโฏโโโโ\nโญโฏโฐโฏโโโโซโโญโฎโฃโฎโญโซโฐโฏโ\nโฐโโโโปโโโซโฃโฏโฐโฏโฐโฏโฐโโโฏ\nโฑโฑโฑโฑโฑโฑโญโฏโ\nโฑโฑโฑโฑโฑโฑโฐโโฏ',
		     buttons=(
	             [Button.url('DegGixM','https://t.me/DegGixM'),
	             Button.url('Ali','https://t.me/MUCVE_M')],
                    ),
                    link_preview=False)

print(">> Bot iลlษyir narahat olmayฤฑn. @MUCVE_M Mษlumat almaq รผรงรผn <<")
client.run_until_disconnected()
