#!/bin/sh
IP="l4714-01.info.polymtl.ca"
PORT=5000
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "65c6e2e6-9910-3005-89df-1a25943e010c" \
        --uuids "2f9603ec-67af-3277-a9ab-308060795960" \
        --uuids "26407711-f072-38e4-ad99-b6116d23ad99" \
        --uuids "e6ff175d-ff54-3945-bb02-1159e4a0e5aa" \
        --uuids "eb356fe2-cb50-3ce5-9b0a-f53829de6672" \
        --uuids "cc8216bd-3f73-3e77-8ef4-d0595891150a" \
        --uuids "29980495-6d16-37f9-a9df-3a9f8acf8cae" \
        --uuids "031d7f5f-35be-3164-9963-6b1b5f2b182e" \
        --uuids "f419a3b4-411a-3e33-b7ae-fabd2e368aa8" \
        --uuids "e2442361-1282-3b7b-b6ff-e77992492100" \
        --uuids "be0367bc-65cd-34a3-9f6a-77d2218bca89" \
        --uuids "4e82d256-fe9e-3648-8cab-aea381f00028" \
        --uuids "3b912096-e874-3cd6-971b-6a06e472bf65" \
        --uuids "fb745074-a75b-3ea6-aa7c-c95994dfcbb5" \
        --uuids "9aadd930-cf2a-3fe5-aaa8-f96aae2a8c95" \
        --uuids "3dd49b48-a7a4-3d5f-b7e8-7b039bac14b8" \
        --uuids "fcc77e94-c876-33c4-84db-d133393beae3" \
        --uuids "d5938817-0a0f-3e24-a360-1eeccf4a7a19" \
        --uuids "2fa00ea7-a4f4-3f40-bd98-9e30b395c7cf" \
        --uuids "c5e8c3cf-1f59-3f0b-a7c1-5d15d07e5b78"


# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"

# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-states -v --nb-times 65000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1701205212748171586\
        1701205476581683428

# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-arrows -v --nb-times 65000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1701205212748171586\
        1701205476581683428

