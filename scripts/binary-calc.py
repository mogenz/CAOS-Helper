def binary_to_int(binary_str):
    """Convert a binary string to an integer."""
    return int(binary_str, 2)

def int_to_binary(value, bits):
    """Convert an integer to a binary string with a specified bit length."""
    binary_str = bin(value)[2:]  # Get the binary representation without '0b' prefix
    if len(binary_str) > bits:
        bits = len(binary_str)
    return binary_str.zfill(bits)

def twos_complement(value, bits):
    """Convert an integer to its two's complement binary representation."""
    if value >= 0:
        return int_to_binary(value, bits)
    else:
        return int_to_binary((1 << bits) + value, bits)

def twos_complement_to_int(binary_str):
    """Convert a two's complement binary string to an integer."""
    value = binary_to_int(binary_str)
    bits = len(binary_str)
    if binary_str[0] == '1':
        value -= 1 << bits
    return value

def binary_calculator():
    """Perform basic binary calculations."""
    while True:
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Two's complement addition")
        print("6. Two's complement subtraction")
        print("7. Two's complement multiplication")
        print("8. Go back to main menu")
        
        choice = input("Enter choice: ")
        
        if choice == '8':
            break

        bin1 = input("Enter first binary number: ")
        bin2 = input("Enter second binary number: ")
        bits = max(len(bin1), len(bin2)) + 1  # Ensure we have enough bits for the result

        if choice in ['1', '2', '3', '4']:
            int1 = binary_to_int(bin1)
            int2 = binary_to_int(bin2)
            
            if choice == '1':
                result = int1 + int2
                operation = '+'
            elif choice == '2':
                result = int1 - int2
                operation = '-'
            elif choice == '3':
                result = int1 * int2
                operation = '*'
            elif choice == '4':
                if int2 == 0:
                    print("Error: Division by zero.")
                    continue
                result = int1 // int2
                operation = '/'
            
            result_binary = int_to_binary(result, bits)
            print(f"{bin1} ({int1}) {operation} {bin2} ({int2}) = {result_binary} ({result})")
        
        elif choice in ['5', '6', '7']:
            int1 = twos_complement_to_int(bin1)
            int2 = twos_complement_to_int(bin2)

            if choice == '5':
                result = int1 + int2
                operation = '+'
            elif choice == '6':
                result = int1 - int2
                operation = '-'
            elif choice == '7':
                result = int1 * int2
                operation = '*'

            result_binary = twos_complement(result, bits)
            print(f"{bin1} ({int1}) {operation} {bin2} ({int2}) (two's complement) = {result_binary} ({result})")

def twos_complement_calculator():
    """Convert to two's complement."""
    while True:
        print("\nChoose operation:")
        print("1. Convert integer to two's complement binary")
        print("2. Convert two's complement binary to integer")
        print("3. Go back to main menu")
        
        choice = input("Enter choice: ")
        
        if choice == '3':
            break
        
        if choice == '1':
            value = int(input("Enter integer: "))
            bits = int(input("Enter number of bits: "))
            result = twos_complement(value, bits)
            print(f"Two's complement of {value} with {bits} bits is: {result}")
        
        elif choice == '2':
            binary_str = input("Enter two's complement binary string: ")
            result = twos_complement_to_int(binary_str)
            print(f"Integer value of {binary_str} is: {result}")

def conversion_calculator():
    """Perform various conversions."""
    while True:
        print("\nChoose conversion type:")
        print("1. Binary to Hex")
        print("2. Decimal to Hex")
        print("3. Hex to Binary")
        print("4. Hex to Decimal")
        print("5. Decimal to Binary")
        print("6. Binary to Decimal")
        print("7. Go back to main menu")
        
        choice = input("Enter choice: ")
        
        if choice == '7':
            break
        
        if choice == '1':
            binary_str = input("Enter binary number: ")
            result = hex(int(binary_str, 2))[2:].upper()
            print(f"Hex value of {binary_str} is: {result}")
        
        elif choice == '2':
            decimal_value = int(input("Enter decimal number: "))
            result = hex(decimal_value)[2:].upper()
            print(f"Hex value of {decimal_value} is: {result}")
        
        elif choice == '3':
            hex_str = input("Enter hex number: ")
            result = bin(int(hex_str, 16))[2:]
            print(f"Binary value of {hex_str} is: {result}")
        
        elif choice == '4':
            hex_str = input("Enter hex number: ")
            result = int(hex_str, 16)
            print(f"Decimal value of {hex_str} is: {result}")
        
        elif choice == '5':
            decimal_value = int(input("Enter decimal number: "))
            result = bin(decimal_value)[2:]
            print(f"Binary value of {decimal_value} is: {result}")
        
        elif choice == '6':
            binary_str = input("Enter binary number: ")
            result = int(binary_str, 2)
            print(f"Decimal value of {binary_str} is: {result}")

def main():
    while True:
        print("\nChoose:")
        print("1. Binary calculator")
        print("2. Two's complement converter")
        print("3. Conversion calculator")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '1':
            binary_calculator()
        elif choice == '2':
            twos_complement_calculator()
        elif choice == '3':
            conversion_calculator()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
