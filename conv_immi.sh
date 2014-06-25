#! /bin/bash
files="../clustering-docs/immidata/endata/93chosun/*.txt"
target="../clustering-docs/immidata/modata/93chosun_test/"
for f in $( ls $files ); do
    a=(${f//// })
    python pyHannanum/converter_stop.py < $f > $target${a[5]}
    echo "finished..." ${a[5]}
done
