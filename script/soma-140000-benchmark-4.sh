#!/bin/sh
IP="l4714-02.info.polymtl.ca"
PORT=5000
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# # Create Experiment
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     create-experiment -v "Experiment Name" \
        

# # Get Output Descriptors
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# # Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"

# # Case Extreme
# # Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-states -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
#         1701205212748171586\
#         1701205476581683428

# # Case Extreme
# # Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-arrows -v --nb-times 15000 "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
#         1701205212748171586\
#         1701205476581683428

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

# # Get XY Tree - CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"

# # Case Extreme
# # Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
#         1701205212748171586\
#         1701205476581683428

# # Case Realist
# # Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-xy -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
#         \
#         