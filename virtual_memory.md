# Virtual Memory & Physical Address: A Step-by-Step Guide

## Definitions

1. **Virtual Memory**:
    - A memory management capability by the OS Kernel, which compensates for physical memory shortages by offloading RAM contents to disk storage.
    - Think of it as uploading your photos to the cloud when your phone runs out of space.

2. **Physical Memory**:
    - The actual RAM module installed in the PC.

3. **Page Table**:
    - A structure that stores the mapping between virtual and physical addresses.

4. **Virtual Address**:
    - An address in the virtual space. It consists of a page number and an offset.
    - Think of the page number as the street and the offset as the house number.

5. **Physical Address**:
    - A byte's location in the computer's RAM.

6. **Valid Bit**:
    - Indicates if the associated memory page is in physical memory (`1`) or not (`0`).

7. **Page**:
    - A fixed-length block of virtual memory, defined by the OS's virtual memory management.

8. **Offset**:
    - A specific location within a page. 

    ```java
    // A Java example to understand 'offset'
    byte[] Page1 = new byte[1024];

    for (int i = 0; i < 1024; i++) {
        Page1[i] = (byte) i;
    }

    int offset = 626;
    byte dataAtOffset = Page1[offset];
    System.out.println("Data at offset " + offset + " is: " + dataAtOffset);
    ```

## Procedure

### 1. Understand the Translation Table

| Valid Bit | Physical Page |
|-----------|---------------|
| 0         | 7             |
| 1         | 9             |
| 0         | 3             |
| 1         | 2             |

From the table:
| Page Number (Virtual) | In Memory? |
|-----------------------|------------|
| 0                     | No         |
| 1                     | Yes        |
| 2                     | No         |
| 3                     | Yes        |

### 2. Convert Hexadecimal to Binary

The address `0xE72` translates to `1110 0111 0010` in binary. 

### 3. Extract Page Number & Offset

From the 12-bit binary, the first 2 bits (`11`) represent the page number (3 in decimal), and the remaining 10 bits (`10011 10010`) represent the offset (626 in decimal).

### 4. Look Up Physical Page

The third entry in the page table (0-based index) shows a valid bit of `1` and a physical page of `2`.

### 5. Construct the Physical Address

Calculate the physical address using:

    Physical Address = (Physical Page Number × Bytes Per Page) + Offset

Given:
- Physical Page Number = 2
- Bytes Per Page = 1024
- Offset = 626

The physical address is `2674` in decimal notation.
