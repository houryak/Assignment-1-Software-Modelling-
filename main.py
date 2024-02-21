# code for part 3 of the requirements
# passenger class
class Passenger:
    def __init__(self, first_name, last_name, reservation_num, identity_proof, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.reservation_num = reservation_num
        self.identity_proof = identity_proof
        self.date_of_birth = date_of_birth

    # function allowing to change (setter)
    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_reservation_num(self, reservation_num):
        self.reservation_num = reservation_num

    def set_identity_proof(self, identity_proof):
        self.identity_proof = identity_proof

    def set_date_of_birth(self, date_of_birth):
        self.date_of_birth = date_of_birth

    # function allowing to read (getter)
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_reservation_num(self):
        return self.reservation_num

    def get_identity_proof(self):
        return self.identity_proof

    def get_date_of_birth(self):
        return self.date_of_birth

    # return a string presentation of an object
    def __str__(self):
        return f"First name: {self.first_name} \nLast name: {self.last_name} \nDate of birth: {self.date_of_birth}\nIdentity proof: {self.identity_proof}\nReservation number: {self.reservation_num}"


passenger1 = Passenger("Hala", "Khalid", 4224, "PO152234", "1999-02-18")
print(passenger1)


# Boarding pass class
class Boarding:
    def __init__(self, flight_num, seat_num, gate_num, boarding_time, flag):
        self.flight_num = flight_num
        self.seat_num = seat_num
        self.gate_num = gate_num
        self.boarding_time = boarding_time
        self.flag = flag

    # function allowing to change (setter)
    def set_flight_num(self, flight_num):
        self.flight_num = flight_num

    def set_seat_num(self, seat_num):
        self.seat_num = seat_num

    def set_gate_num(self, gate_num):
        self.gate_num = gate_num

    def set_boarding_time(self, boarding_time):
        self.boarding_time = boarding_time

    def set_flag(self, flag):
        self.flag = flag

    # function allowing to read (getter)
    def get_flight_num(self):
        return self.flight_num

    def get_seat_num(self):
        return self.seat_num

    def get_gate_num(self):
        return self.gate_num

    def get_boarding_time(self):
        return self.boarding_time

    def get_flag(self):
        return self.flag

    # return a string presentation of an object
    def __str__(self):
        return f"Flight number: {self.flight_num}\nSeat number: {self.seat_num}\nGate number: {self.gate_num}\nBoarding time: {self.boarding_time}\nFlag: {self.flag}"


boardingPass = Boarding(1122, "10S", 11, "11:00", "Issued by staff")
print(boardingPass)


# Check-in agent class
class CheckIn:
    def __init__(self, first_name, last_name, employeeID, shift, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.employeeID = employeeID
        self.shift = shift
        self.gender = gender

    # function allowing to change (setter)
    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_employeeID(self, employeeID):
        self.employeeID = employeeID

    def set_shift(self, shift):
        self.shift = shift

    def set_gender(self, gender):
        self.gender = gender

    # function allowing to read (getter)
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_employeeID(self):
        return self.employeeID

    def get_shift(self):
        return self.shift

    def get_gender(self):
        return self.gender

    # return a string presentation of an object
    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}\nGender: {self.gender}\nEmployee ID: {self.employeeID}\nShift: {self.shift}"


agent = CheckIn("Rashid", "Ali", 5589, "Day shift 08:00-02:00", "Male")
print(agent)


# Boarding pass system class
class Boarding_system:
    def __init__(self, boardingID, passenger_name, flight_num, seat_num, gate_num):
        self.boardingID = boardingID
        self.passenger_name = passenger_name
        self.flight_num = flight_num
        self.seat_num = seat_num
        self.gate_num = gate_num

    # function allowing to make change(setter)
    def set_boardingID(self, boardingID):
        self.boardingID = boardingID

    def set_passenger_name(self, passenger_name):
        self.passenger_name = passenger_name

    def set_flight_num(self, flight_num):
        self.flight_num = flight_num

    def set_seat_num(self, seat_num):
        self.seat_num = seat_num

    def set_gate_num(self, gate_num):
        self.gate_num = gate_num

    # function allowing to read(getter)
    def get_boardingID(self):
        return self.boardingID

    def get_passenger_name(self):
        return self.passenger_name

    def get_flight_num(self):
        return self.flight_num

    def get_seat_num(self):
        return self.seat_num

    def get_gate_num(self):
        return self.gate_num

    # return a string presentation of an object
    def __str__(self):
        return f"Boarding ID: {self.boardingID}\nPassenger name: {self.passenger_name}\nFlight number: {self.flight_num}\nSeat number: {self.seat_num}\nGate number: {self.gate_num}"


BoardingSystem = Boarding_system(4224, "Hala Khalid", 1122, "10S", 11)
print(BoardingSystem)


# code for part 4 of the requirements
# creat class for the airline boardiing pass that's shown in the figure
class Airline:
    def __init__(self, name, current_place, flight_tag, date, time, gate, boarding, seat_num, electronic_ticket,
                 destination, arrival_time, terminal_num, reference_num):  # the object that are on the figure
        self.name = name
        self.current_place = current_place
        self.flight_tag = flight_tag
        self.date = date
        self.time = time
        self.gate = gate
        self.boarding = boarding
        self.seat_num = seat_num
        self.electronic_ticket = electronic_ticket
        self.destination = destination
        self.arrival_time = arrival_time
        self.terminal_num = terminal_num
        self.reference_num = reference_num

    # funtion allowing to make change (setter)  and  function allowing to read (getter)
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_current_place(self, current_place):
        self.current_place = current_place

    def get_current_place(self, current_place):
        return self.current_place

    def set_flight_tag(self, flight_tag):
        self.flight_tag = flight_tag

    def get_flight_tag(self):
        return self.flight_tag

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_time(self, time):
        self.time = time

    def get_time(self):
        return self.time

    def set_gate(self, gate):
        self.gate = gate

    def get_gate(self):
        return self.gate

    def set_boarding(self, boarding):
        self.boarding = boarding

    def get_boarding(self):
        return self.boarding

    def set_seat_num(self, seat_num):
        self.seat_num = seat_num

    def get_seat_num(self):
        return self.seat_num

    def set_electronic_ticket(self, electronic_ticket):
        self.electronic_ticket = electronic_ticket

    def get_electronic_ticket(self):
        return self.electronic_ticket

    def set_destination(self, destination):
        self.destination = destination

    def get_destination(self):
        return self.destination

    def set_arrival_time(self, arrival_time):
        self.arrival_time = arrival_time

    def get_arrival_time(self):
        return self.arrival_time

    def set_terminal_num(self, terminal_num):
        self.terminal_num = terminal_num

    def get_terminal_num(self):
        return self.terminal_num

    def set_reference_num(self, reference_num):
        self.reference_num = reference_num

    def get_reference_num(self):
        return self.reference_num

    def __str__(self):
        return f"Passenger: {self.name}\nFrom: {self.current_place}\nFlight: {self.flight_tag}\nDate: {self.date}\nTime: {self.time}\nGate: {self.gate}\nBoarding till: {self.boarding}\nSeat: {self.seat_num}\nTo: {self.destination}\nArrival time: {self.arrival_time}\nThernimal: {self.terminal_num}\n{self.reference_num}"


boardingpass = Airline("JAMES SMITH", "CHICAGO ORD", "NA4321", "06 DEC 20", "11:40", 3, "11:20", "9A", 629,
                       "NEW YORK JFK", "13:30", 2, "5A6BCD78")

print("NATIONAL AIRLINES PASSENGER TICKET AND BAGGAGE CHECK")
print("BOARDING PASS FIRST CLASS")
print(boardingpass)
print("PLEASE BE AT THE GATE AT BOARDING TIME")