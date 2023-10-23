def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        message = f"Hello, my name is {name}."
        badge_messages.append(message)
    return badge_messages

def assign_rooms(names):
    room_messages = []
    index = 0
    for name in names:
        if index < 8:
            message = f"Hello, {name}! You'll be assigned to room {index + 1}!"
            room_messages.append(message)
            index += 1
    return room_messages

def printer(names):
    badges = batch_badge_creator(names)
    for item in badges:
        print(item)
    room_assignments = assign_rooms(names)
    for item in room_assignments:
        print(item)
