import datetime

class Individual:
    def __init__(self, full_name, years, timestamp):
        self.full_name = full_name
        self.years = years
        self.timestamp = timestamp

    def __str__(self):
        return f"Name: {self.full_name}, Age: {self.years}, Date: {self.timestamp}"

def run_program():
    individuals = []
    print("Welcome to my project ")
    try:
        while True:
            try:
                # Prompt for user input
                full_name = input("Enter the full name: ").strip()
                if not full_name:
                    raise ValueError("Name cannot be empty.please put your name ")
                
                years = input("Enter your age: ").strip()
                if not years.isdigit():
                    raise ValueError("Age must be wriiten ")
                
                years = int(years)
                if years < 0:
                    raise ValueError("Age cannot be negative.")
                
                # Record the current date and time
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Create and add a new Individual object
                individual = Individual(full_name, years, timestamp)
                individuals.append(individual)
                print(f"your data  added successfully: {individual}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            finally:
                print("Attempt to add your data is completed.")
    except KeyboardInterrupt:
        print("\nInput process terminated by the user.")
    
    # Display collected data
    print("\nCollected your Data:")
    for individual in individuals:
        print(individual)

if __name__ == "__main__":
    run_program()
