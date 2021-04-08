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
            sh 'ansible-playbook playbook-1.yaml'
        
        }
        stage('Deploy'){
            sh 'docker stack deploy --compose-file docker-compose.yaml prizegenerator'
            sh 'docker stack services'
        }
    }
}