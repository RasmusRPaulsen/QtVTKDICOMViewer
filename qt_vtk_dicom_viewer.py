import sys
import vtk
from PyQt5 import QtCore, QtWidgets
from PyQt5 import QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor


class MainWindow(QtWidgets.QMainWindow):
    def keypress_callback(self, obj, ev):
        key = obj.GetKeySym()
        if key == 'Up':
            cur_slice = self.image_viewer.GetSlice()
            if cur_slice < self.image_viewer.GetSliceMax():
                self.image_viewer.SetSlice(cur_slice + 1)
        if key == 'Down':
            cur_slice = self.image_viewer.GetSlice()
            if cur_slice > self.image_viewer.GetSliceMin():
                self.image_viewer.SetSlice(cur_slice - 1)

        msg = f"{self.image_viewer.GetSlice()} / {self.image_viewer.GetSliceMax()}"
        self.slice_text_mapper.SetInput(msg)
        self.image_viewer.Render()

    def __init__(self, parent = None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.frame = QtWidgets.QFrame()
        self.vl = QtWidgets.QVBoxLayout()
        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl.addWidget(self.vtkWidget)
        self.image_viewer = None
        self.slice_text_mapper = None
        self.setup_screen_things()

        self.frame.setLayout(self.vl)
        self.setCentralWidget(self.frame)
        self.show()
        self.iren.Initialize()

    def setup_screen_things(self):
        print("setting up screen things")
        print("Reading DICOM")
        folder = 'C:/data/Abdominal/CTLymphNodes/manifest-IVhUf5Gd7581798897432071977/CT Lymph Nodes/ABD_LYMPH_001/09-14-2014-ABDLYMPH001-abdominallymphnodes-30274/abdominallymphnodes-26828/'
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(folder)
        reader.Update()
        print("Reading done")

        self.image_viewer = vtk.vtkImageViewer2()
        self.image_viewer.SetInputConnection(reader.GetOutputPort())
        self.ren_win = self.vtkWidget.GetRenderWindow()
        self.ren_win.AddRenderer(self.image_viewer.GetRenderer())
        self.image_viewer.SetRenderWindow(self.ren_win)
        self.iren = self.image_viewer.GetRenderWindow().GetInteractor()
        self.style = vtk.vtkInteractorStyleImage()
        self.iren.SetInteractorStyle(self.style)
        self.iren.AddObserver('KeyPressEvent', self.keypress_callback, 1.0)

        slice_text_prop = vtk.vtkTextProperty()
        slice_text_prop.SetFontFamilyToCourier()
        slice_text_prop.SetFontSize(20)
        slice_text_prop.SetVerticalJustificationToBottom()
        slice_text_prop.SetJustificationToLeft()

        self.slice_text_mapper = vtk.vtkTextMapper()
        msg = f"{self.image_viewer.GetSlice()} / {self.image_viewer.GetSliceMax()}"
        self.slice_text_mapper.SetInput(msg)
        self.slice_text_mapper.SetInput(msg)
        self.slice_text_mapper.SetTextProperty(slice_text_prop)

        slice_text_actor = vtk.vtkActor2D()
        slice_text_actor.SetMapper(self.slice_text_mapper)
        slice_text_actor.SetPosition(15, 10)

        self.image_viewer.GetRenderer().AddActor2D(slice_text_actor)
        self.image_viewer.GetRenderer().ResetCamera()
        self.image_viewer.Render()


def run_qt_window():
    app = QtWidgets.QApplication(sys.argv)

    folder = 'C:/data/Abdominal/CTLymphNodes/manifest-IVhUf5Gd7581798897432071977/CT Lymph Nodes/ABD_LYMPH_001/09-14-2014-ABDLYMPH001-abdominallymphnodes-30274/abdominallymphnodes-26828/'

    use_file_dialog = False
    if use_file_dialog:
        filedialog = QtWidgets.QFileDialog()
        filedialog.setNameFilter("All files (*.*)")
        filedialog.setAcceptMode(QtWidgets.QFileDialog.AcceptOpen)
        filedialog.setFileMode(QtWidgets.QFileDialog.Directory)
        folder = filedialog.exec()


    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_qt_window()
