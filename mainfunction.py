def transformeTempo(tempo):
    a = tempo.split(":")
    return (int(a[0])*60 + int(a[1]))

def verificaEntradaDeTempo(txt):
    val = txt.split(":")
    if len(val) != 2 or len(val[1]) != 2:
        return False
    if val[0].isnumeric() and val[1].isnumeric():
        return True
    else:
        return False