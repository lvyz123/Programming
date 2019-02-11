with open('p042_words.txt') as file_object:
    file_text=file_object.read()
    word_list=file_text.split('","')
    word_list[0]=word_list[0].lstrip('"')
    word_list[-1]=word_list[-1].rstrip('"')
max_len_word=max([len(word) for word in word_list])
trai_list=[1];n=1;trai_count=0
while trai_list[-1]<26*max_len_word:
    n+=1
    trai_list.append(n*(n+1)/2)
for word in word_list:
    sum_value=0
    for letter in word:
        if ord(letter)<=90:
            letter_value=ord(letter)-64
            sum_value+=letter_value
        else:
            letter_value=ord(letter)-96
            sum_value+=letter_value
    if sum_value in trai_list:
        trai_count+=1
print(trai_count)
