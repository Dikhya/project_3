print("Choose Any one:👇🏻")
print("Enter:'1' for downloding your Instagram Profile📱")
print("Enter:'2'for downloding your Instagram Latest Post🚻")
print("Enter:'3' for downloding YouTube Video🎥")
print("Enter:'4' for downloding YouTube Audio🔊")
user=int(input("Enter Your Choice:"))
if(user==1):
    import instaloader
    igl= instaloader.Instaloader()
    inp=input("Enter User_name:")
    igl.download_profile(inp)
    print("DONE...")
    print("Successfully Downloaded !")
elif(user==2):
    import instaloader
    igl= instaloader.Instaloader()
    inp=input("Enter Your User_name:")

    profile=instaloader.Profile.from_username(igl.context,inp)

    allPosts=profile.get_posts()

    for post in allPosts:
        igl.download_post(post,inp)
        break
    print("DONE...")
    print("Successfully Downloaded !")
elif(user==3):
    from pytube import YouTube

    inp=input("Enter Video link:")
    yt=YouTube(inp)

    video=yt.streams.get_highest_resolution()
    video.download()
    print("DONE...")
    print("Successfully Downloaded !")
elif(user==4):
    from pytube import YouTube
    inp=input("Enter Audio link:")
    yt=YouTube(inp)
    video=yt.streams.get_audio_only()
    video.download()
    print("Done...")
    print("Successfully Downloaded !")
else:
    print("Try Again...!")
