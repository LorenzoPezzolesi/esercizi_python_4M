class Reservation:
    def __init__(self, customer_name, date_time, num_people, status="in attesa"):
        self.customer_name = customer_name
        self.date_time = date_time
        self.num_people = num_people
        self.status = status

    def __str__(self):
        return f"Reservation for {self.customer_name} on {self.date_time} for {self.num_people} people - Status: {self.status}"

    def cancel(self):
        self.status = "cancellata"


class ReservationSystem:
    def __init__(self):
        self.reservations = []

    def add_reservation(self, reservation):
        self.reservations.append(reservation)

    def search_by_customer_name(self, customer_name):
        return [res for res in self.reservations if customer_name.lower() in res.customer_name.lower()]

    def search_by_date(self, date):
        return [res for res in self.reservations if date in res.date_time]

    def display_all_reservations(self):
        for res in self.reservations:
            print(res)

    def cancel_reservation(self, customer_name, date_time):
        for res in self.reservations:
            if res.customer_name == customer_name and res.date_time == date_time:
                res.cancel()
                print("Reservation cancelled.")
                return
        print("Reservation not found.")


def main():
    system = ReservationSystem()

    while True:
        print("\nReservation System Menu:")
        print("1. Add Reservation")
        print("2. Search by Customer Name")
        print("3. Search by Date")
        print("4. Display All Reservations")
        print("5. Cancel Reservation")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            customer_name = input("Enter customer name: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            num_people = int(input("Enter number of people: "))
            reservation = Reservation(customer_name, date_time, num_people)
            system.add_reservation(reservation)
            print("Reservation added successfully.")

        elif choice == '2':
            customer_name = input("Enter customer name to search: ")
            results = system.search_by_customer_name(customer_name)
            if results:
                print("Search Results:")
                for res in results:
                    print(res)
            else:
                print("No reservations found.")

        elif choice == '3':
            date = input("Enter date to search (YYYY-MM-DD): ")
            results = system.search_by_date(date)
            if results:
                print("Search Results:")
                for res in results:
                    print(res)
            else:
                print("No reservations found.")

        elif choice == '4':
            print("All Reservations:")
            system.display_all_reservations()

        elif choice == '5':
            customer_name = input("Enter customer name: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM): ")
            system.cancel_reservation(customer_name, date_time)

        elif choice == '6':
            print("Exiting the program.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
