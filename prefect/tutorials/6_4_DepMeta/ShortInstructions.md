# Brief Instructions

- Create file:      
    2_DeploymentMeta.py
- Run Prefect Orion Server in terminal 2: 
    prefect orion start
- Run Build:        
    prefect deployment build ./2_DepMeta.py:log_flow -n log-simple -q test
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