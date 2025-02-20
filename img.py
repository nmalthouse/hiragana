from PIL import Image
import pytesseract
import corpus

allchars = ""
for item in corpus.fullcorpus:
    allchars += item[1]

#allchars = 'あえいおうかけきこく'
pngn = "test.png"
custom_psm = r'--psm 10 -l jpn -c tessedit_char_whitelist=' + allchars
img = Image.open(pngn)
st = pytesseract.image_to_string(img, config=custom_psm )
print(st)
