from concurrent.futures import ProcessPoolExecutor
import math

def calculate_factorial(n):
    return math.factorial(n)

def main():

    numbers = [50000, 60000, 70000]

    with ProcessPoolExecutor() as executor:
        results = executor.map(calculate_factorial, numbers)

    for result in results:
        print("Calculated factorial")

# สำคัญมากสำหรับ Windows
if __name__ == "__main__":
    main()