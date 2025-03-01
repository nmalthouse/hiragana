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

