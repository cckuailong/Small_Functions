#!/bin/bash

pass="password"
username="username"
ip="host ip"
port=22

expect -c " \
  set timeout 20
  spawn bash -c \"ssh -NfR 6666:localhost:22 $username@$ip\"
  expect {
    timeout {exit 138}
    -re \".*password.*\"
  }
  send -- \"$pass\r\"
  expect eof
"


