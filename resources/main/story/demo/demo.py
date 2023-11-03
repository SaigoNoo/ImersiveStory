from code.game_functions import NPC
from code.core.actions import Actions

variable = Actions()


def command_check(var, prompt_text: str):
    while not var.valid_command(input(f'{prompt_text} >> ')):
        pass


command_check(
    var=variable,
    prompt_text='Que voulez-vous faire'
)

# NPCs declarations
john = NPC(npc='john')

# END of NPCs
if variable.command[1::] == 'start':
    john.text('Salut, comment ça va ?')
    john.choices(
        a="Ca va...",
        b="Bof...",
        c="Mal, je me fais défoncer pour ce MVP..."
    )
