from collections import deque

def round_robin_scheduling():
    num_processes = int(input("Enter number of processes: "))
    quantum = int(input("Enter time quantum: "))
    processes = []
    for i in range(num_processes):
        data = input(f"Enter arrival time and burst time for process {i+1} (separated by comma): ")
        arrival_time, burst_time = map(int, data.split(","))
        processes.append([f'P{i+1}', arrival_time, burst_time, arrival_time, burst_time]) # added original arrival and burst times

    # Sort by arrival time
    processes.sort(key=lambda x: x[1])

    time = 0
    sequence = []

    # Transform list to a deque
    process_queue = deque(processes)

    while process_queue:
        process = process_queue.popleft()
        # if the process has arrived
        if process[1] <= time:
            # add min of quantum and burst time to time
            time += min(quantum, process[2])
            # reduce burst time
            process[2] -= min(quantum, process[2])
            sequence.append([process[0], time, 'DONE' if process[2]==0 else process[2]])
            # if process is not done, add it back to the queue
            if process[2] > 0:
                process_queue.append(process)
        else:
            # if the process hasn't arrived, add it back to the queue
            process_queue.append(process)
            # increment time
            time += 1

    return sequence, processes

if __name__ == "__main__":
    sequence, processes = round_robin_scheduling()
    turnArounds = []
    print("Process\tTotal Bursts\tRemaining")
    for s in sequence:
        print(f"{s[0]}\t{s[1]}\t\t{s[2]}")
    
    print("\nTurnaround Times:")
    for process in processes:
        # the last execution time of a process is its completion time
        completion_time = max(time for p, time, _ in sequence if p == process[0])
        turnaround_time = completion_time - process[3]  # Tturnaround = Tcompletion - Tarrival
        turnArounds.append(turnaround_time)
        print(f"{process[0]}: {turnaround_time}")

    # Calculate average turnaround time by summing all turnaround times and dividing by number of processes
    avg_turnaround_time = sum(turnArounds) / len(turnArounds)
    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
