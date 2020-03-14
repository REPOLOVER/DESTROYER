import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from haruka import dispatcher
from haruka.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "വോഡ്കയുടെ നിറമെന്ത്?.",
    "വെള്ളവുമായി എളുപ്പം മിക്സ് ആവുന്ന മദ്യം ഏത്?.",
    "നിങ്ങൾ ഒരു പൈന്റ് ബോട്ടിൽ MC വാങ്ങാൻ പോയി കൗണ്ടറിന് അടുത്തെത്തി അത് സ്റ്റോക്കില്ല എന്നറിയുമ്പോൾ വാങ്ങുന്ന അടുത്ത ബ്രാൻഡ് ഏത്?.",
    "Command not found. Just like your brain.",
    "എത്ര പെഗ് അടിച്ചാലും ഫുഡ് നന്നായി കഴിക്കുക അങ്ങനെയെങ്കിൽ നിങ്ങൾക്ക് വെള്ളമടി ഒരാഘോഷമായി കൊണ്ടുനടക്കാം ഫുഡ് കഴിക്കാതെ മദ്യം മാത്രം കഴിച്ചാൽ ലിവർ ആൻഡ് ഹാർട്ട് ഡാമേജ് ഉറപ്പാണ് ആയതിനാൽ ഫുഡിന്റെ കാര്യത്തിൽ നോ കോമ്പ്രമൈസ്.",
    "ശശി ബീവറേജിൽ വരിക്കു നിൽക്കുന്നു, നാട്ടിലുള്ള ഉസ്മാൻ സാധനം വാങ്ങാൻ വിളിച്ചു പറഞ്ഞു. കയ്യിൽ 670 രൂപയുള്ള ശശിക്ക് ഒരു പൈന്റ് MH ഉം വാങ്ങണം എങ്കിൽ ശശി സുരേഷിന് ഏതു സാധനം വാങ്ങും?.",
    "Bot rule 544 section 9 prevents me from replying to stupid humans like you.",
    "*കേരളത്തിലെ അച്ഛന്മാർ മുകേഷ് അംബാനിയിൽ നിന്നും പഠിക്കണം മുകേഷ് അംബാനി മകളുടെ വിവാഹത്തിന് ചിലവാക്കിയത് സ്വന്തം സ്വത്തിന്റെ 0.12% മാത്രമാണ്അല്ലാതെ നിങ്ങളെ പോലെ ഉള്ളത് എല്ലാം വിറ്റും കടം വാങ്ങിയും നാട്ടുകാരുടെ മുന്നിൽ ആളായി പൊങ്ങച്ചം കാണിച്ച അച്ഛനല്ല മുകേഷ് അംബാനി ഇനീ എങ്കിലും മുകേഷ് അംബാനിയെ കണ്ട് പടിക്കു.",
    "Pick up a gun and shoot yourself.",
    "Try bathing with Hydrochloric Acid instead of water.",
    "ഒരുമയുണ്ടെങ്കിൽ .... ബീവറേജിലും ക്യൂ നിൽക്കാം.",
    "Hit Uranium with a slow moving neutron in your presence. It will be a worthwhile experience.",
    "You can be the first person to step on sun. Have a try.",
)

@run_async
def insult(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- Reply to a text with /insult for insults.
"""

__mod_name__ = "🤬🤬Insults🤬🤬"

INSULT_HANDLER = DisableAbleCommandHandler("insult", insult)

dispatcher.add_handler(INSULT_HANDLER)
