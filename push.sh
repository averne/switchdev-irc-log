#!/bin/bash

python3 organize.py

if [ $? -eq 0 ]; then
    export GIT_SSH_COMMAND='ssh -i id_rsa'
    git add '*.log'
    git commit -m "Add log files as of $(date +%D)"
    git push
fi
