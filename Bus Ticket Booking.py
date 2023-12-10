class BusTicketBookingSystem:
    def __init__(self, available_seats):
        self.available_seats = available_seats
        self.booked_seats = set()

    def display_available_seats(self):
        print(f"Available Seats: {self.available_seats - len(self.booked_seats)}")
        print("Seat Numbers:", [seat for seat in range(1, self.available_seats + 1) if seat not in self.booked_seats])

    def book_ticket(self, seat_number):
        if seat_number not in self.booked_seats and 1 <= seat_number <= self.available_seats:
            self.booked_seats.add(seat_number)
            print(f"Ticket booked successfully for seat {seat_number}.")
        else:
            print("Invalid seat number or seat already booked. Please choose another seat.")


if __name__ == "__main__":
    total_seats = 30
    bus_system = BusTicketBookingSystem(total_seats)

    while True:
        print("\nBus Ticket Booking System")
        print("1. Display Available Seats")
        print("2. Book a Ticket")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            bus_system.display_available_seats()
        elif choice == "2":
            seat = int(input("Enter the seat number you want to book: "))
            bus_system.book_ticket(seat)
        elif choice == "3":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")
