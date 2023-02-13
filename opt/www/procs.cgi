#!/bin/bash
. header.sh
echo "<h2>Running processes</h2>"
echo "<pre class=\"font-size:\" 10px;>"
ps -eo user,pid,%mem,%cpu,command --sort=pid
echo "</pre>"
cat footer.inc
