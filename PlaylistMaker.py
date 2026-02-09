import pathlib, regex as re
from mutagen import File

def get_duration(lis:list)->dict:
    info_dict={}
    for item in lis:
        audio=File(str(item[0]))
        info_dict[item[1]]=(audio.info.length,item[0])
    return info_dict

print(f"{"PlaylistMaker by KalerKaler":*^40}")

music_paths = list(pathlib.Path('.').rglob("*.mp3"))
english_list=[]
jp=[]

for item in music_paths:
    
    english=r"^[\u0000-\u007F]+$"
    english_jp = r'^[\u0000-\u007F\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFF\uFF00-\uFFEF]+$'

    if re.match(english,item.stem):
        english_list.append([item.absolute(),item.stem])
    
    elif re.match(english_jp,item.stem):
        jp.append([item.absolute(),item.stem])

print(f"Found {len(english_list)} English songs.")
print(f"Found {len(jp)} Japanese songs.")

english_duration_dict=get_duration(english_list)
english_playlist_name=input("Enter the name for the English playlist file\n")
with open(english_playlist_name+".m3u","w") as eng:
    eng.write("#EXTM3U\n")
    for item in english_duration_dict:
        eng.write(f"#EXTINF:{english_duration_dict[item][0]}, {english_duration_dict[item][1]}\n")
        eng.write(f"{item}\n")

japanese_duration_dict=get_duration(jp)
japanese_playlist_name=input("Enter the name for the Japanese playlist file\n")
with open(japanese_playlist_name+".m3u","w",encoding="UTF-8") as jp:
    jp.write("#EXTM3U\n")
    for item in japanese_duration_dict:
        jp.write(f"#EXTINF:{japanese_duration_dict[item][0]}, {japanese_duration_dict[item][1]}\n")
        jp.write(f"{item}\n")
