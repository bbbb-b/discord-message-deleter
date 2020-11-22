#!/usr/bin/python3 -i
import discord
import json
import re
#import asyncio

class DeleterBot(discord.Client):
	blacklisted_words = []
	target_guild = ""
	async def on_ready(self):
		print("ready")
		#blacklisted_words = list(map(lambda x : f"({x})", blacklisted_words))
		# ^ not really needed
		await self.do_stuff()

	async def do_stuff(self):
		return
		deleted_count = 0
		view_count = 0
		#print (blacklisted_words)
		regex = re.compile(".*({}).*".format("|".join(blacklisted_words)))
		for guild in self.guilds:
			if guild.name == self.target_guild:
				print ("GUILD: {}".format(guild.name))
				for channel in guild.channels:
					if type(channel) != discord.TextChannel:
						continue
					print ("CHANNEL: {}".format(channel.name))
					async for message in channel.history(limit = None):
						view_count += 1
						match = lambda r, s : False if type(s) != str else (r.match(s.replace("\n", "")) != None)
						to_delete = False
						to_delete = to_delete or match(regex, message.content)
						for embed in message.embeds:
							to_delete = to_delete or match(regex, embed.title)
							to_delete = to_delete or match(regex, embed.description)
							to_delete = to_delete or match(regex, embed.url)
							if embed.fields != discord.Embed.Empty:
								for field in embed.fields:
									to_delete = to_delete or match(regex, field.name);
									to_delete = to_delete or match(regex, field.value);
						if to_delete:
							deleted_count += 1
							print ("Deleting message: {}".format(message.content))
							await message.delete()
						if view_count % 1000 == 0:
							print ("DELETED {}/{}".format(deleted_count, view_count))
		print ("DELETED {}/{}".format(deleted_count, view_count))
		print ("done")
	async def on_message(self, message):
		pass
		#print("msg from {0.author}: {0.content}".format(message))
		

def main():
	config = json.load(open("auth.json"))
	#print(config)
	bot = DeleterBot()
	#print ("\"{}\"".format(config["client_secret"]))
	bot.run(config["client_token"])




if __name__ == "__main__":
	main()
