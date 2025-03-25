import time
import random
import asyncio
from telegram import Bot
from datetime import datetime, timedelta, timezone

# Configurações do bot
TOKEN = "7322530159:AAGp7V6UZ2ICK4478wnaUaTQTf_kmh9swlo"  # Token do BotFather
CHAT_ID = "-1002663067223"  # ID do canal do Telegram

# Inicializa o bot
bot = Bot(token=TOKEN)

# Mensagens motivacionais para apostas
mensagens = [
    "🔥 *A banca está chamando!* Esse horário está *PAGANDO DEMAIS!* 💰🔥 Não perca tempo, faça sua aposta agora e aproveite o momento certo!",
    "⚡️ Tá rolando *chuva de GREEN!* 🌧💵 Aquele momento raro chegou, e só quem é esperto lucra agora! Entra no jogo antes que seja tarde!",
    "🚀 *Dinheiro rápido e fácil?* 🤑💸 Esse horário tá *INSANO!* Quem apostou já está lucrando, e você vai ficar de fora?",
    "💸 Só os *mestres da aposta* sabem os segredos da banca... e *AGORA* é um deles! ⏳💰 Faça sua entrada e garanta o seu lucro!",
    "📈 *GRANA NO BOLSO* ou arrependimento depois? 🎲💵 Esse horário é quente e já tá pagando pesado! Se liga e faz a tua!",
    "💎 Oportunidade de *OURO* na mesa! 🏆💰 Tá pagando bem, e só os mais rápidos vão lucrar! Entra agora e faz teu jogo!",
    "🔥 *Hora da virada!* Quem não aposta, não ganha! 🎰💵 Agora é o momento de fazer a banca trabalhar para você!",
    "⏳ Quem aposta agora, ri depois! 😏💰 O sinal tá forte, a banca tá mole... será que você vai deixar passar?",
    "⚠️ *ALERTA GREEN!* 🚨💵 As odds estão absurdas e a chance de lucrar é REAL! Quem pegar esse horário vai sorrir no final!",
    "🎯 *Alvo certo!* 📊📈 As análises confirmam: esse é o momento certo para meter a aposta e buscar o lucro! Tá esperando o quê?",
    "🔥 *NÃO É SORTE, É ESTRATÉGIA!* 📊💰 Quem tá ligado sabe que esse é um horário *PAGANTE!* Entra agora e aproveita!",
    "💵 Ganhar dinheiro sem sair de casa? Simples! 🌎💰 As odds estão perfeitas agora. Faz tua entrada antes que passe a chance!",
    "🏆 Os melhores apostadores já sabem... e você? 🎲💰 Não perca essa *OPÇÃO DE LUCRAR AGORA!* O jogo tá aberto, aproveita!",
    "🚨 *Banca solta!* 💰💥 A casa tá distribuindo! É agora ou nunca! Se joga e garante o teu!"
]

# Lista de jogos
jogos = [
    "Dragão e Tigre",
    "Coelho e Touro",
    "Tigre Sortudo e Tigre",
    "Cobra"
]

# Caminho correto da imagem no seu sistema
caminho_imagem = "C:/Users/03594901238/Desktop/bot/miku.jpeg"

# Função para gerar um horário pagante próximo ao horário atual no fuso horário do Brasil (UTC-3)
def gerar_horario_pagante_proximo():
    agora = datetime.now(timezone.utc)  # Obtém o horário UTC usando timezone-aware datetime
    # Ajusta para o fuso horário de Brasília (UTC-3)
    agora_brasil = agora - timedelta(hours=3)
    
    # Adiciona entre 1 e 10 minutos ao horário atual para gerar o próximo horário pagante
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

            # Envia a mensagem com o link da casa de apostas
            await bot.send_message(chat_id=CHAT_ID, text=mensagem_com_link, parse_mode="Markdown")
            
            # Envia a imagem localmente
            with open(caminho_imagem, "rb") as foto:
                await bot.send_photo(chat_id=CHAT_ID, photo=foto)

            print(f"✅ Mensagem e imagem enviadas: {mensagem_com_link}")

        except Exception as e:
            print(f"❌ Erro ao enviar mensagem ou imagem: {e}")

        # Tempo aleatório entre 5 e 15 minutos (300s - 900s)
        tempo_espera = random.randint(300, 900)
        print(f"⏳ Próxima mensagem em {tempo_espera // 60} minutos...")
        await asyncio.sleep(tempo_espera)

# Iniciar o envio automático de mensagens
if __name__ == "__main__":
    asyncio.run(enviar_mensagens())
