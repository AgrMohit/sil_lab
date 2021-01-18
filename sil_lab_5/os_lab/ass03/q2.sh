echo -n "Enter number 1: "
read num1
echo -n "Enter number 2: "
read num2
echo -n "Enter number 3: "
read num3
echo -n "Enter number 4: "
read num4

sum=`expr $num1 + $num2 + $num3 + $num4`
avg=`expr $sum / 4`

echo "Sum is: $sum"
echo "Average is: $avg"
