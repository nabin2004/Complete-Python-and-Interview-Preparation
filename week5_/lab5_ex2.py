my_list =[]

def get_next_point(step):
    x = float(input(f"Enter the x{step} coordinate: "))
    y = float(input(f"Enter the y{step} coordinate: "))
    return x,y

def cal_distance(p1,p2):
    distance = (((p1)**2)+((p2)**2))**0.5
    return distance


def main():
    x1 = 0 
    y1 = 0  
    step = 1  
    while True:
        x2, y2 = get_next_point(step)
        step += 1
        if x2 == 999 and y2 == 999:
            break
        p1 = (x2-x1)
        p2 = (y2-y1)
        distance_Step = cal_distance(p1, p2)
        my_list.append(distance_Step)
        x1 = x2
        y1 = y2


    step_loop = 1
    print("----------")
    for i in my_list:
        print(f"Step {step_loop}: {i:.2f} units")
        step_loop = step_loop +1
    print("----------")



if __name__ == "__main__":
    main()

total_distance = sum(my_list)
print(f"Total distance travelled by the robot: {total_distance:.2f} units")
