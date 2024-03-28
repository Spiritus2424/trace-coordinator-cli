#!/bin/bash

for HOST in l4714-02.info.polymtl.ca l4714-03.info.polymtl.ca l4714-04.info.polymtl.ca l4714-05.info.polymtl.ca l4714-06.info.polymtl.ca l4714-07.info.polymtl.ca l4714-08.info.polymtl.ca l4714-13.info.polymtl.ca l4714-14.info.polymtl.ca l4714-16.info.polymtl.ca l4714-17.info.polymtl.ca l4714-18.info.polymtl.ca l4714-24.info.polymtl.ca l4714-20.info.polymtl.ca l4714-21.info.polymtl.ca l4714-22.info.polymtl.ca l4714-23.info.polymtl.ca l4714-25.info.polymtl.ca l4714-26.info.polymtl.ca l4714-27.info.polymtl.ca
do
    source /workspaces/trace-coordinator-cli/script/1080p/benchmark-8.sh $HOST &
done
