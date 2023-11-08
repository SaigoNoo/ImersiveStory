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

        else:
            return return_value

    def input(self, text_content: str):
        if self.cli:
            return input(f"{text_content} >> ")
        else:
            pass

    @staticmethod
    def set_switches(switch_n: int, set_value: bool):
        if switch_n < 0:
            raise ValueError(f"{switch_n} isn't a valable switch integer")
        else:
            with open(f'saves/{read_ini("USERNAME")}/switches.txt', 'r') as switches_read:
                pass
            with open(f'saves/{read_ini("USERNAME")}/switches.txt', 'w') as switches_write:
                switch = switches_write[1:-1].split(',')
                switch[switch_n] = set_value
                switches_write.write(switch)
        return switch_n < 0

    @staticmethod
    def set_variables(variable_name: str, variable_value):
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'r') as v:
            variables = load(v)
            variables[variable_name] = variable_value
            v.close()
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'w') as v:
            v.write(dumps(variables))

        return True

    @staticmethod
    def get_variable(variable_name: str):
        with open(f'saves/{read_ini("USERNAME")}/variables.json', 'r') as variables:
            return load(variables)[variable_name]

    @staticmethod
    def get_switch(switch_n: int):
        with open(f'saves/{read_ini("USERNAME")}/switches.txt', 'r') as switches:
            switch = switches.read()[1:-1].split(',')
            if switch_n > len(switch):
                raise ValueError(f"{switch_n} is out of range...")
            else:
                return switch[switch_n]
