#! /bin/bash
files="../clustering-docs/immidata/endata/04han/*.txt"
target="../clustering-docs/immidata/modata/04han/"
for f in $( ls $files ); do
    a=(${f//// })
    python pyHannanum/converter.py < $f > $target${a[5]}
    echo "finished..." ${a[5]}
done
