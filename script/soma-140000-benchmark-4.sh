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

# # Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-states -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
#         1699213295226380545\
#         1699213811275474102

# # Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-timegraph-arrows -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
#         "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
#         1699213295226380545 \
#         1699213811275474102

