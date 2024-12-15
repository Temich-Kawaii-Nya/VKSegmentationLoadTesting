import random

from locust import HttpUser, task, between

from utilities import generate_random_string


class UserAnalytic(HttpUser):
    wait_time = between(1, 5)
    def on_start(self):
        login = generate_random_string(6)
        password =generate_random_string(6)
        self.client.post("/signup", json={"login":login, "password":password})
        self.client.post("/login", json={
            "login":login,
            "password":password
        })
    @task(1)
    def create_user(self):
        self.client.post("/create_user", json={
            "id": 1,
            "subscription_type": "premium",
            "monthly_revenue": 12000,
            "join_date": "2024-01-15T12:00:00Z",
            "last_payment_date": "2024-11-01T12:00:00Z",
            "country": "USA",
            "age": 2,
            "gender": "male",
            "device": "phone",
            "plan_duration": "2025-01-15T12:00:00Z"
        })
    @task(1)
    def read_user_segments(self):
        self.client.get("/read_user_segments", json={"id":1})
    @task(5)
    def read_segment_users(self):
        self.client.get("/read_segment_users", json={"id":1})
    @task(3)
    def create_segment(self):
        self.client.post("/create_segment", json={
            "name" : generate_random_string()
        })
    @task(1)
    def update_segment_users(self):
        self.client.post("/update_segment_users", json={
            "segmentID": random.randint(1, 20),
            "userIDs": [
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20),
                random.randint(1, 20)
            ]
        })
    @task(7)
    def distribure_segments(self):
        name = generate_random_string()
        self.client.post("/create_segment", json={
            "name": name
        })
        self.client.post("/segment_distribution", json={
            "segmentName": name,
            "percent": random.randint(0, 100)
        })
