alias python=python3
##
echo "creating virtual environment"
python3 -m venv venv
source venv/bin/activate
##
echo "upgrading pip to get rid of the annoying 'you should blabla'"
pip install --upgrade pip
##
##
echo "preparing for build"
python3 -m pip install --upgrade setuptools wheel
##
echo "prepare for upload"
python3 -m pip install --upgrade twine
pip3 install keyring
##
echo "building"
echo "=-=-=--=-==---=-=-=-=---=-=-=-=-=-=-=-"
rm -rf dist/*
python3 setup.py sdist bdist_wheel
rc=$?
if [ $rc -eq 0 ] ; then
   echo "Uploading to test.pypi.org..."
   python3 -m twine upload --sign --repository-url https://test.pypi.org/legacy/ dist/*
   rc=$?
fi
if [ $rc -eq 0 ] ; then
   echo "Updating version number for git..."
   if [ -f temp/_tmp_version.tmp ] ; then
      cp -p temp/_tmp_version.tmp plugins/__init__.py
      git add plugins/__init__.py
      git commit -m "$(cat plugins/__init__.py) now on test.pypi"
      #git push
   else
      echo "new version file not found. version number not changed in git."
   fi
else
   echo "Version not changed as upload was not successful."
fi

