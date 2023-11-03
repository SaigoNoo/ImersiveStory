from code.game_functions import NPC

# NPCs declarations
john = NPC(npc='john')

# END of NPCs
john.text('Salut, comment ça va ?')
john.choices(
    a="Ca va...",
    b="Bof...",
    c="Mal, je me fais défoncer pour ce MVP..."
)
input("choix > ")