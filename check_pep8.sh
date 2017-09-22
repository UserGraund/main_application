#!/bin/sh

echo "files with pep8 errors:"

pep8 --max-line-length=120 . | \

while read LINE; do
    echo " * $LINE"
done

echo "files without unicode_literals import:"

find . -name '*.py' -not -name '__init__.py' | \

while read FILE; do
    grep "from __future__ import unicode_literals" "$FILE" > /dev/null || \
    echo " * $FILE"
done

