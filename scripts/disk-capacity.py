def calculate_disk_capacity(num_platters, num_surfaces_per_platter, num_cylinders, sectors_per_track, bytes_per_sector):
    # Calculate disk capacity
    disk_capacity_bytes = num_platters * num_surfaces_per_platter * num_cylinders * sectors_per_track * bytes_per_sector
    
    # Convert disk capacity to kilobytes, megabytes, gigabytes for better readability
    disk_capacity_kb = disk_capacity_bytes / 1000
    disk_capacity_mb = disk_capacity_kb / 1000
    disk_capacity_gb = disk_capacity_mb / 1000
    
    return {
        "Disk Capacity (Bytes)": disk_capacity_bytes,
        "Disk Capacity (KB)": disk_capacity_kb,
        "Disk Capacity (MB)": disk_capacity_mb,
        "Disk Capacity (GB)": disk_capacity_gb
    }

def main():
    print("\nDisk Capacity Calculator")
    
    num_platters = int(input("Enter the number of platters: "))
    num_surfaces_per_platter = int(input("Enter the number of surfaces per platter: "))
    num_cylinders = int(input("Enter the number of cylinders (tracks per surface): "))
    sectors_per_track = int(input("Enter the average number of sectors per track: "))
    bytes_per_sector = int(input("Enter the number of bytes per sector: "))
    
    results = calculate_disk_capacity(num_platters, num_surfaces_per_platter, num_cylinders, sectors_per_track, bytes_per_sector)
    
    print("\nResults:")
    for key, value in results.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()
