from curses import curs_set, KEY_UP, KEY_DOWN
from code.variables import Variables

# Objects Init #
variables = Variables(file='variables.json')


# ------------ #

class Choices:
    def __init__(self):
        self.current_index = 0

    def display_options(self, options: list, texte: str, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, f"{texte}")
        for i, option in enumerate(options):
            prefix = "[*] " if i == self.current_index else "[ ] "
            stdscr.addstr(i + 1, 0, f"{prefix}{option}")

        stdscr.refresh()

    def decrement_index(self, options):
        self.current_index = (self.current_index - 1) % len(options)

    def increment_index(self, options):
        self.current_index = (self.current_index + 1) % len(options)

    def run(self, stdscr, options: list, texte: str, variable_key: str):
        curs_set(0)  # Hide the cursor

        while True:
            self.display_options(
                options=options,
                texte=f"{texte}",
                stdscr=stdscr
            )

            key = stdscr.getch()

            if key == KEY_UP:
                self.decrement_index(options)
            elif key == KEY_DOWN:
                self.increment_index(options)
            elif key == 10:  # 10 c'est le code ASCII de la touche ENTER
                selected_option = options[self.current_index]
                variables.save(
                    key=variable_key,
                    value=selected_option
                )
                break
