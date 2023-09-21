#!/bin/bash
###############################################################
# Description:
#   This script will launch the python script of mapt_helper
#   (forwarding any arguments passed to this script).
# 
# Copyright (c) 2023 Nokia
###############################################################

_term(){
    echo "Caught signal SIGTERM !! "
    # when SIGTERM is caught: kill the child process
    kill -TERM "$child" 2>/dev/null
}

# associate a handler with signal SIGTERM
trap _term SIGTERM

# set local variables
virtual_env="/opt/mapt_helper/venv/bin/activate"
main_module="/usr/local/bin/mapt_helper/mapt_helper.py"

# start python virtual environment, which is used to ensure the correct
# python packages are installed and the correct python version is used
source "${virtual_env}"

# update PYTHONPATH variable with the agent directory and the SR Linux gRPC
export PYTHONPATH="$PYTHONPATH:
_term(){
    echo "Caught signal SIGTERM !! "
    # when SIGTERM is caught: kill the child process
    kill -TERM "$child" 2>/dev/null
}