if [ $# -eq 0 ]
then
  echo "Usage - filename.sh x y"
  echo "Where x and y are two numbers for which sum will be printed"
else
  sum=$(( $1 + $2 ))
  echo "sum is $sum"
fi
