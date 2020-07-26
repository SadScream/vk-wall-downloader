import os
import time
import requests

from . import parser


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
		self.parser = parser.Parser()


	def download(self, vk, domain:str, count:int=0, offset:int=0, default_path:str=None, type_of_downloading:int=0):
		try:
			time.sleep(0.1)

			if default_path == None:
				default_path = self.default_path

			path = os.path.join(default_path, "Folders")

			if "Folders" not in os.listdir(default_path):
				os.mkdir(path)

			dirl = os.listdir(path)

			domain_path = os.path.join(path, domain)
			picture_path = os.path.join(domain_path, "pictures")
			video_path = os.path.join(domain_path, "video")

			if domain not in dirl:
				os.mkdir(domain_path)
			
			dirl = os.listdir(domain_path)

			if "pictures" not in dirl:
				os.mkdir(picture_path)
			if "video" not in dirl:
				os.mkdir(video_path)

			list_of_pictures = os.listdir(picture_path)
			list_of_videos = os.listdir(video_path)

			wall = (h for h in vk.method('wall.get', {
				"domain": domain,
				"count": count,
				"extended": 0,
				"filter": "all",
				"offset": offset })["items"])

			print(f"[{self.download.__name__}] `{domain}` download started")

			skiped = 0

			for item in wall:
				if skiped > 25:
					break

				if "attachments" in item:
					if "is_pinned" in item or "copy_history" in item:
						continue

					if len(item["text"]):
						if any(text in item["text"].lower() for text in BAD_TEXT):
							continue

					attachment = item["attachments"]

					for i in range(len(attachment)):
						if "photo" in attachment[i] and type_of_downloading in [0, 2]:
							photos = attachment[i]["photo"]

							if f"{photos['id']}.jpg" in list_of_pictures:
								skiped += 1
								break

							try:
								r = self.session.get(photos["sizes"][-1]["url"])

								file = os.path.join(picture_path, f"{photos['id']}.jpg")

								with open(file, "xb") as out:
									out.write(r.content)
							except:
								continue

						elif "video" in attachment[i] and type_of_downloading in [1, 2]:
							videos = attachment[i]["video"]

							if f"{videos['id']}.mp4" in list_of_videos:
								skiped += 1
								break
							
							owner = videos["owner_id"]
							video_id = videos["id"]
							access_key = videos["access_key"]

							video_url:str = vk.method("video.get", {
								"owner_id": owner, 
								"videos":f"{owner}_{video_id}_{access_key}", 
								"count":1, 
								"offset": 0})["items"][0]["player"]

							urls:dict = self.parser.parse(video_url)

							_, url = urls.best_q()

							try:
								r = self.session.get(url, stream=True)

								file = os.path.join(video_path, f"{video_id}.mp4")

								with open(file, "xb") as out:
									for chunk in r.iter_content(1024):
										out.write(chunk)
							except:
								continue


		except Exception as E:
			print(f"[{self.download.__name__}] Error while trying to download: {E}")

		print(f"[{self.download.__name__}] download of `{domain}` finished`")
		return self.parent.downloading_finished.emit()
