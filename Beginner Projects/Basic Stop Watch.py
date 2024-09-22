import time

def stopwatch():
    input("Press Enter to start the stopwatch.")
    start_time = time.time()
    input("Press Enter to stop the stopwatch.")
    elapsed_time = time.time() - start_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
stopwatch()
