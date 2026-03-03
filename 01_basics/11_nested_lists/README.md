# Nested Lists

## Concept

A nested list is a list that contains other lists as elements. This creates
a two-dimensional (or deeper) structure — the foundation for grids, matrices,
tables, and any data that has both rows and columns.

In AI/ML work you will encounter this constantly: pixel grids, confusion matrices,
weight tables, batches of samples, and adjacency graphs are all nested structures.

## Mental Model

```
matrix = [
    [1, 2, 3],   ← row 0
    [4, 5, 6],   ← row 1
    [7, 8, 9],   ← row 2
]

Access: matrix[row][col]
matrix[1][2] → 6   (row 1, column 2)
```

Think of the outer list as selecting the row, and the inner index as
selecting the column within that row.

## Key Points

- `matrix[r][c]` — row first, column second (same convention as numpy)
- Iterating rows: `for row in matrix`
- Iterating all cells: nested `for row in matrix: for cell in row`
- Creating a grid safely: use a list comprehension — NOT `[[0] * cols] * rows`
  (the `*` trick creates rows that are all the same object)
- Transpose (swap rows and columns): `list(zip(*matrix))`
- Neighbourhood traversal (up/down/left/right): check bounds before accessing

## Common Mistakes

- The `*` copy trap: `grid = [[0] * 3] * 3` — all three rows are the same list.
  Modifying `grid[0][0]` changes ALL rows. Use a comprehension instead:
  `grid = [[0] * 3 for _ in range(3)]`
- Forgetting row/column order: `matrix[col][row]` is a common off-by-one
  conceptual mistake — always think row first
- Assuming all rows have the same length — validate if the data comes from outside

## Interview Angle

*"How do you transpose a matrix in Python?"*
```python
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [list(row) for row in zip(*matrix)]
```
`zip(*matrix)` unpacks the rows as arguments to zip, which then groups
by column position. This is the idiomatic answer.
