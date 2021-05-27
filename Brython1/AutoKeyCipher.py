def generateTR():
    tabulaRecta = {}

    alphabet = [
        chr(i) for i in range(ord('a'),ord('z')+1)]

    idx = 0
    for x in alphabet:
        i = idx
        for y in alphabet:
            key = x + y
            value = alphabet[i]

            #print(f'{key} - {value}')

            tabulaRecta.update( { key : value } )
            if (i == len(alphabet) - 1):
                i = 0
            else:
                i = i + 1
        idx = idx + 1
    return tabulaRecta

def cipher(text, tr, keyword):
    res = ''

    keyword = keyword + text
    keyword = keyword[0:len(text)]

    for i in range(0, len(keyword)):
        x = keyword[i]
        y = text[i]
        key = x + y
        res = res + tr.get(key)
    
    return res

def decipher(text, tr, keyword):
    res = ''

    for i in range(0, len(text)):
        x = keyword[i]
        value = text[i]
        
        # Get all dictionary entries where...
        # key starts with keyword[i]
        # and value is text[i]
        y = [ 
            k[1:] for k, v in tr.items() if (
                k.startswith(x) and v == value
            ) 
        ][0]

        res = res + y
        keyword = keyword + y

    return res    

def test():
    text = 'texttocipher'
    tr = generateTR()
    key = 'alltech'
    c = cipher(text, tr, key)
    d = decipher(c, tr, key)

    print(f'text: {text}')
    print(f'cipher: {c}')
    print(f'decipher: {d}')