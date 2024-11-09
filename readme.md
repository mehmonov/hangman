 # Hangman Game 🎮 
 ## Table of Contents 
 - About 
 - Features 
 - Installation 
 - How to Play 
 - Development 
 - License 

## About 
A classic word guessing game built with Python. Players try to guess the word while having fun with interactive tasks. 
 
## Features 

 ### Core Features 
 - Multiple difficulty levels 
 - Word categories 
 - Score system 
 - Hint system 
 - Player statistics 
 
 ### Categories 
 - 💻 Technology 
 - ⚽ Sports 
 - 🦁 Animals 
 - 🍕 Food 
 

 ### Difficulty Levels 

 | Level | Lives | Word Length | 
 |----------|-------|-------------| 
 | Easy | 8 | ≤ 5 letters | 
 | Medium | 6 | 6-8 letters | 
 | Hard | 4 | > 8 letters | 

 ### Hint System 
 - 🔍 Reveal letter (2 available) 
 - 📑 Category hint (1 available) 
 - 📏 Word length (1 available) 
 

 ### Score System 
 
 ```
 score = (word_length × 10) + (remaining_lives × 20) + max(0, 100 - time_taken)
 ```

 ## Installation 
 
 1. Clone the repository: 
 ```bash
 git clone https://github.com/mehmonov/hangman.git  
``` 
```bash
 cd hangman  
```

 2. Run the game: 
 ```bash
 
 python3 main.py  
 ```

 ## How to Play 
 1. Select a category 
 2. Choose difficulty level 
 3. Guess letters one by one 
 4. Complete tasks for wrong guesses 
 5. Use hints when needed 

 ## Development 

 ### Project Structure 
 
 ```
 hangman/
 ├── main.py
 ├── constants.py
 └── README.md 
  ```
 ### Tech Stack 
 - Python 3.6+ 
 - Built-in libraries: 
 - random 
 - time 
 - typing 

 ### Future Plans 

 #### Version 2.0 
 - [ ] Multiplayer mode 
 - [ ] Leaderboard 
 - [ ] New categories 
 - [ ] Sound effects 
 - [ ] GUI version 

 #### Version 3.0 
 - [ ] Online mode 
 - [ ] Extended word database 
 - [ ] Multiple languages 
 - [ ] Game analytics 
 - [ ] Mobile version 

 ## Contributing 
 1. Fork the project 
 2. Create your feature(bla bla bla) branch 
 3. Submit a pull request 

 ## License 
 MIT © [Mehmonov] 
 --- 
 Documentation is subject to updates and improvements. Feel free to contribute! 