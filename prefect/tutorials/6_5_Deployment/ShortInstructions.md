# Brief Instructions

- Create file:      
    depMeta2.py
- Run file
    python depMeta2
- Run Prefect Orion Server: 
    prefect orion start
- Run Build:        
    prefect deployment build ./depMeta2:log_flow2 -n log-simple2 -q test2
- Configure:        
    In log_flow-deployment change "parameters: {}" to "parameters: {'name':'Marvin'}"
- Apply Deployment: 
    prefect deployment apply log_flow-deployment.yaml
- Demonstrate deployment exists: 
    prefect deployment ls
- INspect new deployment: 
    prefect deployment inspect log-flow/log-simple
- Run Orion with the new queue:
     prefect agent start -q test