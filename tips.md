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
```


## Tip #3: Use a Dummy Node to Simplify Linked List Operations
In LeetCode problems, a dummy node helps handle edge cases cleanly.

```python
dummy = ListNode()              # Create a dummy node to act as the fixed starting point
curr = dummy                    # Use a pointer 'curr' to build the new list

while l1 is not None:           
    curr.next = ListNode(l1.val)  # Create a new node with l1's value and link it
    curr = curr.next              # Move curr to the new last node
    l1 = l1.next                  # Move to the next node in the original list

return dummy.next                # Return the real head, skipping the dummy node
```


## Tip #4: Use is_prime after finding prime number pairs... for questions in volving prime number, dont create a list of prime number.
it is slower.

```python
ef is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def get_primes_check(x):
    return [i for i in range(2, x) if is_prime(I)]
```



