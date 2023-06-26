import ast
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    problem = data.get('problem')

    try:
        # Input Validation
        if not problem or not isinstance(problem, str):
            raise ValueError('Invalid arithmetic problem')

        # Perform calculation
        result = calculate_arithmetic(problem)

        # Secure Logging
        logger.info(f"Calculation: {problem} = {result}")

        # Return successful response
        return jsonify({'result': result})

    except Exception as e:
        # Error Handling
        logger.error(f"Error occurred during calculation: {e}")

        # Return error response
        return jsonify({'error': str(e)}), 400

def calculate_arithmetic(problem):
    try:
        tree = ast.parse(problem, mode='eval')
        result = evaluate_ast(tree.body)
        return result
    except Exception as e:
        raise ValueError('Invalid arithmetic problem')

def evaluate_ast(node):
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        left = evaluate_ast(node.left)
        right = evaluate_ast(node.right)

        if isinstance(node.op, ast.Add):
            return left + right
        elif isinstance(node.op, ast.Sub):
            return left - right
        elif isinstance(node.op, ast.Mult):
            return left * right
        elif isinstance(node.op, ast.Div):
            return left / right

    # Handle other AST nodes or operators as needed

if __name__ == '__main__':
    app.run(port=8000)