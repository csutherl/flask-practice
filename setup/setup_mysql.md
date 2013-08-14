In order to use the sqlalchemy connector you have to have the mysql-python library installed.

Before I could pip install it, I had to install the mysql and mysql-devel packages for Linux. See steps below:

yum install mysql mysql-devel
pip install mysql-python

You're done!