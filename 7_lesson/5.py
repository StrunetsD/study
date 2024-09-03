from functools import reduce


def square(room):
    try:
        return room['length'] * room['width']
    except (TypeError, KeyError):
        return 0


rooms = [
    {
        "name": "Kitchen",
        "length": 10,
        "width": 4
    },
    {
        "name": "Room 1",
        "length": 5.5,
        "width": 4.5
    },
    {
        "name": "Room 2",
        "length": 5,
        "width": 4
    },
    {
        "name": "Room 3",
        "length": 7,
        "width": 6.3
    }
]

result = reduce(lambda current, room: current + square(room), map(square, rooms))
print(result)
