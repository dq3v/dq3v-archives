import os

with open("./video_list", "w", encoding="utf-8") as f:
    f.write("\n".join(os.listdir("./videos")))