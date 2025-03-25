import time
import random
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from datetime import datetime, timedelta, timezone

# Configurações do bot
TOKEN = "7322530159:AAGp7V6UZ2ICK4478wnaUaTQTf_kmh9swlo"  # Token do BotFather
CHAT_ID = "-1002663067223"  # ID do canal do Telegram
CHAT_LINK = "https://t.me/MIKUPG"  # Link do chat para onde o botão direcionará

# Inicializa o bot
bot = Bot(token=TOKEN)

# Mensagens motivacionais para apostas
mensagens = [
    "🔥 *A banca está chamando!* Esse horário está *PAGANDO DEMAIS!* 💰🔥 Não perca tempo, faça sua aposta agora e aproveite o momento certo!",
    "⚡️ Tá rolando *chuva de GREEN!* 🌧💵 Aquele momento raro chegou, e só quem é esperto lucra agora! Entra no jogo antes que seja tarde!",
    "🚀 *Dinheiro rápido e fácil?* 🤑💸 Esse horário tá *INSANO!* Quem apostou já está lucrando, e você vai ficar de fora?",
    "💸 Só os *mestres da aposta* sabem os segredos da banca... e *AGORA* é um deles! ⏳💰 Faça sua entrada e garanta o seu lucro!",
    "📈 *GRANA NO BOLSO* ou arrependimento depois? 🎲💵 Esse horário é quente e já tá pagando pesado! Se liga e faz a tua!"
]

# Lista de jogos
jogos = [
    "Dragão e Tigre",
    "Coelho e Touro",
    "Tigre Sortudo e Tigre",
    "Cobra"
]

# Lista de imagens para alternar
imagens = [
    "C:/Users/03594901238/Desktop/bot/miku.jpeg",
    "C:/Users/03594901238/Desktop/bot/miku2.png",
    "C:/Users/03594901238/Desktop/bot/miku3.webp",
]

# Função para gerar um horário pagante próximo ao horário atual no fuso horário do Brasil (UTC-3)
def gerar_horario_pagante_proximo():
    agora = datetime.now(timezone.utc)  # Obtém o horário UTC usando timezone-aware datetime
    agora_brasil = agora - timedelta(hours=3)  # Ajusta para UTC-3
    
    minutos_aleatorios = random.randint(1, 10)
    proximo_horario = agora_brasil + timedelta(minutes=minutos_aleatorios)
    return proximo_horario.strftime("%H:%M")  # Formata para "hh:mm"

# Função assíncrona para enviar mensagens e imagens locais
async def enviar_mensagens():
    while True:
        try:
            # Seleciona jogos aleatórios
            jogos_selecionados = random.sample(jogos, random.randint(2, 3))
            jogos_texto = "🔥 *Jogos pagantes:* " + " | ".join(jogos_selecionados)

            mensagem = random.choice(mensagens) + f"\n\n*📌 Próximo horário pagante:* {gerar_horario_pagante_proximo()}\n{jogos_texto}"

            # Adiciona o link da casa de apostas no final da mensagem
            link_casa_apostas = "👉 BANCA MOLE: [APOSTE AGORA](https://www.mikupg777.com.br/register?id=50305252&currency=BRL&type=2)"

            # Junta a mensagem principal com o link
            mensagem_com_link = f"{mensagem}\n\n{link_casa_apostas}"

            # Criando um botão personalizado para o chat
            teclado = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔥 Acesse nosso Chat! 🔥", url=CHAT_LINK)]
            ])

            # Envia a mensagem com botão
            await bot.send_message(chat_id=CHAT_ID, text=mensagem_com_link, parse_mode="Markdown", reply_markup=teclado)
            
            # Escolhe uma imagem aleatória para enviar
            imagem_escolhida = random.choice(imagens)

            # Envia a imagem escolhida
            with open(imagem_escolhida, "rb") as foto:
                await bot.send_photo(chat_id=CHAT_ID, photo=foto)

            print(f"✅ Mensagem e imagem enviadas: {mensagem_com_link}\nImagem: {imagem_escolhida}")

        except Exception as e:
            print(f"❌ Erro ao enviar mensagem ou imagem: {e}")

        # Tempo aleatório entre 5 e 15 minutos (300s - 900s)
        tempo_espera = random.randint(300, 900)
        print(f"⏳ Próxima mensagem em {tempo_espera // 60} minutos...")
        await asyncio.sleep(tempo_espera)

# Iniciar o envio automático de mensagens
if __name__ == "__main__":
    asyncio.run(enviar_mensagens())
