node {
    stage('Get Project') {
        echo "checkout from git"
        git credentialsId: '0e624d02-d940-4edb-8b3f-3d939f7a0185', url: 'https://github.com/janeyzhou/JenkinsHomework.git'

        sh "ls"
    }
    stage('Test') {
        sh "pwd"
        sh "pytest TestSuite/Test_Amazon.py"
    }
}