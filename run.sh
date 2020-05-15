#!/usr/bin/env zsh


APP_NAME="iconthemefolders"
SCRIPT_DIR=$(dirname "$0")
APP_DIR=$(dirname "$SCRIPT_DIR")
APP="iconthemefolders/__main__.py"
FUNC="$($APP)"

#How to execute instead of printing?
#"$($FUNC)"
#"$FUNC"
#$FUNC
echo "$FUNC"