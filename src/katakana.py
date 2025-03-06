A = [
["a","ア"],
["i","イ"],
["u","ウ"],
["e","エ"],
["o","オ"]]

K = [
["ka","カ"],
["ki","キ"],
["ku","ク"],
["ke","ケ"],
["ko","コ"]]

S = [
["sa","サ"],
["shi","シ"],
["su","ス"],
["se","セ"],
["so","ソ"]]

T = [
["ta","タ"],
["chi","チ"],
["tsu","ツ"],
["te","テ"],
["to","ト"]]

N = [
["na","ナ"],
["ni","ニ"],
["nu","ヌ"],
["ne","ネ"],
["no","ノ"]]

H = [
["ha","ハ"],
["hi","ヒ"],
["fu","フ"],
["he","ヘ"],
["ho","ホ"]]
M = []

mapping = {
        'A':A, 'K':K, 'S':S, 'T':T, 'N':N, 'H':H,
        }
        #'M':M, 'R':R, 'Y':Y, 'W':W, 'Z':Z, 'D':D,
        #'B':B, 'P':P}
def getAggregateList(symb):
    agg = []
    for char in symb:
        agg += mapping[char]
    return agg
