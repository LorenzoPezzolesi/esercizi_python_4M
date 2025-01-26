classDiagram
    class Reservation {
        -customer_name: str
        -date_time: str
        -num_people: int
        -status: str
        +__init__(customer_name: str, date_time: str, num_people: int, status: str)
        +__str__() str
        +cancel()
    }

    class ReservationSystem {
        -reservations: list
        +__init__()
        +add_reservation(reservation: Reservation)
        +search_by_customer_name(customer_name: str) list
        +search_by_date(date: str) list
        +display_all_reservations()
        +cancel_reservation(customer_name: str, date_time: str)
    }

    class Main {
        +main()
    }

    ReservationSystem --> Reservation
    Main --> ReservationSystem