import pyperclip

# Function to convert hex to decimal
def hex_to_dec(hex_val):
    return int(hex_val, 16)

# Function to convert hex to 8-bit binary
def hex_to_bin(hex_val):
    return format(int(hex_val, 16), '08b')

# Function to find decimal 1's complement of binary number
def ones_complement(bin_val):
    ones_comp = ''
    for bit in bin_val:
        ones_comp += '0' if bit == '1' else '1'
    # If the original binary number was negative (starts with '1'), make the 1's complement negative
    return -int(ones_comp, 2) if bin_val[0] == '1' else int(ones_comp, 2)

# Function to find decimal 2's complement of binary number
def twos_complement(bin_val):
    twos_comp = ''
    for bit in bin_val:
        twos_comp += '0' if bit == '1' else '1'
    # Add one to get 2's complement and if the original binary number was negative (starts with '1'), make the 2's complement negative
    twos_comp = int(twos_comp, 2) + 1
    return -twos_comp if bin_val[0] == '1' else twos_comp

# Get the hex values
hex_values = input("Enter the hex values, separated by commas(like: 43,A4,8F etc.): ").split(',')

# Output table header
table_str = "Hex Value\t\tDecimal Value\t\t1's Complement\t\t2's Complement\n"

# Process each hex value
for hex_value in hex_values:
    hex_value = hex_value.strip()  # Remove leading/trailing whitespace
    dec_value = hex_to_dec(hex_value)
    bin_value = hex_to_bin(hex_value)

    if bin_value[0] == '0':
        ones_comp = dec_value
        twos_comp = dec_value
    else:
        ones_comp = ones_complement(bin_value)
        twos_comp = twos_complement(bin_value)

    # Add data to the table string
    table_str += f"{hex_value}\t\t{dec_value}\t\t{ones_comp}\t\t{twos_comp}\n"

# Copy table string to clipboard
pyperclip.copy(table_str)
print("Table copied to clipboard.")
