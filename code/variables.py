from code.files import File


class Variables(File):
    def save(self, key: str, value: any) -> None:
        """
        Lit un fichier JSON, ajoute ou modifie la valeur d'une clé (existante ou non)
        et la sauvegarde
        """
        self.file = 'variables.json'
        variables = self.read()
        variables[key] = value
        self.write(content=variables)

    def get(self, key: str) -> any:
        """
        Simplement renvoyer la valeur d'un clé d'un dictionnaire
        """
        return self.read()[key]
