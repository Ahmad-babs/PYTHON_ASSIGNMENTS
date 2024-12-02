# Question 1:
# Define the function
def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Question 2:
# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)

# Print the result
if discount_percentage >= 20:
    print(f"Your price with the discount is: {final_price:.2f}")
else:
    print(f"No discount applied. Your price is: {original_price:.2f}")
