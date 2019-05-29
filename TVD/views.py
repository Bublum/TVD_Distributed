import os
import zipfile

import io
from django.http import HttpResponse

from django.shortcuts import render


def requirements(request):
    filenames = ["/home/shibashis/decryptor.py", "/home/shibashis/decryptor.py"]

    zip_subdir = "requirements"
    zip_filename = zip_subdir + ".zip"

    s = io.StringIO()

    zf = zipfile.ZipFile(s, "w")

    for fpath in filenames:
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), mimetype="application/x-zip-compressed")
    # ..and correct content-disposition
    resp['Content-Disposition'] = 'attachment; filename=' + zip_filename

    return resp
