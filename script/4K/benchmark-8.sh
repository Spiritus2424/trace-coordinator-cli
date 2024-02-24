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
        --uuids "23ae7d84-9cb8-3c53-b7c0-3f8f30b4e75c" \
        --uuids "5a2ffe62-2bf3-3984-8315-2f4f604e96ad" \
        --uuids "a09be660-9ab6-346b-a228-2631d31195a3" \
        --uuids "88ac4c54-4c03-3cf7-ae46-9eb00546a5b4" \
        --uuids "1d552d98-9cec-3f8c-912e-a01e04898568" \
        --uuids "5ed6458b-9610-3611-a6d8-56cb125916f8" \
        --uuids "fb791458-2cb6-38d3-8566-94723b0216df" \
        --uuids "8c71506c-3080-393d-a6ef-8357ab71f132" \
        --uuids "ea89832d-ff75-3eb1-8efe-1620c478ed2a" \
        --uuids "2443364a-5efc-31aa-a77e-d113beb7da9d" \
        --uuids "1179293d-ff6d-3ffc-8b41-d4a3e51feedc" \
        --uuids "c7bbc3a5-7914-3a6f-bded-ebce64b6ceb7" \
        --uuids "55d3618a-7b8b-3537-b8e5-b1660d6a6d50" \
        --uuids "80efee23-69ca-3ee6-bf47-f131ac7e9a5d" \
        --uuids "a01a8398-1734-3a25-8890-96c1921dd865" \
        --uuids "a1c50731-fbde-3d76-8e6b-dec6bc8a2241" \
        --uuids "d7fd12d8-f4d9-37bc-b026-f6a38afff1fe" \
        --uuids "06268125-9d28-31d5-ab7b-428aa26cab5d" \
        --uuids "bbcb1af4-9830-3950-94a2-6e0a3dcf2200" \
        --uuids "b0ee60fe-ca5b-31dd-a246-d86703779c2a"



# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"


# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-states -v --nb-times 3840 --process "soma_base.gnu_m" --nb-items 60 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1702056042965447210\
        1702058405022656104


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-arrows -v --nb-times 3840 \
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
    concrete-get-xy -v --nb-times 3840 --process "soma_base.gnu_m" --nb-items 60 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1702056042965447210\
        1702058405022656104
