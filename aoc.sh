#!/bin/bash

DAY=$( date | awk ' { print $2 } ' )
echo "Pulling input for day $DAY"
OUTPUT="./$DAY.txt"
echo "Writing to file: $OUTPUT"

URL="https://adventofcode.com/2021/day/$DAY/input"
SESSION="53616c7465645f5f9c677e64cf30665627b9357e8052e095b6402e2d4c796677df523d22b18ddb6f6f2dd27951b6faf5"

curl --location --request GET "$URL" --header "Cookie: session=$SESSION" -o "$OUTPUT"
echo "Happy Solving :)"
