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
    "https://cdn.qwenlm.ai/output/74c24795-1c5e-4ef6-bd6a-1b5de9537b38/t2i/023ae085-6fcb-4444-877c-ab36ab1b20ef/0a55771d-91d4-4ed9-91fe-3857aadad94c.png?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXNvdXJjZV91c2VyX2lkIjoiNzRjMjQ3OTUtMWM1ZS00ZWY2LWJkNmEtMWI1ZGU5NTM3YjM4IiwicmVzb3VyY2VfaWQiOiIwYTU1NzcxZC05MWQ0LTRlZDktOTFmZS0zODU3YWFkYWQ5NGMiLCJyZXNvdXJjZV9jaGF0X2lkIjpudWxsfQ.04OEY4-zXzCbfUI1OMLceO_VlIEIaEAtmZUr2C5Ag6A",
    "https://cdn.qwenlm.ai/output/74c24795-1c5e-4ef6-bd6a-1b5de9537b38/t2i/f6f0bc49-6cb8-4523-98fb-d7fb9d4fb7b8/7f81a68e-89e1-41c8-9885-e6effb0a9ac6.png?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXNvdXJjZV91c2VyX2lkIjoiNzRjMjQ3OTUtMWM1ZS00ZWY2LWJkNmEtMWI1ZGU5NTM3YjM4IiwicmVzb3VyY2VfaWQiOiI3ZjgxYTY4ZS04OWUxLTQxYzgtOTg4NS1lNmVmZmIwYTlhYzYiLCJyZXNvdXJjZV9jaGF0X2lkIjpudWxsfQ.kdGpsKMghlrLjuujeTFKpJpKK2KGM_ao3uNCLRkL2I4",
    "https://cdn.qwenlm.ai/output/74c24795-1c5e-4ef6-bd6a-1b5de9537b38/t2i/02c074b0-180b-4516-a324-0c9039b30e32/e2eaeb04-6ab1-4f08-9835-9f1700c43c16.png?key=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXNvdXJjZV91c2VyX2lkIjoiNzRjMjQ3OTUtMWM1ZS00ZWY2LWJkNmEtMWI1ZGU5NTM3YjM4IiwicmVzb3VyY2VfaWQiOiJlMmVhZWIwNC02YWIxLTRmMDgtOTgzNS05ZjE3MDBjNDNjMTYiLCJyZXNvdXJjZV9jaGF0X2lkIjpudWxsfQ.AGT_pjtM1c8vIfryAEMOK5yLQKjtoeEPy8W_-MkCdLI",
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
            link_casa_apostas = "👉 BANCA MOLE: [APOSTE AGORA](https://www.fp-starwars.com/register?id=38771753&currency=BRL&type=2)"

            # Junta a mensagem principal com o link
            mensagem_com_link = f"{mensagem}\n\n{link_casa_apostas}"

            # Criando um botão personalizado para o link da casa de apostas e o botão de chat
            teclado = InlineKeyboardMarkup([
                [InlineKeyboardButton("🔥 MIKUPG777", url="https://www.fp-starwars.com/register?id=38771753&currency=BRL&type=2")],
                [InlineKeyboardButton("🔥 Acesse nosso Chat! 🔥", url=CHAT_LINK)]
            ])

            # Envia a mensagem com os botões
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
