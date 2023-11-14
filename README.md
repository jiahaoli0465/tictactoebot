
# Tic-Tac-Toe AI: MCTS Flask Application

## Introduction

Welcome to the Tic-Tac-Toe AI Project! This application is a web-based Tic-Tac-Toe game that features an AI opponent powered by a Monte Carlo Tree Search (MCTS) algorithm. Developed using Flask, a popular Python web framework, this project showcases a combination of web development skills and AI implementation.

I implemented this game as a short project to test MCTs out while I was researching methods to be used for an ML/AI chess bot hackathon. 

Originally the game ran in console but I refractored it to be used via frontend!

## Features

- **Interactive Web-based Tic-Tac-Toe Game**: Play against a challenging AI opponent.
- **AI Opponent Using MCTS**: Experience playing against an AI that uses the Monte Carlo Tree Search algorithm to make decisions.
- **Flask Backend**: The server-side logic is implemented in Python using the Flask framework.
- **State Management**: Efficient handling of game state between client-server interactions.

## Installation

To get this project running on your local machine, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone [URL of the repository]

   cd [repository name]

   python -m venv venv

   source venv/bin/activate  

   pip install -r requirements.txt

   flask run


On Windows use `venv\\Scripts\\activate` instead

Access the application at http://127.0.0.1:5000/ in your web browser.

## Usage
After accessing the application, you can start a new game by clicking the "Start Game" button. During the game, you will play as "X" and the AI as "O". After each move, the AI calculates its move using the MCTS algorithm. The game ends when either player wins or the board is full.

## Project Structure
- app.py: The main file that runs the Flask application and defines routes.
- game/: This directory contains the logic for the Tic-Tac-Toe game and the MCTS implementation.
- templates/: HTML files for the frontend.
- static/: Contains CSS and JavaScript files for frontend interactivity.
  
## Technologies Used
- Python: For backend development and MCTS implementation.
- Flask: A lightweight WSGI web application framework in Python.
- HTML/CSS/JavaScript: For frontend development.
- Axios: For handling asynchronous HTTP requests.


### Author
- Jiahao Li

### Reference used
- https://www.youtube.com/watch?v=wuSQpLinRB4&ab_channel=freeCodeCamp.org