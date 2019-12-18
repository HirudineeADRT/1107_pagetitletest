let AWS = require('aws-sdk');
const cognito_idp = new AWS.CognitoIdentityServiceProvider();

exports.handler = async (event) => {
    cognito_idp.listUsers({
        UserPoolId: process.env.UserPoolId_cognitolkjhg,
        Limit: 10
    }).promise()
        .then(data => {
            // your code goes here
        })
        .catch(err => {
            // error handling goes here 
        });

    return { "message": "Successfully execu ted" };
};