#!/bin/sh
IP="172.17.0.3"
PORT=8080

############################################## Resolution QHD (2560x1440) ##############################################

# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "c39b083a-e15a-3fcb-b53d-8a1fd3ca07d0" \
        --uuids "0d6a8f97-2244-3317-b855-72a9aa1762f2" \
        --uuids "fcdb26d5-ad68-3a1d-aba6-a4c0666839ca" \
        --uuids "69f71e05-7539-366c-9b26-3e37ba67dbb9" \
        --uuids "6eb1fdd5-9632-364a-92db-dc6bcd6ef29e" \
        --uuids "e675df37-e253-36eb-8172-a58d36453fe3" \
        --uuids "6f1dde8e-6f39-3d3d-a511-8ae087e8990d" \
        --uuids "c2698e55-400d-356c-854b-22cb44a1d047" \
        --uuids "3c9c24b7-9469-3ab3-bdb2-b4c63948ab60" \
        --uuids "d2c9aae8-a955-339f-aef9-f7ff82dfb0ef" \
        --uuids "6e46babd-b1fd-332f-9438-db79d32fbb54" \
        --uuids "83176a79-1364-3dc0-868d-f7aa331dcf4f" \
        --uuids "ceafce67-cae4-3bb5-893e-84b030c1f85a" \
        --uuids "4e4ea12e-4a24-3da1-b326-28279fc6287b" \
        --uuids "90bcaaa3-87fa-3e74-bb43-e84cae83eadc" \
        --uuids "1bf947c5-e969-323c-8da4-0b33247e735f" \
        --uuids "1a364a58-0a9e-3020-9f96-59daec6cc01a" \
        --uuids "64aafb24-953f-35e3-842b-03a15e8849b8" \
        --uuids "e5d06115-e733-36dc-bbe9-29432eeb77a5" \
        --uuids "ab074097-0ff0-3716-a377-a9bdb26c1008"



# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"


# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-states -v --nb-times 2560 --process "soma_base.gnu_m" --nb-items 50 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1702056042965447210\
        1702058405022656104


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-arrows -v --nb-times 2560 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1702056042965447210\
        1702058405022656104

# Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"


# Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-xy -v --nb-times 2560 --process "soma_base.gnu_m" --nb-items 50 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1702056042965447210\
        1702058405022656104