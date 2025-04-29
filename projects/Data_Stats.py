'''
Name: karar khalil 
**********************************
This program is designed to read a file from a URL or local file,
calculate various statistics such as mean, median, minimum, maximum,
range, and skewness, and display the results to the user.
'''

from urllib import request

TITLE = "Data Statistics Organizer 1.0v"
CONTINUE_PROMPT = "Do this again? [y/N] "
url = "  #  ENTER YOUR URL HERE BETWEEN THE QUOTATION MARK        "

def mean_val(lst):
    avg = sum(lst) / len(lst)
    return avg
    
def Minimum_value(lst):
    mini = min(lst)
    print(f"Minimum: {mini}")

def maximum_value(lst):
    maxi = max(lst)
    print(f"Maximum: {maxi}")
    return maxi
        
def request_info(lst):
    userinput = input("Please enter the file name (for URL) or leave blank to choose a local file: ").strip()
    
    if userinput == "":
        # --- Uncomment below to allow LOCAL FILE READING instead of URL ---
        '''
        local_filename = input("Enter local file name: ")
        with open(local_filename, "r") as f:
            for line in f:
                for num in [float(num) for num in line.strip().split()]:
                    lst.append(num)
        '''
        print("No URL specified. [Currently using URL mode only.]")
        return lst
    else:
        urls = url + userinput
        with request.urlopen(urls) as response:
            for line in response:
                for num in [float(num) for num in line.decode("utf-8").strip().split()]:
                    lst.append(num)
        return lst
    
def range_value(lst):
    range_val = max(lst) - min(lst)
    print(f"Range Value: {range_val}")
    return range_val

def median_value(lst):
    lst.sort()
    middle = len(lst) // 2
    if not len(lst) % 2:
        median = (lst[middle - 1] + lst[middle]) / 2.0
    else:
        median = lst[middle]
    return median 
    
def skew_value(lst):
    mean = mean_val(lst)
    median = median_value(lst)
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    if abs(mean - median) / max(mean, median) < 1e-6:
        print("Skew status: zero")
    elif median < mean:
        print("Skew status: Left")
    else:
        print("Skew status: Right")

def process():
    lst = []
    URl_data = request_info(lst)
    mean = mean_val(lst)
    Minimum_val = Minimum_value(lst)
    maximum_val = maximum_value(lst)
    range_of_val = range_value(lst)
    median_val = median_value(lst)
    skew = skew_value(lst)

def do_this_again(prompt):
    do_over = input(prompt)
    return do_over.strip().lower() == 'y'

def main():
    print(f"Welcome to {TITLE}")
    while True:
        process()
        if not do_this_again(CONTINUE_PROMPT):
            break
    print(f"Thank you for using {TITLE}")

if __name__ == "__main__":
    main()