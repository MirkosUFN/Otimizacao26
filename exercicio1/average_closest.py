import random as rd

list_num = []

def list_generator():
    for i in range(50):
        number = rd.randint(1, 100)
        list_num.append(number)
    print("LIST:", list_num)

def media():
    return sum(list_num) / len(list_num)

def search_closest():
    avg = media()
    closest = list_num[0]
    
    for x in list_num:
        diff_current = abs(x - avg)
        diff_closest = abs(closest - avg)
        
        if diff_current < diff_closest:
            closest = x
            
    return closest

def show_closests():
    closest = search_closest()
    for i in range(len(list_num)):
        if abs(list_num[i] - closest) <= 3:
            print(list_num[i])

list_generator()
print("MEDIA:",media())
print("CLOSESTS:")
show_closests()
