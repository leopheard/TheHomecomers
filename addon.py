from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feed.podbean.com/thehomecomers/feed.xml"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/84/67/2a/84672a96-aa90-4865-37bb-bd2f4ee8fc63/mza_154294456985786982.jpg/600x600bb.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://is3-ssl.mzstatic.com/image/thumb/Podcasts123/v4/84/67/2a/84672a96-aa90-4865-37bb-bd2f4ee8fc63/mza_154294456985786982.jpg/600x600bb.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
