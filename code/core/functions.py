from json import dumps, load


def read_ini(key: str):
    with open("config.ini", 'r') as ini:
        for line in ini.readlines():
            if line.split(' = ')[0] == key:
                return line.split(" = ")[1]


class UsefullyMethods:
    def __init__(self, cli_mode=False):
        self.cli = cli_mode

    def run(self, return_value):
        if self.cli:
            if type(return_value) is list:
                for [key, value] in return_value:
                    print(f"{key}) {value}")

            elif type(return_value) is str:
                print(return_value)

            elif type(return_value) is dict:
                self.table(
                    table=return_value
                )

        else:
            return return_value

    def input(self, text_content: str):
        if self.cli:
            return input(f"{text_content} >> ")
        else:
            pass

    def table(self, table: dict):
        if self.cli:
            for [key, value] in table.items():
                print(f"{key}) {value}")
        else:
            return table

    @staticmethod
    def set_switches(switch_label: str, switch_bool: bool):
        with open(f'saves/{read_ini("USERNAME")}/switches.json', 'r') as s:
            switches = load(s)
            switches[switch_label] = switch_bool
            s.close()
        with open(f'saves/{read_ini("USERNAME")}/switches.json', 'w') as s:
            s.write(dumps(switches))

        return True

    @staticmethod
    def set_variables(variable_label: str, variable_value):
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'r') as v:
            variables = load(v)
            variables[variable_label] = variable_value
            v.close()
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'w') as v:
            v.write(dumps(variables))

        return True

    @staticmethod
    def get_variable(variable_label: str):
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'r') as variables:
            return load(variables)[variable_label]

    @staticmethod
    def get_switch(switch_n: int):
        with open(f'saves/{read_ini("USERNAME")}/switches.txt', 'r') as switches:
            switch = switches.read()[1:-1].split(',')
            if switch_n > len(switch):
                raise ValueError(f"{switch_n} is out of range...")
            else:
                return switch[switch_n]
