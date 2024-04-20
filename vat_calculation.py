def calculate_vat(price):
    """
    Calculates the price including 25% VAT.

    Args:
        price (float): Price excluding VAT.

    Returns:
        float: Price including VAT.
    """
    vat = 0.25 # 25%

    price_with_vat = price * (1 + vat)
    return price_with_vat

def main():
    # Input price 
    try:
        total_price = float(input("Enter price: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    
    # Calculate price including VAT
    price_with_vat = calculate_vat(total_price)

    # Output price including VAT
    print(f"Price including VAT: {price_with_vat:.2f}")

if __name__ == "__main__":
    main()