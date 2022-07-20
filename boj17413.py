s = input().split()
string_s = ''
for i in range(len(s)):
    string_s +=s[i]
print(string_s)
tags = []
def find_tag(s):
    string_s = str(s)
    total_size = len(string_s)
    opentag_index = []
    closetag_index = []
    for i in range(total_size):
        if string_s[i] == '<':
            opentag_index.append(i)
        elif string_s[i] =='>':
            closetag_index.append(i)
    return(opentag_index,closetag_index)
opentag_index = find_tag(s)[0]
closetag_index = find_tag(s)[1]
for i in range(len(opentag_index)):
    a = opentag_index[i]
    b = closetag_index[i]
    cut_tag = string_s[a:b+1]
    tags.append(cut_tag)
print(tags)
for k in tags:
    final = string_s.strip(k)
print(final)
    
print(opentag_index)
print(closetag_index)
print(tags)

