import threading
import time

def worker():
    print(f"Worker {threading.current_thread().name} is starting.")
    time.sleep(2)
    print(f"Worker {threading.current_thread().name} is done.")

threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print("All workers are done.")
