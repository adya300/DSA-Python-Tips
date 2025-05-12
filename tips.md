# DSA Tips in Python

## Tip #1: Remove Duplicates from a List Using a Set
If you want to remove duplicates from a list in Python while maintaining unique values, use a set.

```python
unique_elements = set()
for n in original_list:
    unique_elements.add(n)
result = list(unique_elements)
```


## Tip #2: Use `enumerate()` Instead of `range(len(...))` for Clean Loops
When you need both the index and value in a loop, use `enumerate()` instead of `range(len(...))`.

```python
for index, value in enumerate(my_list):
    print(index, value)
