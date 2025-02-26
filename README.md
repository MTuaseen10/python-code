# Python Code Repository

This repository contains basic Python code examples.

## The `print()` Function in Python

The `print()` function is one of the most commonly used functions in Python. It outputs text or variables to the console.

### Basic Syntax

```python
print(value1, value2, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

### Parameters

- `value1, value2, ...`: One or more values to be printed
- `sep`: Separator between values (default is space)
- `end`: String appended after the last value (default is newline)
- `file`: Object with a write method (default is sys.stdout)
- `flush`: Whether to forcibly flush the stream (default is False)

### Examples

1. **Basic printing:**
   ```python
   print("Hello World")
   # Output: Hello World
   ```

2. **Multiple arguments:**
   ```python
   print("Hello", "World")
   # Output: Hello World
   ```

3. **Custom separator:**
   ```python
   print("Hello", "World", sep="-")
   # Output: Hello-World
   ```

4. **Custom ending:**
   ```python
   print("Hello", end="!")
   # Output: Hello!
   ```

5. **Printing variables:**
   ```python
   name = "Python"
   print("Hello", name)
   # Output: Hello Python
   ```

6. **Formatted strings (f-strings in Python 3.6+):**
   ```python
   name = "Python"
   print(f"Hello {name}")
   # Output: Hello Python
   ```

### Common Use Cases

- Debugging: Printing variable values to check program state
- User interaction: Displaying information to users
- Output: Showing results of calculations or operations
