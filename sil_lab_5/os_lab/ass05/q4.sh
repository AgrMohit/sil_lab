#!/bin/bash
if [ $# -eq 0 ]
then
  echo "Usage - filename.sh <username>"
else
  echo "Welcome $1"
  for (( i=0; i < 5; i++ ))
  do
    echo "Welcome"
  done
fi

