import pyperclip

def binary_to_decimal(binary):
    binary = str(binary)
    if binary[0]=='1':
        return -1 * (int(''.join('1' if b == '0' else '0' for b in binary), 2) + 1)
    else:
        return int(binary, 2)

def decimal_to_binary(n, bits=5):
    if n < 0:
        return ''.join('1' if b == '0' else '0' for b in bin(-n)[2:].zfill(bits))[:-1] + '1'
    else:
        return bin(n)[2:].zfill(bits)

def calculate_twos_complement(a, b, operation):
    a_dec = binary_to_decimal(a)
    b_dec = binary_to_decimal(b)
    
    if operation == '+':
        result_dec = a_dec + b_dec
    elif operation == '-':
        result_dec = a_dec - b_dec
    else:
        print("Invalid operation. Please use '+' or '-'.")
        return
    
    result_bin = decimal_to_binary(result_dec)
    
    result_str = f"The result of {a} ({a_dec}) {operation} {b} ({b_dec}) is {result_bin} ({result_dec})"

    return result_str

# Take user input
a = input("Enter the first binary number: ")
b = input("Enter the second binary number: ")
operation = input("Enter the operation (+ or -): ")

# Perform the calculation
result = calculate_twos_complement(a, b, operation)

# Copy the result to the clipboard
pyperclip.copy(str(result))
print(result)