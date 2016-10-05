"""
Receive Quay.io webhook
and deploy server 
"""

def post(req, api):
    """
    Input:
        docker_tags
    """

    print(req.params['docker_tags'])