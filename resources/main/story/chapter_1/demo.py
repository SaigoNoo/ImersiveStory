from code import NPC
from code import StoryTools
from code import Player
from code import UsefullyMethods
from main import arg

# StoryTool Declaration
stools = StoryTools(
    cli_mode=arg.cli
)
player = Player()
functions = UsefullyMethods(
    cli_mode=arg.cli
)
# END -----------------
# NPC Declarations
john = NPC(
    npc='john'
)

# END ------------

# Script ---------
# - INTRO --------
functions.run(
    return_value=stools.text(
        text_content="Partie 1: Demo MVP"
    )
)
# - Part One -----
functions.run(
    return_value=john.text(
        text_content="Salut l'ami !"
    )
)

functions.run(
    return_value=f"Je possède {player.money} pièces d'or !"
)

functions.run(
    return_value=stools.text(
        text_content="Question... Combien d'argent as-tu ?"
    )
)

functions.run(
    return_value=stools.choices(
        variable_name='is_player_lier',
        answer="b",
        a="0$ mon ami !",
        b="250$ mon ami !",
        c="Ca ne se demande pas !",
    )
)
