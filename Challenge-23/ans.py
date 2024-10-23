people=[("John",18),("Doe",2),("smith",25),("Alice", 22), ("Bob", 17), ("Charlie", 19), ("David", 15), ("Eva", 30)]

adults=[person for person in people if person[1]>=18]

print(f"Adults : \n{adults}")
