# ---------------PRIOQ I----------------------------
# >>> from queues import PriorityQueue

# >>> CRITICAL = 3
# >>> IMPORTANT = 2
# >>> NEUTRAL = 1

# >>> messages = PriorityQueue()
# >>> messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# >>> messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# >>> messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# >>> messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# >>> messages.dequeue()
# (1, 'Radio station tuned in')

# ------------------PRIOQ II----------------------
# >>> from queues import PriorityQueue

# >>> CRITICAL = 3
# >>> IMPORTANT = 2
# >>> NEUTRAL = 1

# >>> messages = PriorityQueue()
# >>> messages.enqueue_with_priority(IMPORTANT, "Windshield wipers turned on")
# >>> messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
# >>> messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
# >>> messages.enqueue_with_priority(IMPORTANT, "Hazard lights turned on")

# >>> messages.dequeue()
# (1, 'Radio station tuned in')