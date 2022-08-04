#! /bin/bash

# Este archivo limpia el file mock_data
echo "Este archivo lo creó $USER"
tail -n+2 MOCK_DATA.csv |  awk -F, '{print "\"" $3 "\",", "\"" $4 "\",", "\""$5"\""}' | sort -k 1 -n | sed 's/ //g' > sort.txt
echo "Listo."