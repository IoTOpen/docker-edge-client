. config.sh

function remove_nasty_chars() {
  tr -d -c 'a-zA-Z0-9:_\-+\.@'
}

function verify_header() {
  TOKEN=$(echo "${QUERY_STRING}" | sed -ne 's/.*access-token=\(.[^; ]*\).*/\1/p' | remove_nasty_chars)

  if [ -z "${TOKEN}" ]; then
    TOKEN=$(echo "${HTTP_COOKIE}" | sed -ne 's/.*access-token=\(.[^; ]*\).*/\1/p')
  else
    echo Set-Cookie: access-token="${TOKEN}"
  fi

  USERNAME=token
  USER=$(curl -s "${BASE}/api/v2/user/me" -X GET -u "${USERNAME}:${TOKEN}" -H "Accept: application/json" | jq -r .email)

  if [ "${USER}" == "null" ] || [ "${USER}" == "" ]; then
    echo -e "\nACCESS VIOLATION"
    exit
  fi
}

if [ "${INSECURE}" != "true" ]; then
  if [ -z "${BASE}" ]; then
    echo -e "\n AUTHENTICATION ACTIVE, BUT BASE IS MISSING"
    exit
  fi
  verify_header
else
  USER=anonymous
fi

page=$0

sed "s/__USER__/${USER}/" header.inc | sed "s/__${page}__/text-decoration-underline/" | sed "s/__.*__//g"
