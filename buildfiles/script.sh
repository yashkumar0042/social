#!/bin/bash

function init(){

	echo "********************************************************"
	echo "********************************************************"
	echo "Environments set
		BUILD_ID:      : $BUILD_ID
		REVISION_ID:   : $REVISION_ID
		BRANCH_NAME:   : $BRANCH_NAME
		SHORT_SHA:     : $SHORT_SHA
		TAG_NAME:      : $TAG_NAME
		REPO_NAME:     : $REPO_NAME
		File:          : $File
		PROJECT_ID     : ${APP_PROJECT_ID:-dummy value}
		APP_ENV        : $app_env
		SHORT_LOCATION : $short_location
		COMMIT_SHA     : $COMMIT_SHA
		_PR_NUMBER     : $_PR_NUMBER
		_HEAD_REPO_URL : $_HEAD_REPO_URL
		_HEAD_BRANCH   : $_HEAD_BRANCH
		_BASE_BRANCH   : $_BASE_BRANCH"

	echo "********************************************************"
	echo "********************************************************"

}

init