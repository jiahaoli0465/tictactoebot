from flask import Flask, render_template, request, jsonify, session
from game import TTCgame  

app = Flask(__name__)



@app.route('/')
def index():

    return render_template('home.html')

@app.route('/play')
def play():
    global game
    game = TTCgame()  
    return render_template('play.html')

@app.route('/move', methods=['POST'])
def make_move():
    data = request.json
    try:
        bid = int(data.get('bid'))
    except (TypeError, ValueError):

        return 'err'

    game.make_move(bid)

    action = None

    if not game.game_over:
        action, message = game.computer_move()
        if message == 'over':
            return jsonify({
                'action': str(action),
                'message': message

            })

    if game.game_over:
        return jsonify({
            'action': None,
            'message': 'over'
        })
    
        
    return jsonify({
        'action': str(action),
        'message': message

    })

@app.route('/reset', methods=['POST'])
def reset_game():
    game.__init__()  # Reinitialize the game
    return jsonify({"message": "Game reset successfully"})

if __name__ == '__main__':
    app.run(debug=True)
