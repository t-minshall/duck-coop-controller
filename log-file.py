import threading
import time

def background_task(name, delay):
    print(f"Background task {name} started...")
    time.sleep(delay)
    print(f"Background task {name} finished!")

# Create the thread
# Use daemon=True so the background task stops automatically if the main program exits
thread = threading.Thread(target=background_task, args=("Worker-1", 4), daemon=True)

# Start the background task
thread.start()

# The main program continues immediately without waiting
print("Main program is doing other things...")
for i in range(3):
    print(f"Main loop: {i}")
    time.sleep(1)

print("Main program finished.")
