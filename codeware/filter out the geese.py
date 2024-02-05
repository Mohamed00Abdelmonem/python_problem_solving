

gesse = ['egypt', 'german', 'america', 'italya', 'palesten']

def gesse_filter(birds):
    return  [i for i in birds if i not in gesse]
print(gesse_filter(['egypt', 'mansoura', 'america', 'noyslanda', 'italya', 'gapan']))