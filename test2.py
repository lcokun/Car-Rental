

def load_cars():
    return [
        {"make": "Toyota", "model": "RAV4", "year": 2021, "rental_price": 80, "available": True},
        {"make": "Honda", "model": "CR-V", "year": 2020, "rental_price": 75, "available": True},
        {"make": "Ford", "model": "Escape", "year": 2019, "rental_price": 70, "available": False},
        {"make": "Chevrolet", "model": "Equinox", "year": 2022, "rental_price": 85, "available": True},
        {"make": "Hyundai", "model": "Tucson", "year": 2021, "rental_price": 78, "available": True},
        {"make": "Nissan", "model": "Rogue", "year": 2020, "rental_price": 74, "available": True},
        {"make": "Mazda", "model": "CX-5", "year": 2019, "rental_price": 72, "available": True},
        {"make": "Kia", "model": "Sportage", "year": 2022, "rental_price": 79, "available": True},
        {"make": "Subaru", "model": "Forester", "year": 2021, "rental_price": 77, "available": False},
        {"make": "Jeep", "model": "Cherokee", "year": 2020, "rental_price": 76, "available": True},
    ]

def display_cars(cars, start_index=0, count=5):
   for i, car in enumerate(cars[start_index:start_index + count], start=1):
        print(f"{i}. {car['year']} {car['make']} {car['model']} - ${car['rental_price']}/day - {'Available' if car['available'] else 'Not Available'}")

def filter_available_cars(cars):
    return [car for car in cars if car['available']]

def sort_cars(cars, criterion):
    if criterion == "price":
        return sorted(cars, key=lambda car: car["rental_price"])
    elif criterion == "year":
        return sorted(cars, key=lambda car: car["year"], reverse=True)
    else:
        print("Invalid sorting criterion.")
        return cars

def book_car(cars, car_index):
    if 0 <= car_index < len(cars):
        car = cars[car_index]
        if car["available"]:
            car["available"] = False
            print(f"You have successfully booked the {car['year']} {car['make']} {car['model']}.")
        else:
            print("Sorry, this car is not available.")
    else:
        print("Invalid car selection.")

def compare_cars(cars, car_indices):
   for index in car_indices:
        if 0 <= index < len(cars):
            car = cars[index]
            print(f"{car['year']} {car['make']} {car['model']} - ${car['rental_price']}/day - {'Available' if car['available'] else 'Not Available'}")
        else:
            print(f"Car index {index} is invalid.")

def car_rental_program():
    cars = load_cars()
    while True:
        print("\nMenu:")
        print("1. Browse cars")
        print("2. Sort cars")
        print("3. Book a car")
        print("4. Compare cars")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            start_index = 0
            available_cars = filter_available_cars(cars)
            while True:
                print("\nAvailable Cars:")
                display_cars(available_cars, start_index)
                more = input("\nWould you like to see more options? (yes/no): ").lower()
                if more == "yes":
                    start_index += 5
                    if start_index >= len(available_cars):
                        print("No more cars to display.")
                        break
                else:
                    break

        elif choice == "2":
            criterion = input("Sort by 'price' or 'year': ").lower()
            cars = sort_cars(cars, criterion)
            print("Cars sorted successfully.")

        elif choice == "3":
            car_index = int(input("Enter the car number to book: ")) - 1
            book_car(cars, car_index)

        elif choice == "4":
            indices = list(map(int, input("Enter car numbers to compare (comma-separated): ").split(",")))
            indices = [i - 1 for i in indices]  # Adjust for zero-based indexing
            compare_cars(cars, indices)

        elif choice == "5":
            print("Thank you for using the Car Rental Availability Program!")
            break

        else:
            print("Invalid choice. Please try again.")

car_rental_program()
