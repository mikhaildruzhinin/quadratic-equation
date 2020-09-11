'''Find a number of roots for a quadratic equation'''
from flask import Flask, jsonify, request

app = Flask(__name__)

numbers = {}


def solve_linear(b):
    '''Get a number fo roots for a linear equation'''
    if b == 0:
        return 0
    return 1


def solve_quadratic(a, b, c):
    '''Get a number fo roots for a quadratic equation'''
    d = b ** 2 - 4 * a * c
    if d > 0:
        return 2
    if d == 0:
        return 1
    return 0


def solver(a, b, c):
    '''Get a number fo roots for an equation'''
    if a == 0:
        nroots = solve_linear(b)
    else:
        nroots = solve_quadratic(a, b, c)
    return nroots


@app.route('/grab', methods=['POST'])
def grab_numbers():
    '''Get coeffcs for an equation'''
    global numbers
    request_data = request.get_json()
    numbers = {
        'A': int(request_data['A']),
        'B': int(request_data['B']),
        'C': int(request_data['C']),
    }
    return jsonify(numbers), 201


@app.route('/solve', methods=['GET'])
def solve_equation():
    '''Return number of roots'''
    nroots = solver(numbers['A'], numbers['B'], numbers['C'])
    numbers['Nroots'] = nroots
    return jsonify(numbers), 200

if __name__ == '__main__':
    app.run(port=8000, debug=True)
