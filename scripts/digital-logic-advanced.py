def evaluate_expression(a, b, c, expression):
    expression = expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not').replace('XOR', '^').replace('NAND', 'not (a and b)').replace('NOR', 'not (a or b)')
    return eval(expression)

def generate_truth_table(a_values, b_values, c_values, expressions):
    variables = ['a', 'b', 'c']

    print("Truth Table:")
    print('+' + '-'*(len(variables)*5+3) + '+')
    print('| ' + ' | '.join(variables) + ' | ' + ' | '.join(expressions) + ' |')
    print('+' + '-'*(len(variables)*5+3) + '+')

    for a, b, c in zip(a_values, b_values, c_values):
        values = {var: val for var, val in zip(variables, (a, b, c))}
        results = [evaluate_expression(a, b, c, expression) for expression in expressions]
        result_str = ' | '.join(str(int(result)) for result in results)
        print('| ' + ' | '.join(str(val) for val in (a, b, c)) + ' | ' + result_str + ' |')

    print('+' + '-'*(len(variables)*5+3) + '+')

# Prompt for input
a_values = input("Enter the values of 'a' separated by commas: ").split(',')
b_values = input("Enter the values of 'b' separated by commas: ").split(',')
c_values = input("Enter the values of 'c' separated by commas: ").split(',')

expressions = []
for i in range(3):
    expression = input(f"Enter expression {i+1} to be evaluated: ")
    expressions.append(expression)

# Convert input values to integers
a_values = [int(a.strip()) for a in a_values]
b_values = [int(b.strip()) for b in b_values]
c_values = [int(c.strip()) for c in c_values]

# Generate and print the truth table
generate_truth_table(a_values, b_values, c_values, expressions)
