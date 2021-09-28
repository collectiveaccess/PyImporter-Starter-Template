#!/bin/bash

# get the source directory of a bash script https://stackoverflow.com/a/246128
BASE="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# get parent directories
SCRIPT_DIR=`echo $BASE | sed s/\\\/bulk_import//`
PROJECT_DIR=`echo $SCRIPT_DIR | sed s/\\\/scripts//`

# get DATA_DIR from .env file
envar=`grep DATA_DIR $PROJECT_DIR/.env`
# remove quotes
regex="[\"'](.*)[\"']$"
if [[ $envar =~ $regex ]]
then
    DATA_DIR="${BASH_REMATCH[1]}"
else
    echo "DATA_DIR not found in .env" >&2
    exit
fi

python "$SCRIPT_DIR/demo.py" create_records --metadata_id 1
