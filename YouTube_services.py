import pytube
import os

CWD = os.getcwd()

def GetInfoAboutVideo(url):
    Video = pytube.YouTube(url=url)
    print("")
    print("---------------------------------------------")
    print("Information about video:")
    print("")
    print(f"Title: {Video.title}")
    print(f"Views: {Video.views}")
    print("")
    print(f"Published by: {Video.author}")
    print(f"Published at: {Video.publish_date}")
    print("")
    print(f"Description:\n{Video.description}")
    print("---------------------------------------------")
    print("")


def SearchForAVideo(query):
    VideoIDasTAG = pytube.Search(query=query).results[0]
    return "https://www.youtube.com/watch?v="+VideoIDasTAG.replace("<pytube.__main__.YouTube object: videoId=", "").replace(">", "")

def Download(url, quality):
    Video = pytube.YouTube(url)
    res = Video.streams.get_by_itag(quality)
    print(f"Download size: {(res.filesize/1024)/1024} MB")
    askcontinue = input("Do you want to continue? ")
    if askcontinue.lower() in ["yes", "y", "ye", "t", "true"]:
        continuedownloading = True
    elif askcontinue.lower() in ["no", "n", "f", "false"]:
        continuedownloading = False
    if(continuedownloading == True):
        print("")
        print(f"Video title: {Video.title}\nVideo filename: {res.default_filename}")
        print("")
        print("Downloading YouTube video 0%")
        res.download(f"./YouTube/{Video.title}/")
        print("Downloading YouTube video 100%")
        print("")
        print("Successfully downloaded video.")
        print(f"Your video is saved on {CWD}\\YouTube\\{Video.title}\\{res.default_filename}")
        print("")
