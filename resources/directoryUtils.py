import xbmcgui
import cameraList

try:  # Python 3
    from urllib.parse import quote, urlencode
except ImportError:  # Python 2
    from urllib import urlencode
    from urllib2 import quote

from globals import g
def createRegionList():
    directoryItems = []
    for value in cameraList.regionDict:
        listItem = xbmcgui.ListItem(label=value["name"])
        listItem.setProperty('isFolder', str(value['isFolder']))
        #listItem.addContextMenuItems([('Theater Showtimes', buildUrl(cameraId=1))])

        directoryItems.append((buildUrl(params={ 'id' : value["id"]}), listItem, value["isFolder"]))

    return directoryItems

def createCameraList(regionId):
    directoryItems = []
    for element in cameraList.cameraDict:
        if(element['regionId'] == regionId):
            listItem = xbmcgui.ListItem(label=element['name'])
            video_info = {
                'codec': 'h264',
                'aspect': 1.78,
                'width': 1280,
                'height': 720,
            }
            listItem.addStreamInfo('video', video_info)
            cameraUrl = 'https://www.quebec511.info/Carte/Fenetres/camera.ashx?id={id}&format=mp4'.format(
                id = str(element['id']))
            directoryItems.append((cameraUrl, listItem, False))

    return directoryItems

def buildUrl(params=None):
    path = '{netloc}/{path}/{qp}'.format(
        netloc=g.BASE_URL,
        path=_encode_path(0),
        qp=_encode_params(params))
    
    return path

def _encode_path(cameraId):
    return quote(
        '/' + str(cameraId))


def _encode_params(params):
    return ('?' + urlencode(params)) if params else ''