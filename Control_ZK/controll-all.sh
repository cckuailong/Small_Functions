#!/bin/bash

cmd="~/zookeeper/bin/zkServer.sh $1"
ssh master "$cmd"

for i in {1..2}
do
	ssh "slave"$i "$cmd"
done