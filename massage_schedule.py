def massage_schedule(n, m, p, r, b):
    # 建立客人列表，每個客人有服務時間、預約時間、編號和營收
    customers = [(p[i], r[i], i, b[i]) for i in range(n)]
    # 按服務時間、預約時間、編號排序
    customers.sort()
    
    # 建立按摩師列表，每個按摩師有服務開始時間、服務時間和編號
    massage_therapists = [(0, 0, i) for i in range(1, m+1)]
    # 按服務開始時間和編號排序
    massage_therapists.sort()
    
    # 已服務的客人和營收
    serviced_customers = []
    total_revenue = 0
    
    # 依序排定每個客人
    for customer in customers:
        # 尋找能為該客人服務且等待時間最短的按摩師
        min_wait = float('inf')
        selected_therapist = None
        start_time = None
        for therapist in massage_therapists:
            # 該按摩師的服務結束時間
            end_time = therapist[0] + therapist[1]
            # 如果該按摩師還有足夠時間為客人服務
            if end_time <= 720 and end_time <= customer[1] + 30:
                # 計算客人等待時間
                wait_time = max(0, therapist[0] - customer[1])
                # 如果等待時間更短，則更新最小等待時間和選擇的按摩師
                if wait_time < min_wait:
                    min_wait = wait_time
                    selected_therapist = therapist
                    start_time = therapist[0] + wait_time
        # 如果找到了合適的按摩師
        if selected_therapist:
            # 加入已服務的客人和營收
            serviced_customers.append(customer[2])
            total_revenue += customer[3]
            # 更新該按摩師的服務開始時間
            massage_therapists.remove(selected_therapist)
            massage_therapists.append((start_time, customer[0], selected_therapist[2]))
            massage_therapists.sort()
    
    return len(serviced_customers), total_revenue

n = 5
m = 3
p = [70, 50, 50, 60, 60]
r = [0, 10, 0, 10, 30]
b = [300, 300, 300, 500, 500]
print(massage_schedule(n, m, p, r, b))

