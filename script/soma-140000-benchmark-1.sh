#!/bin/sh
IP="172.17.0.3"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# # Create Experiment
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     create-experiment -v "Experiment Name" \
#         --uuids "6f2b0f1a-c8cf-36f1-83f0-2f4932c031ba" \
#         --uuids "99eda657-fadb-3e14-9f75-675120c77bb4" \
#         --uuids "16adae32-7ea4-3ed6-a314-70a21b6768b3" \
#         --uuids "82f3b394-afbe-3651-9f1f-389d8068c894" \
#         --uuids "dcf4463d-6a04-3a74-b577-eb1f8d83361a" \
#         --uuids "06c0faa4-425f-33a3-b494-23546df44104" \
#         --uuids "fa7f6c9f-ed86-360b-8761-29715353dbf3" \
#         --uuids "ebc84662-76d3-38e4-8e52-7a69f33ac396" \
#         --uuids "26b8af97-5819-3d16-a9da-42ab767b4ca6" \
#         --uuids "54464a07-b470-3a25-8138-a94e07591042" \
#         --uuids "ba492294-2252-345f-8951-5be40e2aca57" \
#         --uuids "e9fe111e-94bc-3ac5-96ea-7f86013d9361" \
#         --uuids "8da0dc76-8876-3a3e-80ef-5ed773b521bb" \
#         --uuids "2bdcb6f1-dd4c-3f16-bdd3-85bc00af6125" \
#         --uuids "7ac0ab48-8100-375e-b928-4f1a8f11dc98" \
#         --uuids "d3c64390-588d-3f55-8a4b-1852a7fbe4e7" \
#         --uuids "2c725cce-589e-30bd-8804-e5cdb992a49d" \
#         --uuids "498f6240-eb24-3637-a402-4d72b61c3c72" \
#         --uuids "f87d844f-b6c1-3032-9b93-19f62aef8989" \
#         --uuids "67fb04ee-8459-35c1-a116-87c974e0f6cd" 

# # Get Output Descriptors
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b

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

