import requests

# Tata Play channel ID for Sony SAB HD
url = "https://tvguide.tatasky.com/epg/now?channelId=107"
data = requests.get(url).json()

print('<tv>')
print('<channel id="Sony.SAB.HD.in"><display-name>Sony SAB HD</display-name></channel>')

for p in data['programs']:
    start = p['startTime']
    end = p['endTime']
    title = p['title']
    print(f'<programme start="{start}" stop="{end}" channel="Sony.SAB.HD.in">')
    print(f'<title>{title}</title>')
    print('</programme>')

print('</tv>')
