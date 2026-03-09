A = [["a","あ"],
    ["i","い"],
    ["u","う"],
    ["e","え"],
    ["o","お"]]
K = [ ["ka","か"],
    ["ki","き"],
    ["ku","く"],
    ["ke","け"],
    ["ko","こ"]]
S = [
    ["sa","さ"],
    ["shi","し"],
    ["su","す"],
    ["se","せ"],
    ["so","そ"]]
T = [
    ["ta","た"],
    ["chi","ち"],
    ["tsu","つ"],
    ["te","て"],
    ["to","と"] ]

N = [
    ["na","な"],
    ["ni","に"],
    ["nu","ぬ"],
    ["ne","ね"],
    ["no","の"]]
H = [
    ["ha","は"],
    ["hi","ひ"],
    ["hu","ふ"],
    ["he","へ"],
    ["ho","ほ"]]
M = [
    ["ma","ま"],
    ["mi","み"],
    ["mu","む"],
    ["me","め"],
    ["mo","も"]]
R = [
    ["ra","ら"],
    ["ri","り"],
    ["ru","る"],
    ["re","れ"],
    ["ro","ろ"] ]
Y = [
    ["ya","や"],
    ["yu","ゆ"],
    ["yo","よ"] ]
W = [
    ["wa","わ"],
    ["wo","を"],
    ["n","ん"]]

G = [
    ["ga","が"],
    ["gi","ぎ"],
    ["gu","ぐ"],
    ["ge","げ"],
    ["go","ご"]]

Z = [
["za","ざ"],
["ji","じ"],
["zu","ず"],
["ze","ぜ"],
["zo","ぞ"]]

D = [
["da","だ"],
["di","ぢ"],
["du","づ"],
["de","で"],
["do","ど"]]

B = [
["ba","ば"],
["bi","び"],
["bu","ぶ"],
["be","べ"],
["bo","ぼ"]]

P = [
["pa","ぱ"],
["pi","ぴ"],
["pu","ぷ"],
["pe","ぺ"],
["po","ぽ"]]

seion = A + K + S + T + N + H + M + R + Y + W
dakuten = Z + D + B + P

mapping = {
        'A':A, 'K':K, 'S':S, 'T':T, 'N':N, 'H':H,
        'M':M, 'R':R, 'Y':Y, 'W':W, 'Z':Z, 'D':D,
        'B':B, 'P':P}

new_corp = seion + D + Z
all_hiragana = "AKSTNHMRYWZDBP"

## JIS keyboard layout
kbd_home_left = ['ち','と', 'し','は','き']
kbd_home_right = ['く','ま','の','り','れ','け','む']
kbd_upper_left = ['た','て','い','す','か']
kbd_upper_right = [ 'な', 'に', 'ら', 'せ' ]
kbd_lower_left = [ 'つ', 'さ', 'そ', 'ひ', 'こ']
kbd_lower_right = [ 'み','も','ね','る','め','ろ']
kbd_num_left = ['ぬ','ふ','あ','う','え','お']
kbd_num_right = ['や', 'ゆ', 'よ', 'わ', 'ほ', 'へ']

default_kana = "QAZYHN17"
kbd_mapping = {
        'Q':kbd_upper_left,
        'A':kbd_home_left,
        'Z':kbd_lower_left,

        'y':kbd_upper_right,
        'H':kbd_home_right,
        'N':kbd_lower_right,

        '1':kbd_num_left,
        '7':kbd_num_right,
        }

def getAggregateStringJIS(symb):
    allchars = ""
    for char in symb:
        for item in kbd_mapping[char]:
            allchars += item
    return allchars

def getAggregateList(symb = all_hiragana):
    agg = []
    for char in symb:
        agg += mapping[char]
    return agg



def getAggregateString(symb = all_hiragana):
    allchars = ""
    for char in symb:
        for item in mapping[char]:
            allchars += item[1]
    return allchars

