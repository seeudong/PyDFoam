#!/usr/bin/env python3

from PyFoam.ThirdParty.six import print_

try:
    try:
        import PyQt5
    except ImportError:
        import PyQt4
    from PyFoam.Applications.DisplayBlockMeshQt import DisplayBlockMesh
except ImportError as e:
    try:
        from PyFoam.Error import warning
        warning("Falling back to the old Tkinter-implementation because no PyQT4 was found")
        from PyFoam.Applications.DisplayBlockMesh import DisplayBlockMesh
    except ImportError:
        print_("Seems like PyFoam is not in the PYTHONPATH")
        import sys
        sys.exit(-1)

DisplayBlockMesh()

# Should work with Python3 and Python2
