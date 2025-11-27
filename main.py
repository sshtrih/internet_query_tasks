from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

import random

app = FastAPI()



@app.get("/ip", response_class=HTMLResponse)
async def real_ip(request: Request):

    forwarded = request.headers.get("X-Forwarded-For")
    if forwarded:
        ip = forwarded.split(",")[0]
    else:
        ip = request.client.host

    html = f"<p>{ip}</p>"
    return html


@app.get("/quote", response_class=HTMLResponse)
async def cipher():
    QUOTES = [
    "Если заблудился в лесу, иди домой.",
    "В жизни всегда есть две дороги: одна — первая, а другая — вторая.",
    "Никогда не сдавайтесь, идите к своей цели! А если будет сложно — сдавайтесь.",
    "Запомни: всего одна ошибка — и ты ошибся.",
    "Делай, как надо. Как не надо, не делай.",
    "Работа — это не волк. Работа — ворк. А волк — это ходить.",
    "Как говорил мой дед, «Я твой дед».",
    "Слово — не воробей. Вообще ничто не воробей, кроме самого воробья.",
    "Работа не волк. Никто не волк. Только волк волк.",
    "Если закрыть глаза, становится темно.",
    "Тут — это вам не там.",
]
    return f"<p>{random.choice(QUOTES)[::-1]}</p>"


def random_case(word: str) -> str:
    return "".join(
        ch.upper() if random.random() < 0.5 else ch.lower()
        for ch in word
    )

@app.get("/game", response_class=HTMLResponse)
async def cipher():
    MESSAGE = [
        "И так мой выбор это: ",
        "Пусть это будет: ",
        "А что насчёт: ",
        "Я выбираю: ",
        "А сможешь ли ты победить это: ",
        "Хмм… пожалуй, скажу: ",
        "Ладно, держись, мой вариант: ",
        "Думаю, что это: ",
        "Мой внутренний рандом утверждает: ",
        "Сегодня судьба говорит: ",
        "Мой ассистент подсказывает: ",
        "Ну, удачи… я ставлю на: ",
        "Это было сложное решение, но: ",
        "После долгих раздумий — это: ",
        "Окей, попробуй перебить: ",
        "Пожалуй, выберу: ",
        "Мой секретный алгоритм выдал: ",
        "В этот раз я сыграю так: ",
        "Запоминай — мой ход: ",
        "Настало время легендарного выбора: ",
    ]
    CHOISE = [
        "Камень",
        "Ножницы",
        "Бумага",
    ]

    choice = random_case(random.choice(CHOISE))
    message = random.choice(MESSAGE)

    return f"<p>{message}{choice}</p>"
