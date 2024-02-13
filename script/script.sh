#!/bin/sh
# IP="l4714-05.info.polymtl.ca"
# PORT=5000
IP="132.207.72.41"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/ahmad/ws/trace-coordinator/traces/hpc-soma-140000

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "af06dc20-9ded-3d7c-9f20-ce39066585ec" \
        --uuids "6f5ddfd6-0370-36dc-b24c-2f7b78fd1243" \
        --uuids "e46799a4-0397-3d9b-a4ff-802bb86361b0" \
        --uuids "21d3fa41-9548-3d74-9c97-43f09a5cc5a5" \
        --uuids "fed167d7-19c1-3b17-99fa-fb64167bea1c" \
        --uuids "8f9aed01-9eb7-36a8-b1a8-3f1599e65b62" \
        --uuids "f009e21c-8dbe-3d2b-9406-06fd456802a8" \
        --uuids "ee567596-79d8-3024-b3b2-494eafff83e0" \
        --uuids "45225089-58b5-3640-98bd-5d9f8bca6bf1" \
        --uuids "fdecdfce-091f-336d-8533-f83d7261d654" \
        --uuids "8ee2dc63-bad2-3dda-9623-95b3ac663530" \
        --uuids "557baf4d-632c-3c30-9405-f01e4410ba2a" \
        --uuids "51b35327-2962-32de-9fe0-13e1b2b45731" \
        --uuids "86c2f591-bc39-326f-bed9-be2039d48f1e" \
        --uuids "432535e6-9c16-391b-92ab-f0dcb4d1f35b" \
        --uuids "48fe0c6f-9cc0-386f-b6dd-0edb431dba11" \
        --uuids "336f6dbd-7202-3f90-8f3d-6a9fb4e84e06" \
        --uuids "1f09d4b3-4798-307b-af06-fd77a60f9f7a" \
        --uuids "b2725ab3-fab1-317b-a2a7-80617d1d7651" \
        --uuids "f6215043-8e28-36f0-a139-46a649724736"




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

