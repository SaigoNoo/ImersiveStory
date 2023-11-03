def read_ini(key: str):
    with open("config.ini", 'r') as ini:
        for line in ini.readlines():
            if line.split('=')[0] == key:
                return line.split("=")[1]
