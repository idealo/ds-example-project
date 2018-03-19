pipeline {
    agent {
        node {label 'python'}
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'conda env create -n myapp -f src/python/project/environment.yml'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                source activate myapp
                nosetests -vs src/python/tests/
                '''
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'oc start-build ds-example-project'
            }
        }
    }

}