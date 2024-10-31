import time
import redis
import os

# Redis configurations
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
QUEUE_NAME = "notification_queue"

# Initialize Redis connection
redis_client = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def process_job(job):
    print(f"Processing job: {job}", flush=True)
    # Simulate the time to send a push notification
    time.sleep(20)

def main():
    print("Worker started...", flush=True)
    while True:
        job = redis_client.blpop(QUEUE_NAME, 100)
        if job:
            process_job(job)
        else:
            print("No jobs in queue. Waiting...", flush=True)
            time.sleep(5)

if __name__ == "__main__":
    main()
