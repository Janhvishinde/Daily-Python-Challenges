# sort-an-array
# Sort an Array of 0s, 1s, and 2s
This project solves the problem of sorting an array consisting only of `0`, `1`, and `2` in **O(n)** time and **O(1)** space using the **Dutch National Flag Algorithm** 
### Example
**Input:**  
`[0, 1, 2, 1, 0, 2, 1, 0]`  
**Output:**  
`[0, 0, 0, 1, 1, 1, 2, 2]`
## Constraints
- Array length can be up to `10^5`
- Values are limited to `0`, `1`, and `2`
- Sorting must be done in **linear time** and **in-place**
## Approach
We use the **Dutch National Flag Algorithm**:
- Maintain three pointers:  
  - `low` → next position for `0`  
  - `mid` → current element being processed  
  - `high` → next position for `2`
- Swap elements in place until `mid > high`
```bash
python sort_colors.py
