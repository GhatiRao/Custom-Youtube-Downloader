""" To create a Youtube Downloader """
from pytube import YouTube


def yt_download(download_url , desn_file):

    """ This function takes two inputs of Youtube URL , and the destination file where it needs to be downloaded """
    
    link = YouTube(download_url)                #Object instantiated
    ##help(link)
    ##print(link)
    vid_streams = link.streams.filter()
    ##help(link.streams.filter())
    ##print(vid_streams)
    d_video = vid_streams.get_highest_resolution()
    d_video.download(desn_file)



download_url = input("Enter the Youtube URL you want to download :  ")

desn_file = input("Where do you want to save this file :  ")

yt_download(download_url , desn_file)






    
