read -p "enter a number: " num
rem=$(( $num % 2 ))

if [ $rem -eq 0 ]
then
  echo "number is even"
else
  echo "number is odd"
fi
