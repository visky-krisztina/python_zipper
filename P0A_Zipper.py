import FreeSimpleGUI as sg
import zipfile, pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for file in filepaths:
            file = pathlib.Path(file)
            archive.write(file, arcname=file.name)

label1 = sg.Text("Select files to compress: ")
input2 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination of the zipped file: ")
input1 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose",  key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text("", key='output')

window = sg.Window("Files Zipper",
                   layout=[
                       [label1, input1, choose_button1],
                       [label2, input2, choose_button2],
                       [compress_button, output_label]
                   ])

while True:
    event, values = window.read()
    file_paths = values["files"].split(";")
    folder_paths = values["folder"]
    make_archive(file_paths, folder_paths)
    window['output'].update(value="Compression completed!")

window.close()