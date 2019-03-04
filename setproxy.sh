echo $1
if [ "$1" == "on" ]; then
    export HTTP_PROXY=http://gatekeeper.mitre.org:80
    export HTTPS_PROXY=http://gatekeeper.mitre.org:80
    export NO_PROXY=localhost,127.0.0.1,.mitre.org
    export http_proxy=$HTTP_PROXY
    export https_proxy=$HTTPS_PROXY
    export no_proxy=$NO_PROXY
else
    unset HTTP_PROXY
    unset HTTPS_PROXY
    unset NO_PROXY
    unset http_proxy
    unset https_proxy
    unset no_proxy
fi

echo $HTTP_PROXY
echo $HTTPS_PROXY
echo $NO_PROXY
echo $http_proxy
echo $https_proxy
echo $no_proxy