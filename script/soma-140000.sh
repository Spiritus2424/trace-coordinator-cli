#!/bin/sh
IP="172.17.0.1"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/spiritus/ws/trace-coordinator/traces/hpc-soma-140000

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "2555ab54-1c49-3b3d-a891-02fea0eed441"\
        --uuids "a125f3f2-288f-345b-8921-5c0716e27f30"\
        --uuids "d85badd5-67c2-36df-aedc-aff9456a4992"\
        --uuids "ed94a71b-172e-3979-97d3-3a26fc7d86a4"\
        --uuids "79f0e3aa-9030-3166-b2fa-f1f23bae2d1c"\
        --uuids "1c374a28-1f39-368a-8fa2-340a6b3dc4c2"\
        --uuids "efd48902-808e-310e-beb0-383d9aaf80ef"\
        --uuids "5f5badd4-cbbc-3f9a-8b41-a291b0033a44"\
        --uuids "58211610-d2eb-3686-a331-cfb6d43ecbe5"\
        --uuids "62ee2393-4568-3232-b53a-1c039aed7efa"\
        --uuids "da13cfda-ce48-3c51-a7a3-3c5ed8ba29e9"\
        --uuids "c02a8e66-d1c6-359b-ae30-ca9ffa598825"\
        --uuids "795d29af-0c7c-3fda-9d50-e2ed709ea324"\
        --uuids "34f49521-ed74-3cd3-82a9-43c0e468dbc7"\
        --uuids "9a5ff73d-1ef7-3509-bfe9-f4cfc0abd4d1"\
        --uuids "98a0470a-3d64-381f-82d0-c99f12e1e70f"\
        --uuids "4559b756-5fc4-3d5b-a444-9fc690fc7878"\
        --uuids "9268504c-72b5-3a80-a1a8-231a1737b28e"\
        --uuids "a58051e6-a6e5-35ab-ad9c-ad7d3bb7d610"\
        --uuids "c120baf7-b0e7-34b9-8493-7dbb162a6675"

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

