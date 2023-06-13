import os
import re

from comic_completion.domain.model.id import Id

s = "[麻生羽呂] 今際の国のアリス [完1]"


a = re.findall(r"\[完(\d+)\]", s)
print(a)
# print(a.group())


path = "D:\\Z04_comic_2_tocomp\\[HERO×萩原ダイスケ] ホリミヤ [完16]"
print(os.path.basename(path))


path = "D:\\xx_tocomp\\[HERO×萩原ダイスケ] ホリミヤ [完16]\\ホリミヤ 第11巻"
print(sorted(os.listdir(path)))


REG_VOL = re.compile(r"第(\d+)巻$")
vol = "ホリミヤ エーデル"
vol_num = REG_VOL.findall(vol)
print(vol_num)


vol_num_str = "P_0002.jpg"

filename, ext = os.path.splitext(vol_num_str)
print(filename)
print(ext)

id = Id("AAAA")
print(id.value)
