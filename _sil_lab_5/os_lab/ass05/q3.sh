read -p "Enter beginning of range: " beg
read -p "Enter ending of range: " end
sum=0
for (( i=$beg; i <= end; i++))
do
  if [ $(( $i % 2 )) -eq 0 ]
  then
    sum=$(( $sum + $i ))
  fi
done
echo "sum of even numbers from $beg to $end: $sum"