echo -n "Enter file name: "
read filename

cat $filename | tr "[a-z]" "[A-Z]"
