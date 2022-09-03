# QtVTKDICOMViewer
A minimal example of a DICOM viewer using VTK and Qt

## Use
Start by selecting the directory containing the DICOM files.

- The up/down keys can be used to scroll through the DICOM files.
- Zoom is done with the mouse wheel or right-mouse button plus mouse move.
- The brightness and contrast (window levels) can be changed with left-mouse button plus mouse move

It is based on the (https://vtk.org/doc/nightly/html/classvtkImageViewer2.html) class so some functionally from that class is also active.

## Dependencies
The program has been tested with PyQt5 and VTK9

## Known issues
The DICOM is read by the vtk DICOM reader that has known issues with compressed DICOM files. To make this viewer more robust, it should probably be based on PyDICOM. But the goal was to keep it as simple as possible.

## Author
Rasmus R. Paulsen. DTU Compute. 2022.

(Based on other example code)
