i = 1
registration_codes = []
while i < 6:
    b = input()
    registration_codes.append(b)
    if "FBI" in b:
        print(i)
    i += 1

cia_blimps_found = False
for code in registration_codes:
  if "FBI" in code:
    cia_blimps_found = True
    break

if not cia_blimps_found:
  print("HE GOT AWAY!")