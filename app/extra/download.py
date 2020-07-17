import os
import time
import requests


BAD_TEXT = [
	"реклама", "club", "подпишись", "подписывайся",
	"рекламка", "кликай", "vk.com", "подписка",
	"vk.me/", "вступай", "напиши в лс паблику",
	"подавай заявку", "продаем рекламку", "vk.cc/",
	"продаем рекламу", "давай скорее к нам",
	"давай к нам"
]


class Downloader:

	def __init__(self, parent):
		self.session = requests.Session()
		self.default_path = os.getcwd()
		self.parent = parent


	def download(self, vk, domain:str, count:int=0, offset:int=0, default_path:str=None):
		try:
			time.sleep(0.1)

			if default_path == None:
				default_path = self.default_path

			path = os.path.join(default_path, "Folders")

			if "Folders" not in os.listdir(default_path):
				os.mkdir(path)

			dirl = os.listdir(path)

			domain_path = os.path.join(path, domain)

			if domain not in dirl:
				os.mkdir(domain_path)
			
			dirl = os.listdir(domain_path)

			wall = (h for h in vk.method('wall.get', {
				"domain": domain,
				"count": count,
				"extended": 0,
				"filter": "all",
				"offset": offset })["items"])

			print(f"[{self.download.__name__}] `{domain}` download started")

			start_time = time.time()

			for item in wall:
				if (time.time() - start_time) > 40:
					break

				if "attachments" in item:
					if "is_pinned" in item or "copy_history" in item:
						continue

					if len(item["text"]):
						if any(text in item["text"].lower() for text in BAD_TEXT):
							continue

					attachment = item["attachments"]

					for i in range(len(attachment)):
						if "photo" in attachment[i]:
							photos = attachment[i]["photo"]

							if f"{photos['id']}.jpg" in dirl:
								break

							try:
								r = self.session.get(photos["sizes"][-1]["url"])

								file = os.path.join(domain_path, f"{photos['id']}.jpg")

								with open(file, "xb") as out:
									out.write(r.content)

								start_time = time.time()
							except:
								continue

		except Exception as E:
			print(f"[{self.download.__name__}] Error while trying to download: {E}")

		print(f"[{self.download.__name__}] download of `{domain}` finished`")
		return self.parent.downloading_finished.emit()