"""
CSC-128 Assignment 7 starter: the tools and their schemas
Krista Balling
"""

AVAILABILITY = {
    "Monday": ["214", "216", "220"],
    "Tuesday": ["214"],
    "Wednesday": ["214", "216", "220"],
    "Thursday": [],
    "Friday": ["220"],
}


def check_availability(day):
    """Return which rooms are free on a given weekday."""
    day = day.strip().title()

    if day not in AVAILABILITY:
        return "Invalid day. Please enter Monday through Friday."

    rooms = AVAILABILITY[day]

    if not rooms:
        return f"No study rooms are available on {day}."

    return f"Available on {day}: " + ", ".join(rooms)


def get_hours(day):
    """Return the opening hours for a weekday."""
    day = day.strip().title()

    hours = {
        "Monday": "8:00 AM - 8:00 PM",
        "Tuesday": "8:00 AM - 8:00 PM",
        "Wednesday": "8:00 AM - 8:00 PM",
        "Thursday": "8:00 AM - 8:00 PM",
        "Friday": "8:00 AM - 5:00 PM",
    }

    if day not in hours:
        return "Invalid day. Please enter Monday through Friday."

    return f"Hours on {day}: {hours[day]}"


def book_room(day, room, name):
    """Reserve an available room and remove it from availability."""
    day = day.strip().title()
    room = str(room).strip()
    name = name.strip()

    if day not in AVAILABILITY:
        return "Invalid day. Please enter Monday through Friday."

    if room not in AVAILABILITY[day]:
        return f"Room {room} is not available on {day}."

    if not name:
        return "A name is required to book a room."

    AVAILABILITY[day].remove(room)

    return f"Room {room} booked for {name} on {day}."


AVAILABLE_TOOLS = {
    "check_availability": check_availability,
    "get_hours": get_hours,
    "book_room": book_room,
}

TOOL_SCHEMAS = [
    {
        "type": "function",
        "function": {
            "name": "check_availability",
            "description": (
                "Check which study rooms are available on a given weekday. "
                "Use this whenever a student asks which rooms are free."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Weekday name, for example Monday",
                    }
                },
                "required": ["day"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_hours",
            "description": (
                "Get the opening hours for a weekday. "
                "Use this whenever a student asks when the study rooms are open."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Weekday name, for example Friday",
                    }
                },
                "required": ["day"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "book_room",
            "description": (
                "Book an available study room for a student. "
                "Use this only when the student wants to reserve a specific room "
                "and has provided the day, room number, and name."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "day": {
                        "type": "string",
                        "description": "Weekday name for the booking",
                    },
                    "room": {
                        "type": "string",
                        "description": "Study room number, for example 214",
                    },
                    "name": {
                        "type": "string",
                        "description": "Name of the student making the booking",
                    },
                },
                "required": ["day", "room", "name"],
            },
        },
    },
]
