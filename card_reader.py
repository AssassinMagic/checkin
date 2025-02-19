import re

class CardReader:
    def __init__(self, callback):
        self.callback = callback

    def parse(self, swipe):
        """Extracts student ID and name from swipe data."""
        # Extract student ID (between first and second caret '^')
        match = re.search(r'\^([^ ^]+)\^', swipe)
        student_id = match.group(1) if match else ""

        # Extract name (between last caret '^' and question mark '?'), removing commas
        match = re.search(r'\^([^?]+)\?', swipe.split('^')[-1])
        name = match.group(1).replace(',', '') if match else ""

        return student_id, name

    def start(self):
        """Read swipe data from the card reader."""
        while True:
            try:
                swipe = input("Waiting for card: ")  # User swipes the card
                student_id, name = self.parse(swipe)
                print(f"Name: {name}")
                print(f"Student ID: {student_id}")
                user_info = {
                    "name": name,
                    "student_id": student_id,  
                }
                self.callback(user_info)
            except KeyboardInterrupt:
                print("\nExiting card reader.")
                break  # Allows graceful exit with Ctrl+C