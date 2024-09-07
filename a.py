def main():
    a = 5
    b = 0

    # Checking for division by zero, but no action is taken
    if b == 0:
        print("Error: cannot divide by zero!")
        # Missing return or exit here

    result = a / b  # This will still raise an exception, since we proceed with division

    # Printing result even though division by zero has occurred
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
