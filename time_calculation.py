import time

start_time = time.time()

result = 1
i = 1

while i <= 50:
    result *= i
    i += 1

print('The factorial of 50 is:', result)

end_time = time.time()
execution_time = end_time - start_time
print('Execution time:', execution_time, 'seconds')
