from src.config import conf
from src import command

@command.bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(command.bot))
    await command.tree.sync()


command.bot.run(conf['token'])