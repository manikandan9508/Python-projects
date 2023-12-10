class HotelBookingSystem:
    def __init__(self, available_rooms):
        self.available_rooms = available_rooms
        self.booked_rooms = {}

    def display_available_rooms(self):
        print(f"Available Rooms: {self.available_rooms - len(self.booked_rooms)}")
        print("Room Numbers:", [room for room in range(1, self.available_rooms + 1) if room not in self.booked_rooms])

    def book_room(self, guest_name, room_number, num_nights):
        if room_number not in self.booked_rooms and 1 <= room_number <= self.available_rooms:
            self.booked_rooms[room_number] = {"guest_name": guest_name, "num_nights": num_nights}
            print(f"Room booked successfully for {num_nights} nights by {guest_name}.")
        else:
            print("Invalid room number or room already booked. Please choose another room.")

    def display_booked_rooms(self):
        print("Booked Rooms:")
        for room_number, details in self.booked_rooms.items():
            print(f"Room {room_number}: {details['guest_name']}, {details['num_nights']} nights")

# Example usage
def hotel():
    total_rooms = 10
    hotel_system = HotelBookingSystem(total_rooms)

    while True:
        print("\nHotel Booking System")
        print("1. Display Available Rooms")
        print("2. Book a Room")
        print("3. Display Booked Rooms")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            hotel_system.display_available_rooms()
        elif choice == "2":
            guest_name = input("Enter guest name: ")
            room = int(input("Enter the room number you want to book: "))
            nights = int(input("Enter the number of nights: "))
            hotel_system.book_room(guest_name, room, nights)
        elif choice == "3":
            hotel_system.display_booked_rooms()
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

hotel()

