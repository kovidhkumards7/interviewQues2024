import time
import threading

a = time.time()
def thread():
    time.sleep(5)
    return

t1 = threading.Thread(target=thread)
t2 = threading.Thread(target=thread)

t1.start()
t2.start()

t1.join()
t2.join()

t = abs(a-time.time())
print(f"completed in {t}")

