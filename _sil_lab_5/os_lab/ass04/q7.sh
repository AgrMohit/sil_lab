if [ $# -eq 0 ]
then
  echo "ERROR: This script requires two numbers passed as arguments"
  echo "Usage - filename.sh num1 num2"
else
  if [ $1 -gt $2 ]
  then
    echo "$1 is larger"
  else
    echo "$2 is larger"
  fi
fi
