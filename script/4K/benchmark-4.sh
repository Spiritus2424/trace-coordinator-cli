#!/bin/sh
IP="l4714-02.info.polymtl.ca"
PORT=5000

############################################## Resolution 4K (3840x2160) ##############################################

# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "0d1da35e-0ae0-33d0-8040-7fee263787ed" \
        --uuids "8d9a0337-4762-388e-9eab-9df6c3342348" \
        --uuids "52c8c1ac-53ce-3249-a6c2-4cf7ca40833e" \
        --uuids "a596793e-bdea-349e-bd08-1a1014bc34c2" \
        --uuids "713433b7-097e-3af8-be1c-1c3401d00e3c" \
        --uuids "35a5cb95-2baa-34d8-b238-a53b7d00de0a" \
        --uuids "6eba1e69-cce8-3d12-be1e-933ec1fb8e30" \
        --uuids "013e1ba1-cf97-37d8-9e64-0e50a0efb16b" \
        --uuids "1593140f-ddc9-35ee-b647-8e0d3a8b50c9" \
        --uuids "6ba10c54-cda5-3932-b2f8-99b98420258f" \
        --uuids "347f00fa-fa45-333a-bd18-aa4219274eb8" \
        --uuids "b7f18281-085e-347b-b465-d3e18a58586a" \
        --uuids "a28424cc-9fe0-32e0-b08b-0b187690c752" \
        --uuids "a94f3cfa-2a76-388e-9a9c-38c0a98f2d1c" \
        --uuids "7740aee7-faf4-3c91-bd8e-b8be058cc88a" \
        --uuids "e7b31cad-5db8-3bf7-9d4d-6e2a2e9c00a6" \
        --uuids "f1824e1f-7b04-395d-a08c-c94c89afd42a" \
        --uuids "78b17b4e-c1fb-3b0f-83f8-45d979b6d29c" \
        --uuids "1a273b53-3b48-33bc-8390-dea35fa19f71" \
        --uuids "0a301331-0b19-3ed4-83ac-fd7d6ba238ad"


# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"


# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-states -v --nb-times 3840 --tree "Get Timegraph Tree.json" --process "soma_base.gnu_m" --nb-items 60 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1701205212748171586\
        1701205476581683428


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-arrows -v --nb-times 3840 \
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
    concrete-get-xy -v --nb-times 3840 --tree "Get XY Tree.json" --process "soma_base.gnu_m" --nb-items 60 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1701205212748171586\
        1701205476581683428