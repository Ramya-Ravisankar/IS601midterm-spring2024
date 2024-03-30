'''app/plugins/history/__init__.py'''
from app.commands import Command
from calculator.calc_history import CalculationHistory
import logging

class HistoryCommand(Command):
    '''class to manage the history of calculations'''

    def execute(self,*args):
        '''Execute the HistoryCommand'''

    while True:
        print ("\n --- History --- ")
        print("Choose an option:")
        print("1. Displays the most recent calculation done ")
        print("2. Displays all calculations done so far")
        print("3. Clears the calculation history")
        print("4. Saves the history of calculations to the CSV")
        print("5. Loads the history of calculations from the CSV")
        print ("6. Deletes a calculation from history")
        print("\nType 'exit' - returns back to the main menu.")
        user_Option = input("\nEnter your choice: ")

            if user_Option.lower() == 'exit':
                break  # Exit the loop, ending the command

            self.process_choice(user_Option)

    def process_choice(self, user_Option):
        options = {
            '1': self._display_most_recent_calculation,
            '2': self._display_all_calculations,
            '3': self._clear_history,
            '4': self._save_calculation_history,
            '5': self._load_calculation_history,
            '6': self._delete_calculation_from_history,
        }
        action = options.get(user_Option)
        if action:
            action()
        else:
            print("Invalid choice. Select a valid option or type 'exit' to return to main menu.")

    def retrieve_all_calculations(self):
        '''Retrieve all calculations from the history and print their results'''
        all_calculations = CalculationHistory.get_history()
        print("All Calculations:")
        for calculation in all_calculations:
            self.print_result(calculation)

    def retrieve_latest_calculation(self):
        '''Retrieve the most recent calculation from the history and print its result'''
        latest_calculation = CalculationHistory.get_latest_history()
        self.print_result(latest_calculation)

    def clear_history(self):
        '''Clear the calculation history'''
        CalculationHistory.clear_history()
        print("Calculation history cleared.")

    def print_result(self, calculation):
        '''Print the result of a calculation, handling cases where the calculation is undefined'''
        try:
            result = calculation.compute()
            print(f"{calculation} results in {result}")
        except:
            print(f"{calculation} is undefined.")