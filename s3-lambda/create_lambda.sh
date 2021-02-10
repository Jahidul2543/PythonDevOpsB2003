#!/bin/bash
EnvironmentVariables = "{EMAIL_LIST=kabir.cse10@gmail.com,sowmen2016@gmail.com}"
aws lambda update-function-configuration --function-name get-demo-b2003-izaanit-bucket-new-object-name \
    --environment Variables=$EnvironmentVariables