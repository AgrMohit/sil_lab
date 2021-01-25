echo -n "Enter string 1: "
read str1
echo -n "Enter string 2: "
read str2

res="$str1 $str2"
echo "Concatenated string: $res"
len=`expr length "$res"`
echo "String lenght: $len"
