#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int pid;
    int arrival_time;
    int burst_time;
    int priority;
} Process;

int main() {
    int n, i, j;
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    Process *processes = (Process *)malloc(n * sizeof(Process));

    for(i=0; i<n; i++) {
        printf("Enter pid, arrival time, burst time and priority for process %d: ", i+1);
        scanf("%d %d %d %d", &(processes[i].pid), &(processes[i].arrival_time), &(processes[i].burst_time), &(processes[i].priority));
    }

    // Perform priority algorithm here
    int current_time = 0;
    for(i=0; i<n; i++) {
        if(processes[i].arrival_time <= current_time) {
            printf("Process %d is executed at time %d\n", processes[i].pid, current_time);
            current_time += processes[i].burst_time;
        } else {
            int remaining_time = processes[i].arrival_time - current_time;
            printf("Process %d is executed at time %d and takes %d units to execute.\n", processes[i].pid, processes[i].arrival_time, remaining_time);
            current_time += remaining_time + processes[i].burst_time;
        }
    }

    free(processes);

    return 0;
}