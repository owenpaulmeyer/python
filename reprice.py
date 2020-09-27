
# function. string input
# parses string looking for prices
# reduce and replaces prices by 20%
# price?

# "Sally paid $20 for new shoes."
# "Last weekend I bought a sandwich for $18.95"
# "$#Q!@# Sally exclaimed. $38 was too much to pay for shoes."
# "I only paid six dollars"

# $.95 $0.95 $9.4


def toWords(st):
    return st.split()


def isPrice(st):
    if st[0] == '$':
        return True
    else:
        return False

def reprice(st):
    if not isPrice(st):
        return st
    else:
        st = st[1:]
        number = float(st)
        reduced = number * .8
        result = "${:,.2f}".format(reduced)
        return result

def myFunction(st):
    words = toWords(st)
    converted = list(map(reprice,words))
    return " ".join(converted)
    

    

# get words as list
# then iterate list of words;
# if a word does not start with '$' then append to result else pass word to helper function to convert and then append to result
# helper function converts price word into float; calcs 20% delta and subtracts to produce new value; convert new value back into string beginning with '$'




st = "Sally paid $30 for shoes, but I only paid $28.88"

print(myFunction(st))



