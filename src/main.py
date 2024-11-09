import random
import time
from typing import Dict, List, Set
from constants import *

def display_hangman(tries: int) -> str:
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        """
           --------
           |      |
           |      
           |
           |
           |
           -
        """,
        """
           --------
           |      
           |      
           |
           |
           |
           -
        """,
        """
           --------
           |      
           |      
           |
           |
           |
           
        """
    ]
    return stages[min(len(stages)-1, tries)]

def get_difficulty_words(words: List[str]) -> Dict[str, Dict]:
    return {
        'oson': {'lives': 8, 'words': [w for w in words if len(w) <= 5]},
        "o'rta": {'lives': 6, 'words': [w for w in words if 5 < len(w) <= 8]},
        'qiyin': {'lives': 4, 'words': [w for w in words if len(w) > 8]}
    }

def calculate_score(word_length: int, remaining_lives: int, time_taken: int) -> int:
    base_score = word_length * 10
    life_bonus = remaining_lives * 20
    time_bonus = max(0, 100 - time_taken)
    return base_score + life_bonus + time_bonus

def get_hint(word: str, used_letters: Set[str], hint_type: str, category: str) -> str:
    if hint_type == 'harfni ochish':
        unused_letters = [l for l in word if l not in used_letters]
        if unused_letters:
            return f"Ochiq harf: {random.choice(unused_letters)}"
    elif hint_type == 'kategoriya':
        return f"Bu so'z {category} kategoriyasiga tegishli"
    elif hint_type == 'uzunlik':
        return f"So'z {len(word)} ta harfdan iborat"
    return "Ko'mak mavjud emas"

def select_category() -> str:
    print("\nKategoriyani tanlang:")
    for i, cat in enumerate(CATEGORIES.keys(), 1):
        print(f"{i}. {cat}")
    
    while True:
        try:
            choice = int(input("Raqamni kiriting: "))
            if 1 <= choice <= len(CATEGORIES):
                return list(CATEGORIES.keys())[choice-1]
            print("Noto'g'ri raqam! Qaytadan kiriting.")
        except ValueError:
            print("Iltimos, raqam kiriting!")

def select_difficulty(words: List[str]) -> tuple:
    print("\nQiyinlik darajasini tanlang:")
    difficulty_levels = get_difficulty_words(words)
    for i, diff in enumerate(['oson', "o'rta", 'qiyin'], 1):
        print(f"{i}. {diff}")
    
    while True:
        try:
            choice = int(input("Raqamni kiriting: "))
            if 1 <= choice <= 3:
                selected_diff = list(difficulty_levels.keys())[choice-1]
                return selected_diff, difficulty_levels[selected_diff]
            print("Noto'g'ri raqam! Qaytadan kiriting.")
        except ValueError:
            print("Iltimos, raqam kiriting!")

def play_hangman() -> None:
    category = select_category()
    words = CATEGORIES[category]
    difficulty, settings = select_difficulty(words)
    
    word = random.choice(settings['words'])
    lives = settings['lives']
    
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()
    used_tasks = []
    
    start_time = time.time()
    hints_remaining = HINT_COSTS.copy()

    while len(word_letters) > 0 and lives > 0:
        print("\n" + "="*50)
        print(f"Qolgan jonlar: {lives}")
        print(f"Ishlatilgan harflar: {' '.join(used_letters)}")
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print(display_hangman(lives))
        print(f"So'z: {' '.join(word_list)}")
        
        if any(hints_remaining.values()):
            print("\nMavjud ko'maklar:")
            for hint_type, count in hints_remaining.items():
                if count > 0:
                    print(f"- {hint_type} ({count} ta)")
            
            if input("\nKo'mak ishlatishni xohlaysizmi? (ha/yo'q): ").lower() == 'ha':
                hint_type = input("Qaysi ko'makni ishlatmoqchisiz? ").lower()
                if hint_type in hints_remaining and hints_remaining[hint_type] > 0:
                    print(get_hint(word, used_letters, hint_type, category))
                    hints_remaining[hint_type] -= 1
                    continue

        user_letter = input("\nHarf kiriting: ").lower()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("To'g'ri!")
            else:
                lives -= 1
                if lives > 0:
                    available_tasks = [t for t in TASKS if t not in used_tasks]
                    if available_tasks:
                        task = random.choice(available_tasks)
                        used_tasks.append(task)
                        print(f"\nNoto'g'ri! Vazifangiz: {task}")
                        input("Vazifani bajardingizmi? (Enter bosing)")
                    else:
                        print("\nNoto'g'ri! Barcha vazifalar bajarilgan.")
        
        elif user_letter in used_letters:
            print("Bu harf allaqachon ishlatilgan!")
        else:
            print("Noto'g'ri belgi!")

    time_taken = int(time.time() - start_time)
    if lives > 0:
        score = calculate_score(len(word), lives, time_taken)
        print(f"\nTabriklaymiz! '{word}' so'zini topdingiz!")
        print(f"Vaqt: {time_taken} sekund")
        print(f"Ball: {score}")
        
        PLAYER_STATS['games_played'] += 1
        PLAYER_STATS['words_guessed'] += 1
        PLAYER_STATS['total_score'] += score
        PLAYER_STATS['best_score'] = max(PLAYER_STATS['best_score'], score)
    else:
        print(f"\nAfsus! So'z '{word}' edi.")
        PLAYER_STATS['games_played'] += 1

def main():
    print("Hangman o'yiniga xush kelibsiz!")
    
    while True:
        play_hangman()
        
        print("\nSizning statistikangiz:")
        print(f"O'ynalgan o'yinlar: {PLAYER_STATS['games_played']}")
        print(f"Topilgan so'zlar: {PLAYER_STATS['words_guessed']}")
        print(f"Umumiy ball: {PLAYER_STATS['total_score']}")
        print(f"Eng yuqori ball: {PLAYER_STATS['best_score']}")
        
        if input("\nYana o'ynaysizmi? (ha/yo'q): ").lower() != 'ha':
            break

    print("\nO'yin tugadi! Yana kutib qolamiz!")

if __name__ == '__main__':
    main()