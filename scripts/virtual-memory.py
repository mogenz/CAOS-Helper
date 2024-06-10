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

def main():
    print("Virtual Memory Calculation")
    
    physical_memory_mb = int(input("Enter the physical memory (in MB): "))
    virtual_memory_gb = int(input("Enter the virtual memory (in GB): "))
    page_size_kb = int(input("Enter the page size (in KiB): "))
    tlb_sets = int(input("Enter the number of TLB sets: "))
    tlb_ways = int(input("Enter the TLB associativity (number of ways): "))
    
    results = calculate_virtual_memory_details(physical_memory_mb, virtual_memory_gb, page_size_kb, tlb_sets, tlb_ways)
    
    print("\nResults:")
    for key, value in results.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
