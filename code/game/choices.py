from curses import curs_set, KEY_UP, KEY_DOWN
from code.variables import Variables


class Choices:
    ENTER_KEY_CODE = 10

    def __init__(self):
        self.current_index = 0

    def display_options(self, options, text, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, f"{text}")
        for i, option in enumerate(options):
            prefix = "[*] " if i == self.current_index else "[ ] "
            stdscr.addstr(i + 1, 0, f"{prefix}{option}")
        stdscr.refresh()

    def decrement_index(self, options):
        self.current_index = (self.current_index - 1) % len(options)

    def increment_index(self, options):
        self.current_index = (self.current_index + 1) % len(options)

    def run(self, stdscr, options, text, variable_key=None, memory_value=False):
        if not options:
            raise ValueError("Options cannot be an empty list.")

        curs_set(0)  # Hide the cursor

        while True:
            self.display_options(
                options=options,
                text=f"{text}",
                stdscr=stdscr
            )

            key = stdscr.getch()

            if key == KEY_UP:
                self.decrement_index(options)
            elif key == KEY_DOWN:
                self.increment_index(options)
            elif key == self.ENTER_KEY_CODE:
                selected_option = options[self.current_index]
                if memory_value:
                    return selected_option
                elif variable_key is not None:
                    Variables('variables.json').save(
                        key=variable_key,
                        value=selected_option
                    )
                else:
                    raise ValueError("Variable key must be provided.")
                break
