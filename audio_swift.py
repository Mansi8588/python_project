from moviepy.editor import *

# Separate performing task

# first create a audio file from both videos

      clip1=VideoFileClip(r"C:\Users\younl\OneDrive\Pictures\20230412_135342.mp4").subclip(0,10)
      clip1.audio.write_audiofile("first1.mp3")

      clip2=VideoFileClip(r"C:\Users\younl\OneDrive\Pictures\20230412_135732.mp4").subclip(10,20)
      clip2.audio.write_audiofile("first2.mp3")



# creating a video without audio

    clip1=VideoFileClip(r"C:\Users\younl\OneDrive\Pictures\20230412_135342.mp4").subclip(0,10)
    clip1=clip1.without_audio()
    clip1.write_videofile("first_wa1.mp4")


# final video after swapping audio

    video_one=VideoFileClip("first_wa1.mp4")
    audio_one=AudioFileClip("first2.mp3")
    final_video_one=video_one.set_audio(audio_one)
    final_video_one.write_videofile("swap_video.mp4")


# combine all task together

main_video=VideoFileClip(r"C:\Users\younl\OneDrive\Pictures\20230412_135732.mp4").subclip(10,20)
main_video=main_video.without_audio()

main_audio=AudioFileClip("first1.mp3")

final_video=main_video.set_audio(main_audio)
final_video.write_videofile("swap_video_2.mp4")
