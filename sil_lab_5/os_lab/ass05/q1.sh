#!/bin/sh
read -p "Enter a number: " num
sum=0
rem=0
while [ $num -gt 0 ]
do
  rem=$(( $num % 10 ))
  num=$(( $num / 10 ))
  sum=$(( $sum + $rem ))
done
echo "sum of digits: $sum"

