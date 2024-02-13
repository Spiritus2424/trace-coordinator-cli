#!/bin/sh
IP="172.17.0.3"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "16adae32-7ea4-3ed6-a314-70a21b6768b3" \
        --uuids "e359a33a-324d-3bc9-83b4-43199c27c382" \
        --uuids "a49cb627-07fc-3a1f-ac06-34942fdc02ec" \
        --uuids "3939b89f-51c1-32ee-a5fa-24c58b9afd3e" \
        --uuids "03a07e2b-ed16-375e-b221-2859eee20de9" \
        --uuids "6f2b0f1a-c8cf-36f1-83f0-2f4932c031ba" \
        --uuids "9f8169a0-2c31-3d0d-ac6d-eba3db005bca" \
        --uuids "ea117431-3693-3558-b0c4-d01dc6ef9579" \
        --uuids "d218899d-a461-399e-b4ce-537ec42a4fd9" \
        --uuids "1c9c9793-8c88-3825-b009-99cfba339cdf" \
        --uuids "82f3b394-afbe-3651-9f1f-389d8068c894" \
        --uuids "78af0fe0-08d9-3c9a-b334-25cc7b1bba0f" \
        --uuids "6fa32029-fe4c-3142-8c7e-18261e118b6c" \
        --uuids "99eda657-fadb-3e14-9f75-675120c77bb4" \
        --uuids "cefe74cd-76d4-3b7e-8cac-221a68c7161c" \
        --uuids "5fd35952-cb73-3787-adf1-7a94d6e2e1af" \
        --uuids "70b48655-372b-3688-a9f8-c935a67368e9" \
        --uuids "f43d3e89-fd91-3048-85f7-952bf3e1e7cc" \
        --uuids "26b8af97-5819-3d16-a9da-42ab767b4ca6" \
        --uuids "fb8fcf4c-5d15-3d06-9a6e-3ba44508cca4"


# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"

# Case Extreme
# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-states -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1701205212748171586\
        1701205476581683428

# Case Extreme
# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-arrows -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1701205212748171586\
        1701205476581683428

# # Case Realist
# # Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-states -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
#         \
#     

# # Case Realist
# # Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-arrows -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
#         \
#         

# Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"

# Case Extreme
# Get XY: CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy -v --nb-times 3000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1701205212748171586\
        1701205476581683428

# # Case Realist
# # Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
#         \
#         