#!/bin/sh
IP="172.17.0.3"
PORT=8080

############################################## Resolution 1080p (1920x1080) ##############################################

# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/traces

# Create Experiment
# Experiment Name:cde21a0a-35cd-37d4-8fdc-d1ecad068f6b:[1702056042965447210,1702058405022656104]
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -v "Experiment Name" --trace-set-file "Open Trace.json"

# Get Output Descriptors
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-outputs -v cde21a0a-35cd-37d4-8fdc-d1ecad068f6b


# Get TimeGraph Tree: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-timegraph-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"


# Get TimeGraph States: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-states -v --nb-times 1920 --tree "Get Timegraph Tree.json" --process "soma_base.gnu_m" --nb-items 40 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider"\
        1702056042987417600\
        1702056602949809200


# Get TimeGraph Arrows: Thread Status Provider (org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-timegraph-arrows -v --nb-times 1920 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.internal.analysis.os.linux.core.threadstatus.ThreadStatusDataProvider" \
        1702056042987417600\
        1702056602949809200

# Get XY Tree - CPU Usage (org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    get-xy-tree -v "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider"


# Get XY: CPU Usage (org.eclispe.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider)
trace-coordinator benchmark -d --ip $IP -p $PORT \
    concrete-get-xy -v --nb-times 1920 --tree "Get XY Tree.json" --process "soma_base.gnu_m" --nb-items 40 \
        "cde21a0a-35cd-37d4-8fdc-d1ecad068f6b" \
        "org.eclipse.tracecompass.analysis.os.linux.core.cpuusage.CpuUsageDataProvider" \
        1702056042987417600\
        1702056602949809200
