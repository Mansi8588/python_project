from moviepy.editor import *

clip=VideoFileClip(r"C:\Users\younl\OneDrive\Pictures\20230412_135732.mp4").subclip(5,10)

text_clip=TextClip("Mansi Rai",fontsize=50,color="Black")
text_clip=text_clip.set_position("center").set_duration(5)

video=CompositeVideoClip([clip,text_clip])
video.write_videofile("water.mp4")
