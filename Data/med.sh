#!/bin/bash
let th=0
let tt=0
let td=0
for l in $(tail -5 $1| cut -d , -f 2,3,4)
do
th=$(echo "scale=12; $th+$(echo $l | cut -d , -f 1)" | bc) 
tt=$(echo "scale=12; $tt+$(echo $l | cut -d , -f 2)" | bc) 
td=$(echo "scale=12; $td+$(echo $l | cut -d , -f 3)" | bc) 
done
th=$(echo "scale=2; $th/5" |bc)
tt=$(echo "scale=2; $tt/5" |bc)
td=$(echo "scale=2; $td/5" |bc)
echo -e $th"\t"$tt"\t"$td

