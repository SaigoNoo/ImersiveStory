from code.variables import Variables
from code.files import File


class GameVariables:
    @staticmethod
    def saves_variables(list_var: list) -> None:
        """
        permet de stocker des valeurs dans le variables.json
        """
        for item in list_var:
            Variables(file='variables.json').save(
                key=item.split('=')[0].strip(),
                value=item.split("=")[1].strip()
            )

    @staticmethod
    def set_variables(line: str, color=False) -> str:
        """
        permet de remplacer une/plusieurs variables string |<var>| dans une ligne string.
        """
        var_color = File(file='config.ini').read()['COLOR_VAR']
        temp_line = line.split()
        for [index, word] in enumerate(temp_line):
            if '|' in word:
                replace = word.split('|')
                word = Variables(file='variables.json').get(key=replace[1])
                if color:
                    replace[1] = f"[bold {var_color}]{word}[/bold {var_color}]"
                else:
                    replace[1] = f"{word}"
                temp_line[index] = ''.join(replace)
        return ' '.join(temp_line)
