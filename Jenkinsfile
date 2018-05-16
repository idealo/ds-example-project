pipeline {
    agent {
        node {label 'python'}
    }

    triggers {
        pollSCM('')
    }

    environment {
        APPLICATION_NAME = 'ds-example-project'
    }

    stages {
        stage('Build Testing') {
            steps {
                echo 'Building..'
                sh 'conda env create -n myapp -f src/python/project/environment.yml'
            }
        }
        stage('Test Application') {
            steps {
                echo 'Testing..'
                sh '''
                source activate myapp
                nosetests -vs src/python/tests/
                '''
            }
        }
        stage('Build Application') {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
                            openshiftBuild(buildConfig: '${APPLICATION_NAME}', showBuildLogs: 'true')
                        }
                    }
                }
            }
        }
        stage('Deploy Application') {
            steps {
                script {
                    openshift.withCluster() {
                        openshift.withProject() {
                            openshiftDeploy(deploymentConfig: '${APPLICATION_NAME}')
                        }
                    }
                }
            }
        }
    }
}
