VAR = 0
GALLERY = {
    "01.jpg": ("title1_it", "alt1_it", "title1_en", "alt1_en", "title1_de", "alt1_de"),
    "02.jpg": ("title2_it", "alt2_it", "title2_en", "alt2_en", "title2_de", "alt2_de"),
    "03.jpg": ("title3_it", "alt3_it", "title3_en", "alt3_en", "title3_de", "alt3_de")
}

for i in sorted(GALLERY): 
    DATA = (i, GALLERY[i])
    SRC = DATA[0]
    TITLE = DATA[1][2*VAR]
    ALT = DATA[1][2*VAR+1]
    print "<img src=\"/images/slider/" + SRC + "\" title=\"" + TITLE + "\" alt=\"" + ALT + "\">"
