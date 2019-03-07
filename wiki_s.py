import re

class FormatText:

	async def _cleanhtml(self, raw_html):

		# remove html tags
		cleantext = re.sub(r"<.*?>", "", raw_html)

		# remove the html comments
		cleantext = re.sub("(<!--.*?-->)", "", cleantext, flags=re.DOTALL)

		# remove lines with multiple spaces on them, happens after the regexe
		cleantext = "\n".join([r.strip() for r in cleantext.split("\n")])

		# remove multiple newlines which appeared after the regexes
		cleantext = re.sub(r"\n\n+", "\n\n", cleantext)

		# remove the edit things after the headings
		cleantext = cleantext.replace("[edit]", "")
		cleantext = cleantext.replace("(edit)", "")


		return cleantext


		async def text(self, html):

			return self._cleanhtml(html)



class Deser:

	@classmethod
	async def get_extracts(cls, json):
		
		data = json['query']["pages"]
		data = data[list(data.keys())[0]]["extract"]
		print('-=-', data)
		return data


	@classmethod
	async def get_html(cls, json):
		pass


