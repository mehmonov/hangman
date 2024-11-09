from typing import Dict, List

MAX_LIVES = 6
MIN_WORD_LENGTH = 3
HINT_COSTS = {'harfni ochish': 2, 'kategoriya': 1, 'uzunlik': 1}

CATEGORIES: Dict[str, List[str]] = {
    'texnologiya': ['python', 'computer', 'software', 'internet', 'database', 'algorithm'],
    'sport': ['football', 'tennis', 'basketball', 'swimming', 'volleyball', 'hockey'],
    'hayvonlar': ['elephant', 'giraffe', 'penguin', 'dolphin', 'tiger', 'lion'],
    'ovqatlar': ['pizza', 'burger', 'sushi', 'pasta', 'sandwich', 'chocolate']
}

TASKS: List[str] = [
    "10 ta o'tirib turish bajar!",
    "Bir stakan suv ich!",
    "1 daqiqa plank ushla!",
    "5 ta sakra!",
    "Qo'shiq ayt!",
    "Raqs tushib ber!",
    "10 soniyaga ko'zingni yum!",
    "Qo'lingni 20 soniya yuqorida ushlab tur!",
    "3 ta push-up bajar!",
    "Tovushingni o'zgartirib gapir!"
]

PLAYER_STATS = {
    'games_played': 0,
    'words_guessed': 0,
    'total_score': 0,
    'best_score': 0,
    'tasks_completed': 0
}