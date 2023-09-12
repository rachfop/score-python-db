#!/bin/bash

curl https://api.humanitec.io/orgs/${HUMANITEC_ORG}/resources/defs \
  -H "Authorization: Bearer ${HUMANITEC_TOKEN}" \
  -H "Content-Type: application/json" \
  --data-binary '{
  "id": "static-mysql",
  "name": "Static MySQL",
  "type": "mysql",
  "driver_type": "humanitec/echo",
  "driver_inputs": {
    "values": {
      "name": "${DB_NAME}",
      "host": "${DB_HOST}",
      "port": 3306
    },
    "secret": {
      "username": "${DB_USERNAME}",
      "password": "${DB_PASSWORD}"
    }
  },
  "criteria": [
    {
      "app_id": "${HUMANITEC_APP_ID}",
      "env_id": "development"
    }
  ]
}'