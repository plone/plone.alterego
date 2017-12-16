node {
    checkout scm

    stage('Build') {
        echo 'Building'
        sh 'virtualenv . && . bin/activate && pip install setuptools==38.2.4 zc.buildout==2.10.0'
        sh 'wget https://raw.githubusercontent.com/plone/buildout.coredev/5.2/experimental/qa.cfg'
        sh 'sed -i "s#directory = src#directory = plone#" qa.cfg'
        sh 'bin/buildout -c qa.cfg'
    }
    stage('Test') {
        sh 'bin/code-analysis'
    }
    stage('Deploy') {
        echo 'Deploying....'
    }
}
