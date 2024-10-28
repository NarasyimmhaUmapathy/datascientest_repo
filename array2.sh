#!/bin/bash
rtx=(rtx3060 rtx3070 rtx3090 rx6700)
echo "$(date)" >> file_cards.txt
for x in ${rtx[*]}
    
    do
      echo "$x"
      sales=$(curl -s "http://0.0.0.0:5000/{"$x"}" )
      
      echo $sales:$x >> file_cards.txt
    done
