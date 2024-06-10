def evaluate_expression(a, b, expression):
    expression = expression.replace('NOT', 'not').replace('AND', 'and').replace('OR', 'or')
    return eval(expression)

def generate_truth_table(a_values, b_values, expression):
    variables = ['a', 'b']

    print("Truth Table:")
    print('+' + '-'*(len(variables)*5+3) + '+')
    print('| ' + ' | '.join(variables) + ' | ' + expression + ' |')
    print('+' + '-'*(len(variables)*5+3) + '+')

    for a, b in zip(a_values, b_values):
        values = {var: val for var, val in zip(variables, (a, b))}
        result = evaluate_expression(a, b, expression)
        print('| ' + ' | '.join(str(val) for val in (a, b)) + ' | ' + str(int(result)) + ' |')

    print('+' + '-'*(len(variables)*5+3) + '+')

# Prompt for input
a_values = input("Enter the values of 'a' separated by commas: ").split(',')
b_values = input("Enter the values of 'b' separated by commas: ").split(',')
expression = input("Enter the expression to be evaluated: ")

# Convert input values to integers
a_values = [int(a.strip()) for a in a_values]
b_values = [int(b.strip()) for b in b_values]

# Generate and print the truth table
generate_truth_table(a_values, b_values, expression)