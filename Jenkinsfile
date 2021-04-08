pipeline {
    agent any
    environment{
        DATABASE_URI
    }
    stages{
        stage('Test'){
            sh 'testing.sh'
            
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
        }
        stage('Deploy'){
            sh 'docker stack deploy --compose-file docker-compose.yaml'
            sh 'docker stack services'
        }
    }
}