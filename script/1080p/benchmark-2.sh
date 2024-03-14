#!/bin/sh
IP="172.17.0.2"
PORT=8080

############################################## Resolution 1080p (1920x1080) ##############################################

# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "16adae32-7ea4-3ed6-a314-70a21b6768b3" \
        --uuids "e359a33a-324d-3bc9-83b4-43199c27c382" \
        --uuids "6f2b0f1a-c8cf-36f1-83f0-2f4932c031ba" \
        --uuids "9f8169a0-2c31-3d0d-ac6d-eba3db005bca" \
        --uuids "1c9c9793-8c88-3825-b009-99cfba339cdf" \
        --uuids "82f3b394-afbe-3651-9f1f-389d8068c894" \
        --uuids "99eda657-fadb-3e14-9f75-675120c77bb4" \
        --uuids "cefe74cd-76d4-3b7e-8cac-221a68c7161c" \
        --uuids "26b8af97-5819-3d16-a9da-42ab767b4ca6" \
        --uuids "fb8fcf4c-5d15-3d06-9a6e-3ba44508cca4" \
        --uuids "ff433385-728d-30c3-b0c4-c7582ac55cfc" \
        --uuids "dcf4463d-6a04-3a74-b577-eb1f8d83361a" \
        --uuids "15968462-0f0f-34e3-8547-aedfb48ebab7" \
        --uuids "06c0faa4-425f-33a3-b494-23546df44104" \
        --uuids "24568124-afa0-3b40-a8aa-ebdef50577c9" \
        --uuids "fa7f6c9f-ed86-360b-8761-29715353dbf3" \
        --uuids "ebc84662-76d3-38e4-8e52-7a69f33ac396" \
        --uuids "5ab1511f-e9c3-375f-8174-25d02419e1e6" \
        --uuids "54464a07-b470-3a25-8138-a94e07591042" \
        --uuids "2dded9ad-cbcf-3020-908b-da4bbf131b2a"

# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"


# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-states -v --nb-times 1920 --tree "Get Timegraph Tree.json" --process "soma_base.gnu_m" --nb-items 40 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1701205212748171586\
        1701205476581683428


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-arrows -v --nb-times 1920 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1701205212748171586\
        1701205476581683428

# Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"


# Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-xy -v --nb-times 1920 --tree "Get XY Tree.json" --process "soma_base.gnu_m" --nb-items 40 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1701205212748171586\
        1701205476581683428