import time
from .NumberUtility import NumberUtility
from .UserInterface import UserInterface

class NumberApp:
    def __init__(self):
        self.utility = NumberUtility()
        self.ui = UserInterface()
    
    def run_sum_even_numbers(self) -> None:
        self.ui.display_header("Sum of Even Numbers")
        n = self.ui.get_integer_input("Enter a number to sum even numbers up to", min_val=1)
        
        self.ui.display_processing_animation("calculations")
        
        while_result = self.utility.sum_even_numbers(n, use_while=True)
        for_result = self.utility.sum_even_numbers(n)
        
        self.ui.display_result("Using while loop", while_result)
        self.ui.display_result("Using for loop", for_result)
        
        input(UserInterface.color_text("\nPress Enter to continue...", "yellow"))
    
    def run_random_generator(self) -> None:
        self.ui.display_header("Random Number Generator")
        n = self.ui.get_integer_input("How many random numbers do you want to generate", min_val=1)
        
        self.ui.display_processing_animation("generation")
        
        try:
            result = self.utility.generate_random_numbers(n)
            self.ui.display_result("Generated random numbers", result)
        except Exception as e:
            print(UserInterface.color_text(f"✘ Error: {e}", "red"))
        
        input(UserInterface.color_text("\nPress Enter to continue...", "yellow"))
    
    def run_unique_random_generator(self) -> None:
        self.ui.display_header("Unique Random Number Generator")
        n = self.ui.get_integer_input("How many UNIQUE random numbers to generate", min_val=1)
        
        min_val = self.ui.get_integer_input("Minimum value for range", min_val=1)
        max_val = self.ui.get_integer_input("Maximum value for range", min_val=min_val)
        
        self.ui.display_processing_animation("generation")
        
        try:
            result = self.utility.generate_unique_random_numbers(n, min_val, max_val)
            self.ui.display_result("Generated unique random numbers", result)
        except ValueError as e:
            print(UserInterface.color_text(f"✘ Error: {e}", "red"))
        
        input(UserInterface.color_text("\nPress Enter to continue...", "yellow"))
    
    def run_select_random_numbers(self) -> None:
        self.ui.display_header("Select Random Numbers")
        n = self.ui.get_integer_input("How many unique numbers to generate", min_val=1)
        x = self.ui.get_integer_input(f"How many numbers to select from those {n}", min_val=1, max_val=n)
        
        min_val = self.ui.get_integer_input("Minimum value for range", min_val=1)
        max_val = self.ui.get_integer_input("Maximum value for range", min_val=min_val)
        
        self.ui.display_processing_animation("selection")
        
        try:
            result = self.utility.select_random_numbers(n, x, min_val, max_val)
            self.ui.display_result("Selected random numbers", result)
        except ValueError as e:
            print(UserInterface.color_text(f"✘ Error: {e}", "red"))
        
        input(UserInterface.color_text("\nPress Enter to continue...", "yellow"))
    
    def run(self) -> None:
        """Run the main application loop."""
        options = {
            1: ("Sum of Even Numbers", self.run_sum_even_numbers),
            2: ("Random Number Generator", self.run_random_generator),
            3: ("Unique Random Number Generator", self.run_unique_random_generator),
            4: ("Select Random Numbers", self.run_select_random_numbers),
            5: ("Exit", None)
        }
        
        while True:
            self.ui.display_header("Advanced Number Utility")
            self.ui.display_menu(options)
            
            choice = self.ui.get_integer_input("Choose an option", min_val=1, max_val=len(options))
            
            if choice == 5:
                self.ui.display_header("Goodbye!")
                print(UserInterface.color_text("Thank you for using Advanced Number Utility!", "green"))
                time.sleep(1.5)
                break
            
            options[choice][1]()
