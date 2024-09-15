class Task:
    def __init__(self, task_id, priority, arrival_time):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"Task({self.task_id}, Priority: {self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def insert(self, task):
        self.heap.append(task)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        parent_index = (index - 1) // 2
        if index > 0 and self.heap[index].priority > self.heap[parent_index].priority:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            self._bubble_up(parent_index)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_task = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to the root
        self._heapify_down(0)
        return max_task

    def _heapify_down(self, index):
        largest = index
        left = 2 * index + 1
        right = 2 * index + 2

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left
        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != index:
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self._heapify_down(largest)

    def is_empty(self):
        return len(self.heap) == 0
    
    def increase_key(self, index, new_priority):
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority is lower than current priority")
        self.heap[index].priority = new_priority
        self._bubble_up(index)

    def decrease_key(self, index, new_priority):
        if new_priority > self.heap[index].priority:
            raise ValueError("New priority is higher than current priority")
        self.heap[index].priority = new_priority
        self._heapify_down(index)


# Example usage
pq = PriorityQueue()
pq.insert(Task("Task-1", 50, "2024-09-15"))
pq.insert(Task("Task-2", 40, "2024-09-16"))
pq.insert(Task("Task-3", 60, "2024-09-17"))

print("Max task:", pq.extract_max())
print("Remaining heap:", pq.heap)
