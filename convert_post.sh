#! /bin/bash
files="../blog/post/*.md"
target="../kepler-page-suggestion/postv0/"
for f in $( ls $files ); do
    a=(${f//// })
    python pyHannanum/converter_skip2line.py < $f > $target${a[3]}
    echo "finish..." ${a[3]}
done
