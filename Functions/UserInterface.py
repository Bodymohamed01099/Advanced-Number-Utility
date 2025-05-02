import os
import time
from typing import Dict, Tuple, Any, Optional

class UserInterface:
    COLORS = {
        "reset": "\033[0m",
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "magenta": "\033[95m",
        "cyan": "\033[96m",
        "white": "\033[97m",
        "bold": "\033[1m"
    }
    
    @staticmethod
    def clear_screen() -> None:
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def color_text(text: str, color: str) -> str:
        if os.name == 'nt':
            return text
        return f"{UserInterface.COLORS.get(color, '')}{text}{UserInterface.COLORS['reset']}"
    
    @staticmethod
    def display_header(title: str) -> None:
        width = 50
        UserInterface.clear_screen()
        print(UserInterface.color_text("╔" + "═" * (width - 2) + "╗", "cyan"))
        print(UserInterface.color_text("║" + title.center(width - 2) + "║", "cyan"))
        print(UserInterface.color_text("╚" + "═" * (width - 2) + "╝", "cyan"))
        print()
    
    @staticmethod
    def display_menu(options: Dict[int, Tuple[str, Any]]) -> None:
        print(UserInterface.color_text("\n━━━ Menu Options ━━━", "yellow"))
        for key, (description, _) in options.items():
            print(f"{UserInterface.color_text(f'[{key}]', 'green')} {description}")
        print(UserInterface.color_text("━━━━━━━━━━━━━━━━━━", "yellow"))
    
    @staticmethod
    def get_integer_input(prompt: str, min_val: Optional[int] = None, 
                         max_val: Optional[int] = None) -> int:
        while True:
            try:
                user_input = input(f"{UserInterface.color_text('➤', 'blue')} {prompt}: ")
                value = int(user_input)
                
                if min_val is not None and value < min_val:
                    print(UserInterface.color_text(f"✘ Value must be at least {min_val}", "red"))
                    continue
                    
                if max_val is not None and value > max_val:
                    print(UserInterface.color_text(f"✘ Value must be at most {max_val}", "red"))
                    continue
                    
                return value
            except ValueError:
                print(UserInterface.color_text("✘ Invalid input. Please enter a valid number", "red"))
    
    @staticmethod
    def display_result(title: str, result: Any) -> None:
        print(f"\n{UserInterface.color_text('▶ ' + title, 'magenta')}")
        
        if isinstance(result, list):
            if len(result) > 10:
                items_str = (f"[{', '.join(map(str, result[:5]))}, ... " +
                            f"{', '.join(map(str, result[-5:]))}]")
                print(f"  {len(result)} items: {items_str}")
            else:
                print(f"  {result}")
        else:
            print(f"  {result}")
    
    @staticmethod
    def display_processing_animation(operation: str, duration: float = 0.8) -> None:
        frames = ["⣾", "⣽", "⣻", "⢿", "⡿", "⣟", "⣯", "⣷"]
        start_time = time.time()
        i = 0
        
        print(f"{UserInterface.color_text('Processing', 'cyan')} {operation}", end="", flush=True)
        while time.time() - start_time < duration:
            print(f"\r{UserInterface.color_text('Processing', 'cyan')} {operation} {frames[i % len(frames)]}", end="", flush=True)
            i += 1
            time.sleep(0.1)
        print(f"\r{UserInterface.color_text('Completed', 'green')} {operation}!{' ' * 10}")