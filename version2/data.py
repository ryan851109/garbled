import hashlib

file_data = input("請輸入檔案名稱 : ")
try :
    fp = open(file_data, "r")
except :
    print("無此檔案")
    exit()

lines = fp.readlines()
#print(lines)
all_line = []
for line in lines:                          #字串切割
    all_line.append(line.split(','))

fp.close()

feature = []
for line in all_line :
    feature_hash = ''
    for content in line:
        content = content.replace('\n','')
        hash_value = hashlib.md5()
        hash_value.update(content.encode('utf-8'))
        feature_hash = feature_hash + (bin(int(hash_value.hexdigest()[-1],16))[-2:]).replace('b','0')
    feature.append(feature_hash)


#print(answer)
fp2 = open("feature.txt" , 'w')
for i in range(len(feature)):
    fp2.write(str(feature[i]) + '\n')

fp2.close()