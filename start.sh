#!/bin/bash
a=`ls | grep *.py`
winpty python $a 
read -p $'\nPress enter to exit.  ' exit_bash