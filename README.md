
<div align="center">
  <h3 align="center">MSCS532 Assignment 4</h3>
</div>

<!-- CLONING THE REPOSITORY -->
## Cloning the Repository

To get a local copy of this repository, use the following commands:
```sh
# Clone the repository
git clone https://github.com/abhattarai28547/MSCS532_Assignment4.git

# Navigate into the project directory
cd MSCS532_Assignment4
```
<!-- Running the code-->
### Heapsort Implementation

To test the **Heapsort** implementation, execute:
```sh
python heapsort.py
```
This will run the Heapsort algorithm on a sample array and output the sorted result.

To test the **Heapsort** implementation on randomly generated arrays, execute:

```sh
python comparison_sort.py
```
This will run Heapsort along with Quicksort and Merge Sort for performance comparison on arrays of varying sizes and distributions (random, sorted, reverse-sorted).

### Priority Queue Operations

To test the **Priority Queue** implementation using a binary heap, execute:
```sh
python priority_queue.py
```
This script demonstrates core priority queue operations such as task insertion, extraction (max/min), and priority modification.


<!-- CUSTOMIZATION -->
Customization
You can modify the array sizes or task data within the Python scripts for testing different scenarios:

`comparison_sort.py`: Modify the sizes array to test different input `sizes` for sorting algorithms. You can also change the array generation logic in the `generate_test_arrays()` function to customize input distributions.

`priority_queue.py`: Adjust the task list, priorities, and heap size to test different scenarios in the priority queue.


 <!-- SUMMARY OF FINDINGS -->

 
### Summary of Findings
<div> 
  <li>
    **Heapsort**: The Heapsort algorithm showed consistent performance across different array sizes and distributions with time complexity of 𝑂(𝑛log𝑛). However, it was slightly slower compared to Python’s built-in sorting (Timsort).
  </li> 
  <li>
    **Quicksort**: Python's built-in `sorted()` function, based on Timsort, outperformed Heapsort, especially on larger arrays. It was efficient for all input types (random, sorted, reverse-sorted), consistently achieving its best-case performance of 𝑂(𝑛log𝑛).
  </li>
  <li>
    **Merge Sort**: Similar to Quicksort, Merge Sort (also implemented using Python's `sorted()`) was highly efficient and had comparable performance to Timsort. As expected, it performed steadily across all input sizes and types due to its stable time complexity of 𝑂(𝑛log𝑛).
  </li>
  <li>**Priority Queue**: The binary heap-based priority queue operations showed excellent average performance. Insertions and extractions both maintained logarithmic time complexity 𝑂(log 𝑛), demonstrating the suitability of heaps for scheduling and task management applications.
  </li>
</div>

### Instructions:
<ol>
  <li>
    Clone the Repository: Use the provided Git commands to clone the repository and navigate into the project directory.
  </li> 
  <li>
    Run Scripts: Execute the provided Python scripts to test the sorting algorithms and priority queue operations.
  </li> 
  <li>Customize: Modify the input arrays or task lists as needed to explore different test scenarios.
  </li> 
  <li>
    Review Findings: Refer to the summary of findings to understand the performance characteristics observed during the implementation and testing.
  </li>
</ol>

This `README.md` now includes detailed instructions for running the implementations, customizing them, and a summary of the findings.
