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
    print(f"Processing job: {job}")
    # Simulate the time to send a push notification
    time.sleep(1)

def main():
    print("Worker started...")
    while True:
        job = redis_client.lpop(QUEUE_NAME)
        if job:
            process_job(job)
        else:
            print("No jobs in queue. Waiting...")
            time.sleep(5)

if __name__ == "__main__":
    main()