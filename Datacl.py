# >>> from dataclasses import dataclass

# >>> @dataclass
# ... class Message:
# ...     event: str
# ...

# >>> wipers = Message("Windshield wipers turned on")
# >>> hazard_lights = Message("Hazard lights turned on")

# >>> wipers < hazard_lights
# Traceback (most recent call last):
#   ...
# TypeError: '<' not supported between instances of 'Message' and 'Message'

# ------------------------- DATACL II------------------

# >>> messages = PriorityQueue()
# >>> messages.enqueue_with_priority(CRITICAL, wipers)
# >>> messages.enqueue_with_priority(IMPORTANT, hazard_lights)

# ------------------------- DATACL III------------------

# >>> messages.enqueue_with_priority(CRITICAL, Message("ABS engaged"))
# Traceback (most recent call last):
#   ...
# TypeError: '<' not supported between instances of 'Message' and 'Message'

