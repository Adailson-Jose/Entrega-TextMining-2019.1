def tokenizer(string):
    currentPosition = 0
    endOfString = len(string)-1
    flag = False
    delimiterSet = [',','.',';',':','!','?','(',')','<','>','+', "'",'\n','\t',' ','[',']']
    whiteSpace = ['\t','\n',' ']
    result = []
    while True:
        
        cursor = getNextPosition(currentPosition, string[currentPosition], string, endOfString, delimiterSet)
        ch = string[cursor]
        if cursor == endOfString:
            if cursor == currentPosition:
                return result
            else:
                result.append(string[currentPosition:cursor+1])
                if ch in delimiterSet:
                    result.append(ch)
                return result
            
        if ch in whiteSpace:
            if cursor == currentPosition:
                currentPosition+=1
                continue
            else:
                result.append(string[currentPosition:cursor])
                currentPosition = cursor+1
                continue
        if ch == "'":
            if string[cursor-1] in delimiterSet:
                flag = True
                currentPosition+=1
                continue
            if string[cursor+1] not in delimiterSet:
                currentPosition+=1
                #ch = string[cursor]
                continue
            else:
                if flag == True:
                    result.append(string[currentPosition:cursor-1])
                    flag = False
                else:
                    result.append(string[currentPosition:cursor])
                currentPosition = cursor+1
                continue
                #return Token
        if cursor == currentPosition: #others in delimiter set
            result.append(ch)
            currentPosition = cursor+1
            continue
        else:
            result.append(string[currentPosition:cursor])
            currentPosition = cursor
            continue
        return result

def getNextPosition(cursor, ch, string, endOfString, delimiterSet):
    while ch not in delimiterSet:
        if cursor == endOfString:
            return cursor
        cursor+=1
        ch = string[cursor]
    return cursor
                    

while True:
    try:
        text = input()
        if text == '':#flag para rodar direto no cmd
            continue
        print(tokenizer(text))
    except EOFError:
        break
