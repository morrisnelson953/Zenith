
#### main.py

```python
#!/usr/bin/env python3
import random

def generate_ascii_art(width=40, height=10):
    # Characters sorted by increasing density for a shading effect
    shades = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']
    art = ""
    for _ in range(height):
        line = "".join(random.choice(shades) for _ in range(width))
        art += line + "\n"
    return art

def main():
    print("Welcome to the Zenith Project!")
    print("Here is your random ASCII art pattern:\n")
    print(generate_ascii_art())

if __name__ == "__main__":
    main()
