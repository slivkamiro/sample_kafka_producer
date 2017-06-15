#!/bin/bash

token=`curl -XPOST -s -d "grant_type=password&client_id=insightapp&username=admin&password=admin123" http://localhost/auth/oauth2.0/accessToken | sed -r 's/.*\"access_token\":\"([^\"]+)\".*/\1/'`

#Create topic
curl -XPUT -H "Authorization: Bearer $token" -H "Content-Type: application/json" http://localhost/api/kafka-topic/workshop
echo ""
curl -XPOST -H "Content-Type: application/vnd.schemaregistry.v1+json" http://localhost:8989/subjects/workshop-value/versions --data @workshop.avsc.json
echo ""
