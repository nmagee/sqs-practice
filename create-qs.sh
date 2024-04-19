#!/bin/bash

INFILE="students.txt"

while read -r LINE
do
  printf '%s\n' "$LINE"
  aws sqs create-queue --queue-name $LINE --attributes file://attributes.json
done < "$INFILE"


