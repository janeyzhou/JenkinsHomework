node {
    stage('Get Project') {
        echo "checkout from git"
        git credentialsId: 'c34a11a4-8ef2-4b6a-be17-c0c4f2e01216', url: 'https://github.com/janeyzhou/JenkinsHomework.git'

        sh "ls"
    }
    stage('Test') {
        sh "sh comparecontent/greeting.sh"
	sh "diff comparecontent/greeting.txt comparecontent/testgreeting.txt"
		
    }
}
