from tools import check_availability, get_hours, book_room, AVAILABILITY
from agent import dispatch


def test_check_availability():
    result = check_availability("Monday")
    assert "214" in result
    assert "216" in result
    assert "220" in result

def test_get_hours():
    result = get_hours("Friday")
    assert "8:00 AM" in result
    assert "5:00 PM" in result

def test_book_room():
    AVAILABILITY["Tuesday"] = ["214"]

    result = book_room("Tuesday", "214", "Krista")

    assert "booked" in result.lower()
    assert "214" not in AVAILABILITY["Tuesday"]


    def test_unknown_tool_is_rejected():
        before = AVAILABILITY.copy()

        result = dispatch("delete_all_bookings", {})

        assert "no tool named" in result.lower()
        assert AVAILABILITY == before


    def test_booking_requires_confirmation():
        AVAILABILITY["Wednesday"] = ["214", "216", "220"]

        result = dispatch(
            "book_room",
            {"day": "Wednesday", "room": "214", "name": "Krista"}
        )

        assert "confirmation required" in result.lower()
        assert "214" in AVAILABILITY["Wednesday"]

if __name__ == "__main__":
    test_check_availability()
    print("test_check_availability passed")

    test_get_hours()
    print("test_get_hours passed")

    test_book_room()
    print("test_book_room passed")

