import re
import threading

class CardReader:
    def __init__(self, callback):
        self.callback = callback

    def parse(self, swipe):
        """Extracts student ID and name from swipe data."""
        # Extract student ID (between first and second caret '^')
        match = re.search(r'\^([^ ^]+)\^', swipe)
        studentID = match.group(1) if match else ""

        # Extract name (between last caret '^' and question mark '?'), removing commas
        match = re.search(r'\^([^?]+)\?', swipe.split('^')[-1])
        name = match.group(1).replace(',', '') if match else ""

        return studentID, name

    def start(self):
        """Start a background thread to read swipe data from the card reader."""
        t_thread = threading.Thread(target=self._read_card)
        t_thread.daemon = True
        t_thread.start()

    def _read_card(self):
        """Continuously reads swipe data from the card reader."""
        while True:
            try:
                swipe = input("Waiting for card: ")  # User swipes the card
                studentID, name = self.parse(swipe)
                print(f"Name: {name}")
                print(f"Student ID: {studentID}")
                user_info = {
                    "name": name,
                    "email": f"{studentID}@example.com",  # Example email, replace with actual logic
                    "skateSize": "9",  # Example skate size, replace with actual logic
                    "timeSlot": "12:00 PM - 1:00 PM"  # Example time slot, replace with actual logic
                }
                self.callback(user_info)
            except KeyboardInterrupt:
                print("\nExiting card reader.")
                break  # Allows graceful exit with Ctrl+C