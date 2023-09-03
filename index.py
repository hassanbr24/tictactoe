from flask import Flask, request, jsonify

app = Flask(__name__)

# Variables globales para el estado del juego y el jugador actual
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Ruta para obtener el estado actual del tablero
@app.route('/board', methods=['GET'])
def get_board():
    return jsonify(board)

# Ruta para realizar un movimiento
@app.route('/play', methods=['POST'])
def play():
    global current_player

    data = request.get_json()
    row = data.get('row')
    col = data.get('col')

    # Verificar si la casilla está vacía y si el movimiento es válido
    if not (0 <= row < 3 and 0 <= col < 3) or board[row][col] != ' ':
        return jsonify({'message': f'Jugador {current_player} ha realizado un Movimiento invalido'}), 400

    # Realizar el movimiento
    board[row][col] = current_player

    # Verificar si hay un ganador o empate
    winner = check_winner()
    if winner:
        return jsonify(board, {'message': f'El jugador {winner} ha ganado'}), 200, reset_board()

    if ' ' not in [cell for row in board for cell in row]:
        return jsonify(board, {'message': 'Empate'}), 200, reset_board()

    # Cambiar al siguiente jugador
    current_player = 'X' if current_player == 'O' else 'O'
    return jsonify(board)

# Ruta para reiniciar el tablero y comenzar una nueva partida
@app.route('/new_game', methods=['POST'])
def new_game():
    reset_board()
    return jsonify({'message': 'Nueva partida iniciada'}), 200

# Función para verificar si hay un ganador
def check_winner():
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Función para reiniciar el tablero
def reset_board():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

if __name__ == '__main__':
    app.run(debug=True)
