#!/usr/bin/env bash
./createllms.sh
llms_txt2ctx llms.txt >llms-ctx.txt
llms_txt2ctx llms.txt --optional true > llms-ctx-full.txt
pysym2md --output_file apilist.txt monsterui
