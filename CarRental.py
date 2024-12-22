# Car Rental Program

# Car database: List of dictionaries with car details

cars = [
    {"id": 1, "type": "SUV", "brand": "Toyota", "model": "Highlander", "year": 2022, "price": 60, "available": True},
    {"id": 2, "type": "SUV", "brand": "Ford", "model": "Explorer", "year": 2021, "price": 55, "available": True},
    {"id": 3, "type": "SUV", "brand": "Honda", "model": "CR-V", "year": 2023, "price": 65, "available": True},
    {"id": 4, "type": "SUV", "brand": "Chevrolet", "model": "Tahoe", "year": 2020, "price": 75, "available": False},
    {"id": 5, "type": "SUV", "brand": "Nissan", "model": "Rogue", "year": 2022, "price": 50, "available": True},
    {"id": 6, "type": "SUV", "brand": "Jeep", "model": "Cherokee", "year": 2021, "price": 58, "available": True},
    {"id": 7, "type": "SUV", "brand": "Subaru", "model": "Outback", "year": 2022, "price": 62, "available": True},
    {"id": 8, "type": "SUV", "brand": "Mazda", "model": "CX-5", "year": 2023, "price": 64, "available": True},
    {"id": 9, "type": "Sedan", "brand": "Toyota", "model": "Camry", "year": 2022, "price": 45, "available": True},
    {"id": 10, "type": "Sedan", "brand": "Honda", "model": "Accord", "year": 2023, "price": 50, "available": True},
    {"id": 11, "type": "Sedan", "brand": "BMW", "model": "3 Series", "year": 2021, "price": 70, "available": True},
    {"id": 12, "type": "Sedan", "brand": "Mercedes", "model": "C-Class", "year": 2020, "price": 75, "available": False},
    {"id": 13, "type": "Hatchback", "brand": "Volkswagen", "model": "Golf", "year": 2022, "price": 40, "available": True},
    {"id": 14, "type": "Hatchback", "brand": "Ford", "model": "Focus", "year": 2021, "price": 38, "available": True},
    {"id": 15, "type": "Hatchback", "brand": "Hyundai", "model": "i30", "year": 2023, "price": 42, "available": True},
    {"id": 16, "type": "Hatchback", "brand": "Honda", "model": "Fit", "year": 2020, "price": 35, "available": True},
    {"id": 17, "type": "Sports", "brand": "Porsche", "model": "911", "year": 2023, "price": 150, "available": True},
    {"id": 18, "type": "Sports", "brand": "Ferrari", "model": "488", "year": 2022, "price": 200, "available": False},
    {"id": 19, "type": "Sports", "brand": "Lamborghini", "model": "Huracan", "year": 2023, "price": 250, "available": True},
    {"id": 20, "type": "Sports", "brand": "Chevrolet", "model": "Corvette", "year": 2021, "price": 140, "available": True}
]

# Execute main program

def main():
    print("Welcome to the Car Rental Program!")
    vehicle_type = input("Enter the vehicle type you're looking for (e.g., SUV, Sedan, Hatchback, Sports): ").strip()

if __name__ == "__main__":
    main()