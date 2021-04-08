pipeline {
    agent any
    environment{
        DATABASE_URI = credentials('DATABASE_URI')

    }
    stages{
        stage('Test'){
            sh 'bash/prizegenerator/testing.sh'
            
        }
        stage('Build'){
            sh 'docker-compose build'
            sh 'docker-compose up -d'
        }
        stage('Push'){
            sh 'docker ps && docker images'
            sh 'docker-compose push'

        }
        stage('Configure Swarm'){
            //run playbook define inventory
            sh 'ansible-playbook -i inventory.yaml playbook-1.yaml'
        
        }
        stage('Deploy'){
            sh 'docker stack deploy --compose-file docker-compose.yaml prizegenerator'
            sh 'docker stack services'
        }
        stage('NGINX'){
            sh 'cd ansible && ansible-playbook -i inventory.yaml playbook.yaml'
        }
    }
}