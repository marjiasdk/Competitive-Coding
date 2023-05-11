symbol = input()

i = 0
smiles = []
while i < len(symbol):
    if symbol[i:i+3] in [";-)", ":-)"]:
        smiles.append(i)
        i += 3
    elif symbol[i:i+2] in [":)", ";)"]:
        smiles.append(i)
        i += 2
    else:
        i += 1

i = 0
while i < len(smiles):
    print(smiles[i])
    i += 1