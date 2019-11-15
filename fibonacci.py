# fibonacci.py

def fib():
    fibs = [1, 2]

    for i in range(1,9):
        next_in_sequence = fibs[i-1]+fibs[i]
        fibs.append(next_in_sequence)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
