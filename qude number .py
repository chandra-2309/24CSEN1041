for i in range(1, 100):
    if i % 2 == 0:
        continue  # Skip even numbers, go to next iteration
    elif i == 25:
        break     # Exit the loop when i becomes 25
    else:
        pass      # Explicitly do nothing (dummy placeholder)

    # This block runs only for odd numbers before 25
    print(f"{i}^3 = {i**3}")
    output:
    1^3 = 1
3^3 = 27
5^3 = 125
7^3 = 343
9^3 = 729
11^3 = 1331
13^3 = 2197
15^3 = 3375
17^3 = 4913
19^3 = 6859
21^3 = 9261
23^3 = 12167
