# CAOS Helper :)
## Helper for Computer Architecture and Operating Systems

This project contains several Python scripts, each serving a specific purpose related to computer science concepts. Below is a brief description of each file:

## Files and Descriptions

### 1. `2scompliment.py`
This script that subtracts or addition two given binary number in 2's compliment.

### 2. `binary-calc.py`
Performs basic arithmetic operations on binary numbers and 2's compliment binary numbers like:
- Addition, subtraction, division and multiplication on binary.
- Addition, subtraction and multiplication on 2's compliment binary.

### 3. `circuit-truth-table.py`
Generates the truth table for a given digital circuit provided these:
- Variables
- Expressions

### 4. `cpu-arrival-time.py`
Simulates CPU scheduling and calculates arrival times of processes given these:
- Number of processes
- CPU time and arrival time for process

### 5. `digital-logic.py`
Evaluates digital logic expressions and outputs the result in a table with multiple rows given:
- Variables & number of variables
- Expressions & number of expressions

### 5.5 `digital-logic-simple.py & digital-logic-advanced.py`
Honestly no reason to use these. Just use `digital-logic.py`

### 6. `disk-access.py`
Simulates disk access patterns and calculates the average time to access a Sector on the disk based on:
- Rotational rate (RPM)
- Average seek time (ms)
- Average number of sectors per track

### 7. `hextable.py`
Converts a given input of multiple hexadecimal representation and generates a hex table with convertations like:
- 1's compliment
- 2's compliment
- Decimal value

### 8. `page-table-size.py`
Calculates the size of a page table for a given memory configuration variables:
- Physical memory (MB)
- Virtual address space (bits)
- Page size (KB)

### 9. `roundrobin.py`
Implements the Round Robin scheduling algorithm for process management based on: 
- Number of processes
- Time quantum
- Arrival time and burst time for the process

### 10. `virtual-memory.py`
Simulates virtual memory management to find the size of the page table given:
- Physical memory (MB)
- Virtual address space (bits)
- Page size (KB)

### 11. `virtual-phys.py`
Finds the physcial address from the virtual address given:
- Virtual address in hex
- Physical page on table entry

### 11.5 `virtual-phys-advanced.py`
Same as the previous, but asks for the given table.

### 12. `disk-capacity.py`
Calculates disk capacity from:
- Platters
- Surfaces per platter
- Cylinders
- Sectors per track

## Usage

Each script can be run individually using Python. For example:
```sh
python 2scompliment.py
