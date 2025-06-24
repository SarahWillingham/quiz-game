## Brainstorm Trivia Game
Brainstorm is a Python-based trivia application built with tkinter for the UI. It fetches trivia questions from the Open Trivia Database and lets users test their knowledge with true/false questions in a lightweight desktop interface.

## Note: This project is currently a work in progress (WIP). While support for multiple-choice questions is planned and partially integrated, the UI currently only supports True/False questions.

## Features (Implemented)
Fetches questions dynamically from the Open Trivia Database API

GUI built with Python’s tkinter

Score tracking throughout the session

Adjustable difficulty and category via API URL (partially implemented)

## Planned Features (WIP)
UI functionality for multiple-choice questions (though the choice is offered, it doesn't yet work)

Dropdowns and radio buttons at app launch to select: Number of questions, Category (e.g., History, Science), Question type (True/False or Multiple Choice)

Full support for multiple choice questions

Additional visual feedback and polish

## Technologies Used
Python 3.13, tkinter (standard GUI library), requests (for API calls)

## Getting Started
Clone this repository:

git clone https://github.com/SarahWillingham/quiz-game.git

cd quiz-game

Install dependencies:

pip install -r requirements.txt

Run the application:

python main.py
