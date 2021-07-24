phrase = "Don't panic!"
plist = list(phrase)
slist = plist.copy()
print(phrase)
print(plist)
print(len(plist))
for i in range(4):
    plist.pop()
    print(plist)
plist.pop(0)
print(plist)
plist.remove("'")
print(plist)
plist.extend([plist.pop(), plist.pop()])
print(plist)
plist.insert(2, plist.pop(3))

new_phrase = ''.join(plist)

print(plist)
print(len(plist))
print(new_phrase)

print(slist[:5])
print(slist[6:])