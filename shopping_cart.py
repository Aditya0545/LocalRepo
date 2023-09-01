total_amount=float(input("enter the total purchase amount:"))
is_primium_member=str(input("are you a primium member? (yes/No): "))

regular_discount=0.05
primium_discount=0.10

additional_discount_threshold = 1000
additional_discount_percent=0.05

if is_primium_member == 'yes':
    discount=primium_discount*total_amount
else:
    discount=regular_discount*total_amount
if total_amount > 1000:
    t_discount = (total_amount*additional_discount_percent)
else:
    t_discount = 0
final_amount = total_amount-(discount+t_discount)
print("RECEIPT")
print("Total Amount: Rs.",total_amount)
print("Discount Amount is {}".format(discount))
print("Threshold Discount Amount:{}".format(t_discount))
print("final Price: Rs.",final_amount)
print("Thank You For Shopping")