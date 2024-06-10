def main():
    print("\nVirtual Address to Physical Address Conversion")

    # Step 1: Get the virtual address in hex and convert to decimal
    virtual_address_hex = input("Enter the virtual address in hex (e.g., 0xE72): ").strip()
    virtual_address_dec = int(virtual_address_hex, 16)
    print(f"\nVirtual address: {virtual_address_hex} = {virtual_address_dec}")

    # Step 2: Divide by 1024 and round down to the closest integer using integer division
    page_table_entry = virtual_address_dec // 1024
    print(f"\n{virtual_address_dec} / 1024 = {virtual_address_dec / 1024} ~ {page_table_entry}")

    # Step 3: Get the page table from the user
    num_entries = int(input("\nEnter the number of entries in the page table: "))
    
    valid_bits = []
    physical_pages = []
    
    for i in range(num_entries):
        valid_bit = int(input(f"Enter the valid bit for entry {i}: "))
        physical_page = int(input(f"Enter the physical page for entry {i}: "))
        valid_bits.append(valid_bit)
        physical_pages.append(physical_page)
    
    # Print the page table
    print("\nPage Table:")
    print("Entry\tValid Bit\tPhysical Page")
    for i in range(num_entries):
        print(f"{i}\t{valid_bits[i]}\t\t{physical_pages[i]}")
    
    # Step 4: Find the physical page number
    if valid_bits[page_table_entry] == 1:
        physical_page = physical_pages[page_table_entry]
        print(f"\nPage table entry {page_table_entry} is valid. Physical page: {physical_page}")
    else:
        print(f"\nPage table entry {page_table_entry} is invalid.")
        return
    
    # Step 5: Calculate the modulo of the decimal value with 1024
    offset = virtual_address_dec % 1024
    print(f"\n{virtual_address_dec} % 1024 = {offset}")

    # Step 6: Calculate the final physical address
    physical_address = physical_page * 1024 + offset
    physical_address_hex = hex(physical_address).upper()
    print(f"\n{physical_page} * 1024 + {offset} = {physical_address} = {physical_address_hex}")

if __name__ == "__main__":
    main()
