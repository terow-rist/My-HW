def longest_job_first(n, burst_times):
    processes = [(i + 1, burst_times[i]) for i in range(n)]
    
    processes.sort(key=lambda x: x[1], reverse=True)

    waiting_times = [0] * n
    turnaround_times = [0] * n
    total_waiting_time = 0
    total_turnaround_time = 0

    for i in range(1, n):
        waiting_times[i] = waiting_times[i - 1] + processes[i - 1][1]
        total_waiting_time += waiting_times[i]

    for i in range(n):
        turnaround_times[i] = processes[i][1] + waiting_times[i]
        total_turnaround_time += turnaround_times[i]

    avg_waiting_time = total_waiting_time / n
    avg_turnaround_time = total_turnaround_time / n

    print("P\tBT\tWT\tTAT")
    for i in range(n):
        print(f"P{processes[i][0]}\t{processes[i][1]}\t{waiting_times[i]}\t{turnaround_times[i]}")
    print(f"Average Waiting Time = {avg_waiting_time:.2f}")
    print(f"Average Turnaround Time = {avg_turnaround_time:.2f}")

def main():
    try:
        n = int(input("Enter the number of processes: "))
        if n <= 0:
            print("Number of processes must be a positive integer.")
            return
        
        burst_times = []
        for i in range(n):
            bt = int(input(f"Burst time for P{i + 1}: "))
            if bt <= 0:
                print("Burst time must be a positive integer.")
                return
            burst_times.append(bt)
        
        longest_job_first(n, burst_times)

    except ValueError:
        print("Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
