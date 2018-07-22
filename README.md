##This garbled circuit uses AES Crypto
##The version is only to input one file. If you want input more file, you could go to the version2.

If you want to run the program :

>"python3 {program_name}.py"

If you want to run the encrypto-search model,you can follow the step :

>Step1. Run the produce_feature_table.py

>Step2. Run the compare_bit.py

>Step3. Run the n_bit_counter_function.py

>Step4. Run the key_convert_number.py

>So,you can know the degree of difference.

==============================================

##Explain the function :

###produce_feature_table.py :

>產生每筆特徵向量的garbled circuit

>並儲存在一個名為"feature_garbled_table.txt"的文件裡

###compare_bit.py :

>讀取"feature_garbled_table.txt"裡頭的資料

>然後透過輸入原先產生garbled circuit的seed與想要查詢的資訊特徵

>便會產生出比較結果的garbled circuit

>並儲存在一個名為"compare_result.txt"的文件裡

###n_bit_counter_function.py :

>輸入原先產生garbled circuit的seed

>便會開始計算差異度

>差異度結果會儲存一個名為"counter.txt"的文件裡

>並且此function內garbled circuit的key會儲存在一個名為"counter_key.txt"的文件裡

###key_convert_number.py :

>讀入"counter.txt"與"counter_key.txt"

>把差異性用數字顯示出來
