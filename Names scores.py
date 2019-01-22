with open('p022_names.txt') as file_object:
    ori_str=file_object.read()
    names=ori_str.split('","')
    names[0]=names[0].lstrip('"')
    names[-1]=names[-1].rstrip('"')
names.sort()
name_score_rec=[]
for name in names:
    sum_char=0
    for i in name:
        char_value=ord(i)-64
        sum_char+=char_value
    name_score=(1+names.index(name))*sum_char
    name_score_rec.append(name_score)
print(sum(name_score_rec))

