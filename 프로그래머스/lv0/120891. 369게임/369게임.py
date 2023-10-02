def solution(order):
    order_list = list(map(int, str(order)))
    
    return order_list.count(3) + order_list.count(6) + order_list.count(9)