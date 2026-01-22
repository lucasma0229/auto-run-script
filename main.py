from datetime import datetime
import random

now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
print("Hello from GitHub Actions!")
print("Time:", now)
print("Random:", random.randint(1, 1000000))
