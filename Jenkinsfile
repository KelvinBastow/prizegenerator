pipeline {
    agent any
    environment{
        DATABASE_URI
    }
    stages{
        stage('Test'){
            //run pytest
        }
        stage('Build'){
            sh 'docker-compose build'
        }
        stage('Push'){
            sh 'docker-compose push'

        }
        stage('Configure Swarm'){
            //run playbook define inventory
        }
        stage('Deploy'){
            // docker stack deploy ref compose file
        }
    }
}