import re
import requests
import urllib.parse as urlparse

target_url = "https://www.yna.co.kr"
target_links = []

def extract_link_from(url):
	response = requests.get(target_url)
	return re.findall('(?:href=")(.*?)"', response.content.decode(errors="ignore"))

def crawl(url):
	href_links = extract_link_from(url)
	for link in href_links:
		link = urlparse.urljoin(url, link)

		if "#" in link:
			link = link.split("#")[0]

		if target_url in link and link not in target_links:
			target_links.append(link)
			print(link)
			crawl(link)

crawl(target_url)