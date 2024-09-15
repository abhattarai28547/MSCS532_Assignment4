import time
import random
from priority_queue import PriorityQueue, Task


def run_priority_queue_test():
    pq = PriorityQueue()
    task_count = 100000  # Large number of tasks for measurable time
    insertion_times = []
    extraction_times = []

    # Insert tasks into the priority queue
    for i in range(task_count):
        task = Task(f"Task-{i}", random.randint(1, 100), f"2024-09-{random.randint(20, 30)}")
        start_time = time.perf_counter()
        pq.insert(task)
        insertion_times.append(time.perf_counter() - start_time)

    # Extract tasks from the priority queue
    for _ in range(task_count):
        start_time = time.perf_counter()
        pq.extract_max()
        extraction_times.append(time.perf_counter() - start_time)

    avg_insertion_time = sum(insertion_times) / task_count
    avg_extraction_time = sum(extraction_times) / task_count

    print(f"Average insertion time: {avg_insertion_time:.8f} seconds")
    print(f"Average extraction time: {avg_extraction_time:.8f} seconds")

# Run the test
run_priority_queue_test()
