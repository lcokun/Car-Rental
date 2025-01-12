# Car Rental Program

class Car:
    def __init__(self, make, model, year, rental_price, vehicle_type, available=True):
        """
        Initialize a car object with attributes for make, model, year, rental price,
        vehicle type (e.g., SUV, sedan), and availability.
        """
        self.make = make
        self.model = model
        self.year = year
        self.rental_price = rental_price
        self.vehicle_type = vehicle_type
        self.available = available

    def display_info(self):
        """
        Display the details of the car, including make, model, year, rental price,
        vehicle type, and availability status.
        """
        status = "Available" if self.available else "Not Available"
        return f"{self.year} {self.make} {self.model} ({self.vehicle_type}) - ${self.rental_price}/day - {status}"


class RentalService:
    def __init__(self):
        """
        Initialize the rental service with a list of cars and a starting index for pagination.
        """
        self.cars = self.load_cars()
        self.start_index = 0

    def load_cars(self):
        """
        Load a predefined list of cars with attributes including type (e.g., SUV).
        """
        return [
            # SUVs
            Car("Toyota", "RAV4", 2021, 80, "SUV"),
            Car("Honda", "CR-V", 2020, 75, "SUV"),
            Car("Ford", "Escape", 2019, 70, "SUV", available=False),
            Car("Chevrolet", "Equinox", 2022, 85, "SUV"),
            Car("Hyundai", "Tucson", 2021, 78, "SUV"),
            Car("Nissan", "Rogue", 2020, 74, "SUV"),
            Car("Mazda", "CX-5", 2019, 72, "SUV"),
            Car("Kia", "Sportage", 2022, 79, "SUV"),
            Car("Subaru", "Forester", 2021, 77, "SUV", available=False),
            Car("Jeep", "Cherokee", 2020, 76, "SUV"),

            # Sedans
            Car("Toyota", "Camry", 2021, 70, "Sedan"),
            Car("Honda", "Accord", 2020, 65, "Sedan"),
            Car("Hyundai", "Elantra", 2022, 60, "Sedan"),
            Car("Mazda", "Mazda3", 2021, 68, "Sedan"),

            # Hatchbacks
            Car("Volkswagen", "Golf", 2020, 55, "Hatchback"),
            Car("Ford", "Focus", 2019, 50, "Hatchback"),
            Car("Toyota", "Yaris", 2021, 53, "Hatchback"),
            Car("Hyundai", "i20", 2022, 57, "Hatchback"),

            # Trucks
            Car("Ford", "F-150", 2021, 90, "Truck"),
            Car("Chevrolet", "Silverado", 2020, 95, "Truck"),
            Car("Toyota", "Tacoma", 2019, 88, "Truck"),

            # Continental Cars
            Car("Mercedes-Benz", "C-Class", 2021, 120, "Luxury"),
            Car("BMW", "3 Series", 2022, 130, "Luxury"),
            Car("Audi", "A4", 2020, 125, "Luxury"),
        ]

    def filter_cars_by_type(self, vehicle_type):
        """
        Filter the list of cars by their vehicle type (e.g., SUVs, sedans).
        """
        return [car for car in self.cars if car.vehicle_type.lower() == vehicle_type.lower()]

    def display_cars(self, cars):
        """
        Display a list of cars with their details.
        Each car is displayed with its index for easy selection.
        """
        for index, car in enumerate(cars):
            print(f"{index + 1}. {car.display_info()}")

    def sort_cars(self, criteria):
        """
        Sort the cars by a given criteria: either 'rental_price' or 'year'.
        """
        if criteria == "rental_price":
            # Sort by rental_price, then year (for cars with the same price)
            self.cars.sort(key=lambda car: (car.rental_price, -car.year))
        elif criteria == "year":
            # Sort by year (descending)
            self.cars.sort(key=lambda car: car.year, reverse=True)
        else:
            print("Invalid criteria for sorting.")

    def book_car(self, index):
        """
        Allow the user to book a car by marking it as unavailable.
        Display booking confirmation after successful booking.
        """
        if 0 <= index < len(self.cars) and self.cars[index].available:
            self.cars[index].available = False
            # unicode code prints out "Party Popper" emoji
            print(f"\n{chr(0x1F389)} Booking Confirmation {chr(0x1F389)}")
            print(f"You have successfully booked: {self.cars[index].display_info()}")
        else:
            print("Invalid choice or car not available.")

    def compare_cars(self, indices):
        """
        Compare multiple cars side-by-side by displaying their details together.
        """
        selected_cars = [self.cars[index] for index in indices if 0 <= index < len(self.cars)]
        for car in selected_cars:
            print(car.display_info())

    def run(self):
        """
        Main program loop to navigate the rental service. 
        Allows browsing, sorting, booking, and comparing cars.
        """
        while True:
            print("\nMenu (input number):")
            print("1. Browse cars by type")
            print("2. Sort cars")
            print("3. Book a car")
            print("4. Compare cars")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                # Browse cars by type (e.g., SUV, sedan)
                vehicle_type = input("Enter the type of vehicle (e.g., SUV, sedan, truck): ").lower()
                filtered_cars = self.filter_cars_by_type(vehicle_type)
                if not filtered_cars:
                    print("No cars available for the selected type.")
                    continue

                self.start_index = 0
                while True:
                    print("\nAvailable Cars:")
                    self.display_cars(filtered_cars[self.start_index:self.start_index + 5])
                    if self.start_index + 5 >= len(filtered_cars):
                        print("No more cars to display.")
                        break
                    more = input("\nWould you like to see more options? (yes/no): ").lower()
                    if more == "yes":
                        self.start_index += 5
                    else:
                        break

            elif choice == "2":
                # Sort cars by rental price or year
                criteria = input("Enter sorting criteria ('rental_price' or 'year'): ").lower()
                self.sort_cars(criteria)
                print("\nCars sorted successfully!")

            elif choice == "3":
                # Book a car
                self.display_cars(self.cars)

                # Validate input for car selection
                while True:
                    index_input = input("Enter the number of the car you want to book: ")
                    if index_input.isdigit():
                        index = int(index_input) - 1
                        if 0 <= index < len(self.cars):
                            self.book_car(index)
                            break
                        else:
                            print("Invalid car number. Please select a valid option.")
                    else:
                        print("Invalid input. Please enter a valid number.")

            elif choice == "4":
                # Compare cars side-by-side
                self.display_cars(self.cars)

                # Validate input for comparing cars
                while True:
                    indices_input = input("Enter the numbers of the cars to compare (comma-separated): ")
                    indices = indices_input.split(",")
                    if all(index.isdigit() and 0 <= int(index) - 1 < len(self.cars) for index in indices):
                        """
                        Adjust for 0-based indexing.
                        For when the user enters "1" for the first car, the program will refer to index 0.
                        Same logic as when user enters "2". The program will need to refer to index 1.
                        """
                        indices = [int(i) - 1 for i in indices]
                        self.compare_cars(indices)
                        break
                    else:
                        print("Invalid input. Please enter valid car numbers.")

            elif choice == "5":
                # Exit the program
                print("Thank you for using the car rental service!")
                break

            else:
                print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    service = RentalService()
    service.run()
