🎶 Biridins Music Bot

Um bot de música feito em Python, simples, leve e com som de respeito.
Nascido no Paraná 🇧🇷, criado pra deixar teu Discord mais animado.

🚀 Sobre o projeto

O Biridins Music Bot toca música direto do YouTube usando yt_dlp e FFmpeg.
A ideia aqui é fazer o básico bem feito: sem frescura, sem lag, só som limpo e comando que funciona.

Feito pra quem quer um bot confiável, com código claro e fácil de mexer.

🧩 O que ele faz

✅ Toca música do YouTube (link ou nome)
✅ Usa FFmpeg pra garantir qualidade de áudio top
✅ Se cair, tenta reconectar sozinho
✅ Tem comando pra parar e sair do canal
✅ Configuração bem simples via .env ou config.json

💬 Comandos
Comando	O que faz
.play <nome ou link>	Toca a música que tu pediu
.stop	Para tudo e desconecta o bot

💡 O prefixo padrão é !, mas dá pra mudar no arquivo de config.

⚙️ Como rodar o bicho
1️⃣ Pré-requisitos

Python 3.10+ (instalado certinho)

FFmpeg configurado no PATH

Pacotes Python:

pip install discord.py yt-dlp

2️⃣ Configura o token

Cria um arquivo config.json com:

{
  "token": "SEU_TOKEN_AQUI",
  "prefix": "!"
}

3️⃣ Bora rodar
python main.py


Se tudo estiver certo, o bot vai aparecer online e pronto pra tocar som 🎧

📂 Estrutura
📦 biridins-music-bot/
├── main.py         # Onde o bot nasce
├── music.py        # Os comandos de música
├── utils.py        # Coisinhas auxiliares (tipo o FFmpeg)
├── .env            # Token e prefixo (não sobe)
└── README.md       # Esse arquivo aqui


👨‍💻 Feito por

Feito com café e umas boas horas de código por mim Henrique Kenzo.

📜 Licença

Código aberto, estilo MIT, usa à vontade, só não esquece de dar aquele crédito 😄

🌟 Curtiu meu mano?

Dá uma ⭐ no repo e espalha o som.
Se quiser trocar ideia, abrir issue ou sugerir melhoria, tamo junto 💬"# BotDiscord_Music" 
"# BotDiscord_Music" 
