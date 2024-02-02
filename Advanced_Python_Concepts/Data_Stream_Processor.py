'''
Implement a generator that simulates processing a large data stream. 
This generator will yield processed data in chunks, 
allowing for memory-efficient data processing.
'''

def chucks(data_stream):
    for i in range(0, len(data_stream) - 1, 2):
        yield data_stream[i] + data_stream[i+1]


# Simulated data stream
data_stream = [1,2,3,4,5,6,7,8,9]

# Processing the data stream
for result in chucks(data_stream):
    print(result)