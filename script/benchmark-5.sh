#!/bin/sh
IP="172.17.0.3"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "c39b083a-e15a-3fcb-b53d-8a1fd3ca07d0" \
        --uuids "fcdb26d5-ad68-3a1d-aba6-a4c0666839ca" \
        --uuids "e675df37-e253-36eb-8172-a58d36453fe3" \
        --uuids "c2698e55-400d-356c-854b-22cb44a1d047" \
        --uuids "3c9c24b7-9469-3ab3-bdb2-b4c63948ab60" \
        --uuids "83176a79-1364-3dc0-868d-f7aa331dcf4f" \
        --uuids "4e4ea12e-4a24-3da1-b326-28279fc6287b" \
        --uuids "90bcaaa3-87fa-3e74-bb43-e84cae83eadc" \
        --uuids "64aafb24-953f-35e3-842b-03a15e8849b8" \
        --uuids "e5d06115-e733-36dc-bbe9-29432eeb77a5" \
        --uuids "aebd8ea8-30b3-3755-98d7-59ce6e1e7042" \
        --uuids "8eba9691-1121-333d-a1c3-3917fb138b0d" \
        --uuids "4b933923-f9e0-33a8-8127-a35cffc2361d" \
        --uuids "1dbcae00-36ca-3a54-b71c-96a9a68030a3" \
        --uuids "91ea3062-b38e-381b-a2af-6bfc36cf00c1" \
        --uuids "f1d33602-09e3-3c0d-a372-115baf14ec9b" \
        --uuids "8a0ff34b-9ca5-30a4-8556-adf77e9b4f19" \
        --uuids "7e2a4b29-9d70-3044-82a7-0448214d0a78" \
        --uuids "842e8ed8-cbf2-3a6b-b396-a53273910da9" \
        --uuids "65d6b1bf-9192-307d-aac6-57db8c99ec0a"



# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


############################################## TimeGraph Case Extreme ##############################################

# # Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"

# # Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-states -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
#         1701205212748171586\
#         1701205476581683428

# # Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-arrows -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
#         1701205212748171586\
#         1701205476581683428   


############################################## TimeGraph Case Realist ##############################################

# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-states -v --nb-times 4096 \
        -i 1 -i 2 -i 3 -i 4 -i 5 -i 6 -i 7 -i 8 -i 9 -i 10 \
        -i 11 -i 12 -i 13 -i 14 -i 15 -i 16 -i 17 -i 18 -i 19 -i 20 \
        -i 21 -i 22 -i 23 -i 24 -i 25 -i 26 -i 27 -i 28 -i 29 -i 30 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1701205212748171586\
        1701205476581683428\
        


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-arrows -v --nb-times 4096 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1701205212748171586\
        1701205476581683428\

############################################## XY Case Extreme ##############################################

# # Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"

# # Case Extreme
# # Get XY: CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy -v --nb-times 3000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
#         1701205212748171586\
#         1701205476581683428

############################################## XY Case Realist ##############################################

# Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"

# Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy -v --nb-times 4096 \
        -i 1 -i 2 -i 3 -i 4 -i 5 -i 6 -i 7 -i 8 -i 9 -i 10 \
        -i 11 -i 12 -i 13 -i 14 -i 15 -i 16 -i 17 -i 18 -i 19 -i 20 \
        -i 21 -i 22 -i 23 -i 24 -i 25 -i 26 -i 27 -i 28 -i 29 -i 30 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1701205212748171586\
        1701205476581683428
        