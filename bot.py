import telebot
from threading import Timer

TOKEN = '8032461876:AAGmLkgGBPHlVO5dRjxrs9iccPEjG_zfruM'
ID_DONO = 8098852558

bot = telebot.TeleBot(TOKEN)

produto = "Fone Bluetooth ProX - Qualidade absurda, 24h de bateria, por apenas R$99!"

@bot.message_handler(commands=['start'])
def start(msg):
    chat_id = msg.chat.id
    nome = msg.from_user.first_name
    bot.send_message(chat_id, f"Olá {nome}! 👋\nTenho uma oferta imperdível pra você!\n\n{produto}")
    Timer(60, lambda: insistir(chat_id)).start()

def insistir(chat_id):
    bot.send_message(chat_id, f"Ei! 🤔 Ainda tá pensando? Essa oferta acaba hoje!\nAproveita: {produto}")

@bot.message_handler(func=lambda m: m.text and m.text.lower() in ['quero', 'me interessei', 'interessei', 'topo'])
def interesse(msg):
    chat_id = msg.chat.id
    bot.send_message(chat_id, "Perfeito! Vou avisar o vendedor agora mesmo 💬")
    bot.send_message(ID_DONO, f"📢 Novo interesse!\nUsuário: @{msg.from_user.username or msg.from_user.first_name}\nMensagem: \"{msg.text}\"")

bot.polling(none_stop=True)
