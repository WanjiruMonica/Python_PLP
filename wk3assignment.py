# 

def calculate_discount(price, discount_percent):
    if discount_percent >20:
        dicounted_price = price - (price * discount_percent / 100)
        print(f"Discount applied! New price: {dicounted_price}")
        
    else:
        print(f"Discount is below 20%, no discount applied. Price remains {price}")



calculate_discount(int(input("Enter the price: ")), int(input("Enter the discount percentage: ")))

    
