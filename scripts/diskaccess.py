def calculate_average_access_time(rotational_rate_rpm, avg_seek_time_ms, avg_sectors_per_track):
    # Calculate rotational rate in seconds
    rotational_rate_s = 60 / rotational_rate_rpm
    
    # Calculate rotation time
    rotation_time_s = 0.5 * rotational_rate_s
    rotation_time_ms = rotation_time_s * 1000  # convert to ms
    
    # Calculate transfer time
    transfer_time_s = rotational_rate_s / avg_sectors_per_track
    transfer_time_ms = transfer_time_s * 1000  # convert to ms
    
    # Calculate average access time
    avg_access_time_ms = avg_seek_time_ms + rotation_time_ms + transfer_time_ms
    
    return avg_access_time_ms, rotational_rate_s, rotation_time_s, rotation_time_ms, transfer_time_s, transfer_time_ms

def main():
    while True:
        print("\nAverage Seek Time Calculator")
        print("1. Enter parameters to calculate access time")
        print("2. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == '2':
            break
        
        if choice == '1':
            rotational_rate_rpm = int(input("Enter rotational rate (RPM): "))
            avg_seek_time_ms = float(input("Enter average seek time (ms): "))
            avg_sectors_per_track = int(input("Enter average number of sectors per track: "))
            
            avg_access_time_ms, rotational_rate_s, rotation_time_s, rotation_time_ms, transfer_time_s, transfer_time_ms = calculate_average_access_time(rotational_rate_rpm, avg_seek_time_ms, avg_sectors_per_track)
            
            print("\nDetailed Calculation:")
            print(f"Rotational rate = {rotational_rate_rpm} RPM = (60 / {rotational_rate_rpm}) = {rotational_rate_s:.3e} s")
            print(f"Rotation time = 1/2 × Rotational rate = 1/2 × {rotational_rate_s:.3e} = {rotation_time_s:.3e} s")
            print(f"Rotation time in ms = {rotation_time_s:.3e} × 1000 = {rotation_time_ms:.3f} ms")
            print(f"Transfer time = Rotational rate × (1 / Average number of sectors/track) = {rotational_rate_s:.3e} × 1/{avg_sectors_per_track} = {transfer_time_s:.3e} s")
            print(f"Transfer time in ms = {transfer_time_s:.3e} × 1000 = {transfer_time_ms:.3f} ms")
            print(f"Average time to access a Sector on the disk = Average seek time + Rotation time + Transfer time")
            print(f"Average time to access a Sector on the disk = {avg_seek_time_ms} ms + {rotation_time_ms:.3f} ms + {transfer_time_ms:.3f} ms = {avg_access_time_ms:.3f} ms")
            print(f"The average time to access a Sector on the disk is {avg_access_time_ms:.3f} ms")
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
