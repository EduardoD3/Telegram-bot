import time
import random
import asyncio
from telegram import Bot
from datetime import datetime, timedelta

# Configurações do bot
TOKEN = "7322530159:AAGp7V6UZ2ICK4478wnaUaTQTf_kmh9swlo"  # Token do BotFather
CHAT_ID = "-1002663067223"  # ID do canal do Telegram

# Inicializa o bot
bot = Bot(token=TOKEN)

# Mensagens motivacionais para apostas
mensagens = [
    "🔥 A banca está chamando! Esse horário está PAGANDO DEMAIS! 💰🔥 Não perca tempo, faça sua aposta agora e aproveite o momento certo!",
    "⚡️ Tá rolando chuva de GREEN! 🌧💵 Aquele momento raro chegou, e só quem é esperto lucra agora! Entra no jogo antes que seja tarde!",
    "🚀 Dinheiro rápido e fácil? Sim! 🤑💸 Esse horário tá insano! Quem apostou já está lucrando, e você vai ficar de fora?",
    "💸 Só os mestres da aposta sabem os segredos da banca... e AGORA é um deles! ⏳💰 Faça sua entrada e garanta o seu lucro!",
    "📈 GRANA NO BOLSO ou arrependimento depois? 🎲💵 Esse horário é quente e já tá pagando pesado! Se liga e faz a tua!",
    "💎 Oportunidade de OURO na mesa! 🏆💰 Tá pagando bem, e só os mais rápidos vão lucrar! Entra agora e faz teu jogo!",
    "🔥 Hora da virada! Quem não aposta, não ganha! 🎰💵 Agora é o momento de fazer a banca trabalhar para você!",
    "⏳ Quem aposta agora, ri depois! 😏💰 O sinal tá forte, a banca tá mole... será que você vai deixar passar?",
    "⚠️ ALERTA GREEN! 🚨💵 As odds estão absurdas e a chance de lucrar é REAL! Quem pegar esse horário vai sorrir no final!",
    "🎯 Alvo certo! 📊📈 As análises confirmam: esse é o momento certo para meter a aposta e buscar o lucro! Tá esperando o quê?",
    "🔥 NÃO É SORTE, É ESTRATÉGIA! 📊💰 Quem tá ligado sabe que esse é um horário PAGANTE! Entra agora e aproveita!",
    "💵 Ganhar dinheiro sem sair de casa? Simples! 🌎💰 As odds estão perfeitas agora. Faz tua entrada antes que passe a chance!",
    "🏆 Os melhores apostadores já sabem... e você? 🎲💰 Não perca essa OPÇÃO DE LUCRAR AGORA! O jogo tá aberto, aproveita!",
    "🚨 Banca solta! 💰💥 A casa tá distribuindo! É agora ou nunca! Se joga e garante o teu!"
]

# URLs dos GIFs do tigrinho
gifs = [
    "https://files.oaiusercontent.com/file-5ufh1JE1CpjABXiDVyfNno?se=2025-03-24T14%3A39%3A30Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D11c28c8a-848c-40fc-9b96-ed3eb3f9bbc9.webp&sig=rTVwXyqhm2qdRHSU73K7nCEgIoGCMF3eC3qbMu9Y0bQ%3D",  # Gif 1
    "https://cdn.qwenlm.ai/output/74c24795-1c5e-4ef6-bd6a-1b5de9537b38/t2i/49e2811a-595d-4634-a4f4-0911b4bc5884/ba308609-1e89-4593-9405-3dc1d50bad2b.png?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXNvdXJjZV91c2VyX2lkIjoiNzRjMjQ3OTUtMWM1ZS00ZWY2LWJkNmEtMWI1ZGU5NTM3YjM4IiwicmVzb3VyY2VfaWQiOiJiYTMwODYwOS0xZTg5LTQ1OTMtOTQwNS0zZGMxZDUwYmFkMmIiLCJyZXNvdXJjZV9jaGF0X2lkIjpudWxsfQ.lEIvTw5RlgmG8rWtd5-U-FKlyIEheCH55TzawTFEgMs"   # Gif 3
]

# Variável global para controle da alternância dos GIFs
gif_index = 0

# Função para gerar um horário pagante próximo ao horário atual
def gerar_horario_pagante_proximo():
    agora = datetime.now()  # Obtém o horário atual
    # Adiciona entre 1 e 10 minutos ao horário atual para gerar o próximo horário pagante
    minutos_aleatorios = random.randint(1, 10)
    proximo_horario = agora + timedelta(minutes=minutos_aleatorios)
    return proximo_horario.strftime("%H:%M")  # Formata para "hh:mm"

# Função assíncrona para enviar mensagens e GIFs aleatórios
async def enviar_mensagens():
    global gif_index  # Usar a variável global para controlar o índice do GIF
    while True:
        try:
            mensagem = random.choice(mensagens) + f"\n📌 Próximo horário pagante: {gerar_horario_pagante_proximo()}"
            gif_url = gifs[gif_index]
            
            # Envia a mensagem
            await bot.send_message(chat_id=CHAT_ID, text=mensagem)
            # Envia o gif
            await bot.send_animation(chat_id=CHAT_ID, animation=gif_url)
            print(f"✅ Mensagem e gif enviados: {mensagem}")

            # Alterna o índice do gif para o próximo
            gif_index = (gif_index + 1) % len(gifs)

        except Exception as e:
            print(f"❌ Erro ao enviar mensagem ou gif: {e}")

        # Tempo aleatório entre 5 e 15 minutos (300s - 900s)
        tempo_espera = random.randint(300, 900)
        print(f"⏳ Próxima mensagem em {tempo_espera // 60} minutos...")
        await asyncio.sleep(tempo_espera)

# Iniciar o envio automático de mensagens
if __name__ == "__main__":
    asyncio.run(enviar_mensagens())
