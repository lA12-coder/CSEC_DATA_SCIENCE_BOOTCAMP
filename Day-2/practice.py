import numbers,math
def get_stats(data):
    if not all(isinstance(x,numbers.Number) for x in data):
        return "Error: All elements of the data must be numbers"
    mean  = sum(data)/len(data)
    data.sort()
    if len(data)%2!=0:
        median = data[len(data)//2]
    else:
        median = data[len(data)//2 -1 ] + data[len(data)//2]
        median = median/2
    return f"Mean: {mean} and Median: {median}"

def get_variance(data):
    if not data:
        return    
    if not all(isinstance(x,numbers.Number) for x in data):
        return "Error: All elements of the data must be numbers"
    if len(data)<2:
        print("Error: Need more data point for a variance")
    mean = sum(data)/len(data)
    data = [(x-mean)**2 for x in data]
    variance = sum(data)/len(data)
    
    return f"Variance: {variance} and Standard Deviation: {math.sqrt(variance)}"



data = [12, 15, 20, 22, 18, 30, 25, 17, 19, 21]
print(get_stats(data))
print(get_variance(data))



        