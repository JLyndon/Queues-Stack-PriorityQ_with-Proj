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