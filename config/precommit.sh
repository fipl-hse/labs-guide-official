set -ex

source venv/bin/activate
export PYTHONPATH=$(pwd):${PYTHONPATH}

python -m black .

python -m pyspelling -c config/spellcheck/.spellcheck.yaml -v

python config/static_checks/check_doc8.py

python config/static_checks/requirements_check.py

python config/static_checks/newline_check.py

python admin_utils/converter.py
