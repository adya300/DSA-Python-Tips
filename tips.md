# DSA Tips in Python

## Tip #1: Remove Duplicates from a List Using a Set
If you want to remove duplicates from a list in Python while maintaining unique values, use a set.

```python
unique_elements = set()
for n in original_list:
    unique_elements.add(n)
result = list(unique_elements)
