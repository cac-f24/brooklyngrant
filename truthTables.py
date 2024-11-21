import argparse
from itertools import product
import re

"""
Takes an expression and try to evaluate it using the given variable values
"""
def evaluateExpression(expression, variable_values):
    # replace logical operators with Python equivalents so it can be evaluated
    expression = expression.replace("⇒", " or not ")  # implication
    expression = expression.replace("⇔", " == ")      # equal truth values
    expression = expression.replace("∧", " and ")     # and
    expression = expression.replace("∨", " or ")      # or
    expression = expression.replace("¬", "not ")      # not

    # replace variables with their truth values
    for variable, value in variable_values.items():
        # use regex to match whole words only (avoid partial matches)
        expression = re.sub(rf'\b{variable}\b', str(value), expression)

    try:
        return eval(expression) # make sure we can evaluate the expression
    except Exception as e:
        raise ValueError(f"Error evaluating the expression '{expression}': {e}")

"""
Generates a truth table for a logical expression
"""
def generateTruthTable(expression):
    """Generates a truth table for a logical expression."""
    # get all unique variables using regex to handle complex expressions
    variables = sorted(set(re.findall(r'\b[A-Za-z]+\b', expression)))

    # generate all possible combinations of truth values
    combinations = list(product([False, True], repeat=len(variables)))

    # Generate the truth table
    truthTable = []
    for combo in combinations:
        variableValues = dict(zip(variables, combo))
        result = evaluateExpression(expression, variableValues)
        truthTable.append((*combo, result))

    # calculate column widths for formatting
    column_widths = [max(len(var), 5) for var in variables] + [6]  # Add 6 for "Result"

    # print the truth table
    header = [var.ljust(width) for var, width in zip(variables + ["Result"], column_widths)]
    print("\nTruth Table for:", expression)
    print(" | ".join(variables + ["Result"]))
    print("-" * (len(variables) * 4 + 10))
    for row in truthTable:
        formatted_row = [str(value).ljust(width) for value, width in zip(row, column_widths)]
        print(" | ".join(formatted_row))

    return truthTable

"""
Main function to parse arguments and generate truth tables
"""
def main():
    parser = argparse.ArgumentParser(description="Generate a truth table for an expression.")
    parser.add_argument(
        "-exp", "--expression", type=str, help="The logical expression to evaluate. Use logical operators: ∧, ∨, ¬, ⇒, ⇔."
    )
    args = parser.parse_args()

    if args.expression:
        # process the provided logical expression
        generateTruthTable(args.expression)
    else:
        # Default expressions from problem if no argument
        expressions = [
            "Smoke ⇒ Smoke",
            "Smoke ⇒ Fire",
            "(Smoke ⇒ Fire) ⇒ (¬Smoke ⇒ ¬Fire)",
            "Smoke ∨ Fire ∨ ¬Fire",
            "((Smoke ∧ Heat) ⇒ Fire) ⇔ ((Smoke ⇒ Fire) ∨ (Heat ⇒ Fire))",
            "(Smoke ⇒ Fire) ⇒ ((Smoke ∧ Heat) ⇒ Fire)",
            "Big ∨ Dumb ∨ (Big ⇒ Dumb)"
        ]
        for expr in expressions:
            generateTruthTable(expr)


if __name__ == "__main__":
    main()