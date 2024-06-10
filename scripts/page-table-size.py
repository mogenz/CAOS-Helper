def calculate_page_table_size(physical_memory_mb, virtual_address_space_bits, page_size_kb):
    # Calculate number of pages
    num_pages = 2 ** virtual_address_space_bits // (page_size_kb * 1024)
    num_pages_exp = virtual_address_space_bits - (page_size_kb * 1024).bit_length() + 1
    
    # Calculate number of bits for physical address
    physical_memory_bytes = int(physical_memory_mb * 1024 * 1024)
    physical_address_bits = physical_memory_bytes.bit_length()
    
    # Calculate number of bits for page frame number
    page_offset_bits = (page_size_kb * 1024).bit_length() - 1
    page_frame_number_bits = physical_address_bits - page_offset_bits
    
    # Calculate size of the page table
    page_table_entries = num_pages
    page_table_entry_size_bits = page_frame_number_bits
    page_table_size_bits = page_table_entries * page_table_entry_size_bits
    page_table_size_bytes = page_table_size_bits / 8  # Convert bits to bytes
    page_table_size_kb = page_table_size_bytes / 1024  # Convert bytes to KB
    
    return num_pages, page_table_entries, physical_address_bits, page_offset_bits, page_frame_number_bits, page_table_size_kb

def main():
    while True:
        print("\nPage Table Size Calculator")
        print("1. Enter parameters to calculate page table size")
        print("2. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '2':
            break
        
        if choice == '1':
            physical_memory_mb = float(input("Enter physical memory (MB): "))
            virtual_address_space_bits = int(input("Enter virtual address space (bits): "))
            page_size_kb = int(input("Enter page size (KB): "))
            
            num_pages, page_table_entries, physical_address_bits, page_offset_bits, page_frame_number_bits, page_table_size_kb = calculate_page_table_size(physical_memory_mb, virtual_address_space_bits, page_size_kb)
            
            print(f"\nNumber of pages = 2^{virtual_address_space_bits} / {page_size_kb * 1024} = 2^{num_pages.bit_length() - 1} = {num_pages}")
            print(f"So, we need 2^{num_pages.bit_length() - 1} entries in the page table.")
            print(f"Physical memory being {physical_memory_mb} MB, a physical address must be {physical_address_bits} bits, and a page address needs {physical_address_bits} - {page_offset_bits} = {page_frame_number_bits} address bits.")
            print(f"So, each page table entry must be at least {page_frame_number_bits} bits.")
            print(f"The size of the page table is approximately {page_table_size_kb:.2f} KB")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
