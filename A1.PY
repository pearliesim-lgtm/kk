student={
    "id1":{"name":"tanu","class":"6th","age":9},
    "id2":{"name":"ayesha","class":"7th","age":13},
    "id3":{"name":"aahana","class":"8th","age":14},
    "id4":{"name":"tanu","class":"6th","age":9}
}
result={}
for key,value in student.items():
    if value not in result.values():
        result[key]=value
print(result)