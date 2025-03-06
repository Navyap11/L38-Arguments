def total_calculation(bill_amount, tip_percentage):
    total= bill_amount*(1+0.01*tip_percentage)
    total= round(total,2)
    print(f"Please pay ${total}")
total_calculation(125,40)