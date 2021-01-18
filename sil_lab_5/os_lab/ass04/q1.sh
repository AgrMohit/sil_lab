read -p "Enter a number: " num
if [ $num -gt 0 ]
then
  echo "number is greater than 0"
elif [ $num -lt 0 ]
then
  echo "number is less than 0"
elif [ $num -eq 0 ]
then
  echo "number is equal to 0"
fi

