import aiohttp
from html import unescape
import kw

class Wiki:

	def __init__(self, lang='ru', session = None):
		if session is None:
			self.session = aiohttp.ClientSession()
		else:
			self.session = session

		self.url = f'https://{lang.lower()}.wikipedia.org/w/api.php'


	async def get_html(self, page, clear=True, *args, **kwargs):
		query_des = kw.QueryDesigner()
		query = await query_des.get_html(page, *args, **kwargs)
		try:
			data = await self._fetch(query)
		except:
			print('======')
		return data


	async def opensearch(self, search, *args, **kwargs):
		query_des = kw.QueryDesigner()
		query = await query_des.opensearch(page, *args, **kwargs)
		try:
			data = await _fetch(self.session, query)
		except:
			print('======1')
		return data


	async def get_urls(self, gapfrom, *args, **kwargs):
		query_des = kw.QueryDesigner()
		query = await query_des.get_urls(gapfrom, *args, **kwargs)
		try:
			data = await _fetch(self.session, query)
		except:
			print('======2')
		return data

	async def get_media(self, titles, *args, **kwargs):
		query_des = kw.QueryDesigner()
		query = await query_des.get_media(titles, *args, **kwargs)
		try:
			data = await _fetch(self.session, query)
		except:
			print('======3')
		return data

	async def get_extracts(self, titles, *args, **kwargs):
		query_des = kw.QueryDesigner()
		try:
			query = await query_des.get_extracts(titles, *args, **kwargs)
			print('-=-=-=-', query)
		except:
			print('======4')
		
		data = await self._fetch(query)
		return data





	async def _fetch(self, send):

		response = await self.session.get(self.url, params=send)
		if response.content_type == 'text/html':
			data = await response.text()
		if response.content_type == 'application/json':
			data =  await response.json()
		data = unescape(data)	
		return data


	# async def _fetch1(self, send):
		
	# 	# response = await self.session.get(self.url, params=send)
	# 	async with aiohttp.ClientSession() as self.session:

		
	# 		async with self.session.get(self.url, params=send) as response:
	# 			print('+++', response)
	# 			if response.content_type == 'text/html':
	# 				data = await response.text()
	# 			if response.content_type == 'application/json':
				
	# 				data =  await response.json()
	# 		# print(unescape(data))
	# 	# await self.session.close()
			
	# 	return data





	async def close(self):
		"""Close the aiohttp Session"""
		await self.session.close()

	async def __aenter__(self):
		return self

	async def __aexit__(self, exception_type, exception_value, traceback):
		await self.close()










