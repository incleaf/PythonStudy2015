# 03-package.py

# way 1
import pkg.sound.echo
pkg.sound.echo.echo_test()

# way 2
from pkg.sound import echo
echo.echo_test()

# way 3
from pkg.sound.echo import echo_test
echo_test()

# impossible

# import pkg
# pkg.sound.echo.echo_test()

# import pkg.sound.echo.echo_test

# way 4
from pkg.sound import *
echo.echo_test() # __init__.py에 __all__ =['echo']로 변수 선언을 해야 한다.