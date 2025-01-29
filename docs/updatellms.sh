#!/usr/bin/env bash
./createllms.sh
pysym2md --output_file apilist.txt monsterui
llms_txt2ctx llms.txt >llms-ctx.txt

