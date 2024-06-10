def evaluate_expression(variables, values, expression):
    expression = expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')
    for var, val in zip(variables, values):
        expression = expression.replace(var, str(val))
    return eval(expression)

def generate_truth_table(variables, expressions):
    num_vars = len(variables)
    num_combinations = 2 ** num_vars

    print("Truth Table:")
    header = '| ' + ' | '.join(variables) + ' | Q |'
    print('+' + '-' * (len(header) - 2) + '+')
    print(header)
    print('+' + '-' * (len(header) - 2) + '+')

    for i in range(num_combinations):
        values = [(i >> j) & 1 for j in range(num_vars)]
        results = [evaluate_expression(variables, values, expr) for expr in expressions[:-1]]
        q_expression = expressions[-1]
        for j, result in enumerate(results):
            q_expression = q_expression.replace(f'Q{j+1}', str(int(result)))
        q_expression = q_expression.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')  # Ensure final Q expression is correct
        q = eval(q_expression)
        result_str = str(int(q))
        values_str = ' | '.join(str(val) for val in values)
        print(f'| {values_str} | {result_str} |')

    print('+' + '-' * (len(header) - 2) + '+')

def main():
    print("\nDefine the expressions for the logic gates.")
    num_vars = int(input("Enter the number of variables: "))
    variables = [input(f"Enter name for variable {i+1} (e.g., A, B, C): ").strip().upper() for i in range(num_vars)]
    
    num_expressions = int(input("Enter the number of intermediate expressions: "))
    expressions = [input(f"Enter expression for Q{i+1} (e.g., A AND (NOT B) AND C): ").strip().upper() for i in range(num_expressions)]
    expressions.append(input("Enter expression for Q (e.g., Q1 OR Q2 OR Q3 OR Q4): ").strip().upper())

    generate_truth_table(variables, expressions)

if __name__ == "__main__":
    main()
