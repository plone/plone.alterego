node {
    checkout scm

    stage('Build') {
        echo 'Building'
        sh 'virtualenv .'
        sh 'pip install setuptools==38.2.4 zc.buildout==2.10.0'
    }
    stage('Test') {
        echo 'Building....'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }
}
