#!/bin/bash
scp -i ~/.ssh/id_rsa docker-compose.yaml jenkins@deathstar-manager:/home/jenkins/docker-compose.yaml
ssh -i ~/.ssh/id_rsa jenkins@deathstar-manager << EOF
    export DATABASE_URI=${DATABASE_URI}
    docker stack deploy --compose-file /home/jenkins/docker-compose.yaml prizegenerator
EOF

# this allows the Main dev machine to pass the yaml file across to the manager node.