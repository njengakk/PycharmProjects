
def binary_search(list, element):
    middle = 0
    start= 0
    steps =0
    end = len(list ) 
    while start <= end:
        print("steps", steps, ":", str(list[start:end+1]))
        middle = (start +end) //2
        if element == list(middle):
            return middle
        elif element < list(middle):
            end = middle-1
        else:
            start = middle+1
my_list = [1,2,3,4,5,6,7]
target = 2
binary_search(my_list, target)


    