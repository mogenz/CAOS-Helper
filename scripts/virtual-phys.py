def main():
    print("\nVirtual Address to Physical Address Conversion")

    # Step 1: Get the virtual address in hex and convert to decimal
    virtual_address_hex = input("Enter the virtual address in hex (e.g., 0xE72): ").strip()
    virtual_address_dec = int(virtual_address_hex, 16)
    print(f"Virtual address: {virtual_address_hex} = {virtual_address_dec}")

    # Step 2: Divide by 1024 and round down to the closest integer using integer division
    page_table_entry = virtual_address_dec // 1024
    print(f"{virtual_address_dec} / 1024 = {virtual_address_dec / 1024} ~ {page_table_entry}")

    # Step 3: Get the physical page number from the user
    physical_page = int(input(f"Enter the physical page corresponding to page table entry {page_table_entry}: "))

    # Step 4: Calculate the modulo of the decimal value with 1024
    offset = virtual_address_dec % 1024
    print(f"{virtual_address_dec} % 1024 = {offset}")

    # Step 5: Calculate the final physical address
    physical_address = physical_page * 1024 + offset
    physical_address_hex = hex(physical_address).upper()
    print(f"{physical_page} * 1024 + {offset} = {physical_address} = {physical_address_hex}")

if __name__ == "__main__":
    main()
