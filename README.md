# Discord message deleting bot

Deletes messages that includes the (hardcoded) blacklisted words
from the whole server (as long as it has the correct message deleting perms).

I once needed this and didn't find anything like it so made my own,
you're welcome to edit and use it if you find it.

Note that it puts the words into regex and doesn't escape them,
so if your words include some symbols that are used by regex, it might
mess something up or just throw an error.

Also note that it might take like 2 minutes for the bot to call `on_ready`
because of something that has to do with getting all the server information. You can
quicken it with some argument but then it won't be able to see all the
channels or servers. Google it if you wanna know more, point is, be patient.

