#Connor Schwengel
#10/19/2025

import math

def generate_sin_table(start, end, num_points):
    step = (end - start) / (num_points - 1)
    table = []
    for i in range(num_points):
        x = start + i * step
        y = math.sin(x)
        table.append((x, y))
    return table

def print_table(table):
    print(f"{'x':>10} {'sin(x)':>10}")
    print("-" * 22)
    for x, y in table:
        print(f"{x:10.6f} {y:10.6f}")

def main():
    start = 0.0
    end = 2.0
    num_points = 1000
    sin_table = generate_sin_table(start, end, num_points)
    print_table(sin_table)

if __name__ == "__main__":
    main()