def infinite_movie():
    count = 0
    while True:
        count+=1
        yield f"Refill #{count}"
user1 = infinite_movie()
for _ in range(3):
    print(next(user1))

user2=infinite_movie()
for _ in range(5):
    print(next(user2))