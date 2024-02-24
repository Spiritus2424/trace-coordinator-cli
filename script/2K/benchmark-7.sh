#!/bin/sh
IP="172.17.0.2"
PORT=8080

############################################## Resolution QHD (2560x1440) ##############################################

# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" \
        --uuids "c39b083a-e15a-3fcb-b53d-8a1fd3ca07d0" \
        --uuids "f6894aaa-d860-30a7-be28-6d57b6bd6a28" \
        --uuids "b0e5cf1e-532a-3919-888c-c3533a70230d" \
        --uuids "0d6a8f97-2244-3317-b855-72a9aa1762f2" \
        --uuids "fcdb26d5-ad68-3a1d-aba6-a4c0666839ca" \
        --uuids "590be2df-5350-3df6-910c-0170b67df5f5" \
        --uuids "69f71e05-7539-366c-9b26-3e37ba67dbb9" \
        --uuids "8b7c6041-247f-3b4b-9be3-cafd989b7e1b" \
        --uuids "56c0afe7-c1f7-3cbd-882e-c5496a16e7ce" \
        --uuids "6eb1fdd5-9632-364a-92db-dc6bcd6ef29e" \
        --uuids "9fcaa9bb-8bbb-32a6-ab16-6a559048c033" \
        --uuids "e675df37-e253-36eb-8172-a58d36453fe3" \
        --uuids "1542a5aa-296e-3dd4-8fb8-bc39a1a90e59" \
        --uuids "6f1dde8e-6f39-3d3d-a511-8ae087e8990d" \
        --uuids "67c7d984-f9ab-3981-acbc-b7b37d7a6046" \
        --uuids "c2698e55-400d-356c-854b-22cb44a1d047" \
        --uuids "3c9c24b7-9469-3ab3-bdb2-b4c63948ab60" \
        --uuids "00fa0373-4531-371b-8ca2-a01bf6ad7514" \
        --uuids "d2c9aae8-a955-339f-aef9-f7ff82dfb0ef" \
        --uuids "cc3abd38-0d9c-3356-9462-2ea533911852"



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