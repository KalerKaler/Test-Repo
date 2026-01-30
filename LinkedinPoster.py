import pathlib, glob, regex as re
from mutagen import File

def get_duration(lis:list)->dict:
    info_dict={}
    for item in lis:
        audio=File(item)
        info_dict[item]=audio.info.length
    return info_dict

music_paths = list(pathlib.Path('.').rglob("*.mp3"))
print(music_paths)
english_list=[]
jp=[]

for item in music_paths:
    english=r"^[\u0000-\u007F]+$"
    english_jp = r'^[\u0000-\u007F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]+$'

    if re.match(english,item):
        english_list.append(item)
    
    elif re.match(english_jp,item):
        jp.append(item)

print(english_list,"\n",jp)

english_duration_dict=get_duration(english_list)
with open("English.m3u","w") as eng:
    eng.write("#EXTM3U\n")
    for item in english_duration_dict:
        eng.write(f"#EXTINF:{english_duration_dict[item]}, {item}\n")
        eng.write(f"{item}\n")

japanese_duration_dict=get_duration(english_jp)
with open("Japanese.m3u","w") as jp:
    jp.write("#EXTM3U\n")
    for item in japanese_duration_dict:
        jp.write(f"#EXTINF:{japanese_duration_dict[item]}, {item}\n")
        jp.write(f"{item}\n")
