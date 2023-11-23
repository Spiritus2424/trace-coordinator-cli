#!/bin/sh
IP="172.17.0.1"
PORT=8080
# Open Traces
trace-coordinator benchmark -d --ip $IP -p $PORT \
    open-trace -v --max-depth=1 /home/spiritus/ws/trace-coordinator/traces/hpc-soma-50000-test

# Create Experiment
trace-coordinator benchmark -d --ip $IP -p $PORT \
    create-experiment -d  "Experiment Name" \
        --uuids "68c43d1c-1880-39e0-bc9e-ad00621c0785"\
        --uuids "3044f59d-d89e-33c8-8a3d-211f11c63d57"\
        --uuids "c28df1fc-ce8d-3edd-9328-a0d808c243a1"\
        --uuids "d5036461-85b9-352c-8abc-ea74772f46a8"\
        --uuids "30d78cdd-69cd-32df-be2d-41f2d3137e41"\
        --uuids "4c8970c4-20c6-3242-b85d-77c7dc9ad342"\
        --uuids "a3849d88-aa02-3f16-8786-f5f1d62faa16"\
        --uuids "b5fced73-e7f2-3b5a-b103-3e4c917e2420"\
        --uuids "e8a5e1e5-bc29-3142-932c-7e0a15295b88"\
        --uuids "6a084b3c-17bf-3839-ab90-66967521bdc0"\
        --uuids "b76826c4-a33d-3cba-b8de-02f2f726f2c7"\
        --uuids "e72f0761-dc49-3706-a84a-715595f9b9f1"\
        --uuids "c057c1a5-7f78-3934-9d76-a12cb2776628"\
        --uuids "31ee5a6d-758b-3620-8279-be35f67f41ee"\
        --uuids "b82303ec-803c-36ed-a59d-8a492e499044"\
        --uuids "5dc005e1-549c-3c41-85d2-6d205575e0d3"\
        --uuids "e369e8a0-dd43-3754-a065-d4c91be72fd2"\
        --uuids "277acdbe-fbff-3777-852a-bd3f30f35f26"\
        --uuids "29c1940b-4c34-3d3b-b3da-f70d4eb8e7ea"\
        --uuids "2076f5cf-f32f-3a30-84b8-d1960522385d"\
        --uuids "6386d4fe-a58c-340e-8928-4078fb734046"\
        --uuids "d987b9d3-e75c-3ee8-ba45-e7510fe3730f"

# Get Output Descriptors
# trace-coordinator benchmark -d --ip $IP -p $PORT \
#     get-outputs -v 

