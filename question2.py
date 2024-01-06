import threading

def reverse_number(num):
    return int(str(num)[::-1])

def printer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
    return wrapper

@printer
def calculate_reverse_and_print(num):
    return reverse_number(num)

def main():
    numbers = input("Istalgan sonlarni probel bilan kiriting: ").split()
    numbers = [int(num) for num in numbers]
    
    threads = []
    for num in numbers:
        thread = threading.Thread(target=calculate_reverse_and_print, args=(num,))
        thread.start()
        threads.append(thread)
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    main()