def evaluate_expression(values, expression):
    expression = expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not').replace('XOR', '^').replace('NAND', 'not (a and b)').replace('NOR', 'not (a or b)')
    return eval(expression, {}, values)

def generate_truth_table(variables, expressions):
    print("Truth Table:")
    print('+' + '-'*(len(variables)*5 + len(expressions)*5 + 3) + '+')
    print('| ' + ' | '.join(variables) + ' | ' + ' | '.join(expressions) + ' |')
    print('+' + '-'*(len(variables)*5 + len(expressions)*5 + 3) + '+')

    def recursive_assign(var_list, values):
        if not var_list:
            results = [evaluate_expression(values, expression) for expression in expressions]
            result_str = ' | '.join(str(int(result)) for result in results)
            print('| ' + ' | '.join(str(values[var]) for var in variables) + ' | ' + result_str + ' |')
        else:
            var = var_list[0]
            for val in [0, 1]:
                values[var] = val
                recursive_assign(var_list[1:], values)

    recursive_assign(variables, {})
    print('+' + '-'*(len(variables)*5 + len(expressions)*5 + 3) + '+')

# Prompt for variables
variables = input("Enter variables separated by space: ").split()

# Prompt for expressions
num_expressions = int(input("Enter the number of expressions to be evaluated: "))
expressions = []
for i in range(num_expressions):
    expression = input(f"Enter expression {i+1} to be evaluated: ")
    expressions.append(expression)

# Generate and print the truth table
generate_truth_table(variables, expressions)