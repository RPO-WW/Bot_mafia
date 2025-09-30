# Bot_mafia

<img width="576" height="807" alt="image" src="https://github.com/user-attachments/assets/12dfa710-8946-4a99-a001-7f611610a5d0" />

# Структура проекта
bot/
├── main.py           # точка входа
├── db.py             # работа с базой данных
├── game.py           # логика игры
├── handlers/         # обработчики команд и кнопок
│   ├── start.py
│   ├── lobby.py
│   ├── night.py
│   └── day.py
└── utils.py          # вспомогательные функции
