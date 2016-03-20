from reddit import reddit

def load_subs():
    f = open('config', 'r')
    subs = []
    for line in f:
        if 'sub_reddit' in line:
            s = line.split(':')
            s = s[1].replace(' ', '').replace('\'', '').replace('[', '').replace(']', '')
            s = s.split(',')
            for sub in s:
                subs.append(sub)
    f.close()
    return subs

subs = load_subs()
obj = []
for s in subs:
    obj.append(reddit(s))
    print(s)

#print(obj.count)

for o in obj:
    o.get_sub()

#r2 = reddit('programming')
#r2.get_sub(5)
