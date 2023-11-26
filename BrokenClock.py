class Clock:
    def __init__(self, day_time, broken_right):
        self.day_time = day_time  # Total seconds in a day
        self.broken_right = broken_right  # Number of times the broken clock is right

    def calculate_broken_wrong(self):
        # Subtracting the number of times the clock is right from the total day time
        return self.day_time - self.broken_right


class BrokenClock:
    @staticmethod
    def main():
        # Total seconds in a day
        total_day_time = 86400

        # Number of times the broken clock is right
        broken_right = 2

        # Creating a Clock object with initial values
        broken_clock = Clock(total_day_time, broken_right)

        # Calling the calculate_broken_wrong method to get the number of times the clock is wrong
        broken_wrong = broken_clock.calculate_broken_wrong()

        # Printing the statement with the calculated value
        print(f"A broken clock is wrong {broken_wrong} times a day.")


# Running the main method
BrokenClock.main()
