def calculate_order_and_response_time(processes):
    # Sort processes by arrival time
    processes.sort(key=lambda x: x[1])
    
    # Initialize list for process order and response times
    process_order = []
    response_times = []

    # Initialize current_time
    current_time = processes[0][1]
    
    while processes:
        # Check all processes that have arrived up to current_time and pick the shortest job
        available_processes = [p for p in processes if p[1] <= current_time]
        if available_processes:
            shortest_process = min(available_processes, key=lambda x: x[2])
            processes.remove(shortest_process)
            
            process_order.append(shortest_process[0])
            
            response_time = current_time - shortest_process[1]
            response_times.append(response_time)
            
            # Update current_time (add burst time of the shortest process)
            current_time += shortest_process[2]
        else:
            # If no process is available, increment current_time
            current_time += 1

    return process_order, response_times

def sjf_scheduling():
    num_processes = int(input("Enter number of processes: "))
    processes = []
    for i in range(num_processes):
        data = input(f"Enter CPU time and arrival time for process {i+1} (separated by comma): ")
        cpu_time, arrival_time = map(int, data.split(","))
        processes.append((i+1, arrival_time, cpu_time))

    process_order, response_times = calculate_order_and_response_time(processes)

    # Take the average of response times
    avg_response_time = sum(response_times) / len(response_times)

    print("Order of process execution:", process_order)
    print("Avg: Response times: " + str(avg_response_time) + "ms")

if __name__ == "__main__":
    sjf_scheduling()
