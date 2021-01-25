echo -n "Enter file 1 name: "
read filename1
echo -n "Enter file 2 name: "
read filename2

cat $filename1 $filename2 >> file_res

sort file_res
