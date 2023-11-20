from code import File


class Variables(File):
    def save(self, key: str, value: any) -> None:
        variables = self.read()
        variables[key] = value
        self.write(content=variables)

    def get(self, key: str) -> any:
        return self.read()[key]
