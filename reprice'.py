
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
  
