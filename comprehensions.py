ele=[1,2,3,4,5,6,7,8,9]
out=[e for e in ele if e%2==1]
print(out)

output::[1, 3, 5, 7, 9]

ele=[1,2,3,4,5,6,7,8,9]
doubled=[val*2 for val in ele]
print(doubled)

output::[2, 4, 6, 8, 10, 12, 14, 16, 18]

names=["kranthi","rakesh"]
changed=[name.upper() for name in names]
print(changed)

output::['KRANTHI', 'RAKESH']

nested=[[1,2,3],[4,5,6]]
single=[j for i in nested for j in i]
print(single)

output::[1, 2, 3, 4, 5, 6]

num=[1,2,3,4]
square={x:x**2 for x in num}
print(square)

output::{1: 1, 2: 4, 3: 9, 4: 16}

string="this is an example of python programming"
freq={x: string.count(x) for x in string if x!=" "}
print(freq)

output::{'t': 2, 'h': 2, 'i': 3, 's': 2, 'a': 3, 'n': 3, 'e': 2, 'x': 1, 'm': 3, 'p': 3, 'l': 1, 'o': 3, 
'f': 1, 'y': 1, 'r': 2, 'g': 2}

dictionary={
    "apple":"red",
    "orange":"orange",
    "mango":"yellow"
}
changed={dictionary key: for key in dictionary}
print(changed)


word=["philanthoripist","periperi","nostalgia"]
length={key : len(key) for key in word}
print(length)

output::{'philanthoripist': 15, 'periperi': 8, 'nostalgia': 9}


val={
    "a":50,
    "b":67,
    "c":45,
    "d":25
}
greater={k:v for k,v in val.items() if v>50}
print(greater)

output::{'b': 67}

string="python programming"
vowels={ch for ch in string if ch in "aeiou"}
print(vowels)

output::{'o', 'i', 'a'}

sentence="this is a sentence in python"
title={word.title() for word in sentence.split(" ")}
print(title)

output::{'This', 'Sentence', 'In', 'Is', 'Python', 'A'}

word={"java","python","c","aws","azure","php","oracle"}
vowels={tech for tech in word if tech[0] in "aeiou"}
print(vowels)

output::{'aws', 'oracle', 'azure'}

matrix=[
    [1,2],
    [3,4],
    [4,5]
]
res=[]
for j in range(len(matrix[0])):
    row=[]
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    res.append(row)
print(res)

output::[[1, 3, 4], [2, 4, 5]]