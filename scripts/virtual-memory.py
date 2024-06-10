def calculate_virtual_memory_details(physical_memory_mb, virtual_memory_gb, page_size_kb, tlb_sets, tlb_ways):
    # Calculate bits for page offset
    page_size_bytes = page_size_kb * 1024
    bits_page_offset = page_size_bytes.bit_length() - 1
    
    # Calculate bits for virtual address and VPN
    virtual_memory_bytes = virtual_memory_gb * (1024**3)
    bits_virtual_address = virtual_memory_bytes.bit_length() - 1
    bits_vpn = bits_virtual_address - bits_page_offset
    
    # Calculate bits for physical address and PPN
    physical_memory_bytes = physical_memory_mb * (1024**2)
    bits_physical_address = physical_memory_bytes.bit_length() - 1
    bits_ppn = bits_physical_address - bits_page_offset
    
    # Calculate the number of entries in the page table
    entries_page_table = 2 ** bits_vpn
    entries_page_table_exp = bits_vpn
    
    # Output the results
    return {
        "Bits for page offset": bits_page_offset,
        "Bits for VPN": bits_vpn,
        "Bits for PPN": bits_ppn,
        "Entries in page table": f"{entries_page_table} (2^{entries_page_table_exp})",
        "TLB sets": tlb_sets,
        "TLB ways": tlb_ways
    }

def lru_page_replacement(reference_string, frames):
    page_faults = 0
    page_hits = 0
    memory = []
    lru_stack = []
    state = []

    for page in reference_string:
        if page in memory:
            page_hits += 1
            # Move the page to the top of the LRU stack
            lru_stack.remove(page)
            lru_stack.append(page)
        else:
            page_faults += 1
            if len(memory) < frames:
                memory.append(page)
            else:
                # Remove the least recently used page
                lru_page = lru_stack.pop(0)
                memory[memory.index(lru_page)] = page
            lru_stack.append(page)

        # Store the current state of the memory
        state.append(memory.copy())

    return page_hits, page_faults, state

def calculate_page_table_size(physical_memory_mb, virtual_address_bits, page_size_kb):
    # Calculate number of pages
    page_size_bytes = page_size_kb * 1024
    num_pages = 2 ** virtual_address_bits // page_size_bytes
    num_pages_exp = virtual_address_bits - (page_size_bytes.bit_length() - 1)
    
    # Calculate bits for physical address
    physical_memory_bytes = physical_memory_mb * 1024 * 1024
    bits_physical_address = physical_memory_bytes.bit_length() - 1
    
    # Calculate bits for page frame number
    bits_page_offset = page_size_bytes.bit_length() - 1
    bits_page_frame_number = bits_physical_address - bits_page_offset
    
    # Calculate size of the page table
    page_table_entry_size_bits = bits_page_frame_number
    page_table_size_bits = num_pages * page_table_entry_size_bits
    page_table_size_bytes = page_table_size_bits / 8  # Convert bits to bytes
    page_table_size_kb = page_table_size_bytes / 1024  # Convert bytes to KB
    
    return {
        "Number of pages": f"{num_pages} (2^{num_pages_exp})",
        "Bits for physical address": bits_physical_address,
        "Bits for page frame number": bits_page_frame_number,
        "Page table entry size (bits)": page_table_entry_size_bits,
        "Size of the page table (KB)": page_table_size_kb
    }

def main():
    while True:
        print("\nMain Menu")
        print("1. Calculate Virtual Memory Details")
        print("2. Calculate Page Hits and Misses using LRU")
        print("3. Calculate Page Table Size")
        print("4. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '4':
            break
        
        if choice == '1':
            print("\nVirtual Memory Calculation")
            physical_memory_mb = int(input("Enter the physical memory (in MB): "))
            virtual_memory_gb = int(input("Enter the virtual memory (in GB): "))
            page_size_kb = int(input("Enter the page size (in KiB): "))
            tlb_sets = int(input("Enter the number of TLB sets: "))
            tlb_ways = int(input("Enter the TLB associativity (number of ways): "))
            
            results = calculate_virtual_memory_details(physical_memory_mb, virtual_memory_gb, page_size_kb, tlb_sets, tlb_ways)
            
            print("\nResults:")
            for key, value in results.items():
                print(f"{key}: {value}")
        
        elif choice == '2':
            print("\nLRU Page Replacement Calculation")
            reference_string = input("Enter the page reference string (comma-separated): ").split(',')
            reference_string = [int(x.strip()) for x in reference_string]
            frames = int(input("Enter the number of frames: "))
            
            page_hits, page_faults, state = lru_page_replacement(reference_string, frames)
            
            print("\nPage Replacement Process:")
            for frame in range(frames):
                print(f"Frame {frame+1}:", end=" ")
                for page in state:
                    if len(page) > frame:
                        print(page[frame], end=" ")
                    else:
                        print(" ", end=" ")
                print()
            
            print(f"\nNumber of page hits: {page_hits}")
            print(f"Number of page misses: {page_faults}")
        
        elif choice == '3':
            print("\nPage Table Size Calculation")
            physical_memory_mb = int(input("Enter the physical memory (in MB): "))
            virtual_address_bits = int(input("Enter the virtual address space (in bits): "))
            page_size_kb = int(input("Enter the page size (in KiB): "))
            
            results = calculate_page_table_size(physical_memory_mb, virtual_address_bits, page_size_kb)
            
            print("\nResults:")
            for key, value in results.items():
                print(f"{key}: {value}")
        
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
