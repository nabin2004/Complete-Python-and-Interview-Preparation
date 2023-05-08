def get_data():
    houses = []
    for i in range(7):
        num = int(input(f"Please enter the number of houses with {i} occupants: "))
        houses.append(num)
    num = int(input("Please enter the number of houses with 6+ occupants: "))
    houses.append(num)
    return houses

def cal_percentage(h0, h1, h2, h3, h4, h5, h6, h6plus):
    total = sum([h0, h1, h2, h3, h4, h5, h6, h6plus])
    p0 = round(h0/total*100, 1) 
    p1 = round(h1/total*100, 1)
    p2 = round(h2/total*100, 1)
    p3 = round(h3/total*100, 1)
    p4 = round(h4/total*100, 1)
    p5 = round(h5/total*100, 1)
    p6 = round(h6/total*100, 1)
    p6plus = round(h6plus/total*100, 1)
    return f"{p0:.1f}%", f"{p1:.1f}%", f"{p2:.1f}%", f"{p3:.1f}%", f"{p4:.1f}%", f"{p5:.1f}%", f"{p6:.1f}%", f"{p6plus:.1f}%"


def display_result(h0, h1, h2, h3, h4, h5, h6, h6plus, p0, p1, p2, p3, p4, p5, p6, p6plus):
    print(f'{" occupants: ":<15} {0:<10} {1:<9} {2:<9} {3:<9} {4: <9} {5:<9} {6:<9} {">6"}')
    print(f'{" No.Houses:": <15} {h0: <10} {h1: <9} {h2: <9} {h3: <9} {h4:<9} {h5: <9} {h6:<9} {h6plus}')
    print(f'{"percentage: ": <12} {p0:<10}{p1: <9.5} {p2:<10} {p3:<8.5} {p4:<10} {p5:<8.5} {p6:<10} {p6plus:<15}') 



houses = get_data()
percentages = cal_percentage(*houses)
percentages_list = percentages
display_result(*houses, *percentages_list)

