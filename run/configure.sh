#!/bin/bash

pip show tqdm 1>/dev/null #pip for Python 2
if [ $? == 0 ]; then
    echo "tqdm already installed" #Replace with your actions
else

    echo "tqdm not found" #Replace with your actions, 'pip3 install --upgrade package_name' ?
    python -m pip install tqdm
fi

python ./run/service_configuration.pyc