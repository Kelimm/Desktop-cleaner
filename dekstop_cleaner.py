import os
import shutil
from tkinter import Tk, Label, Button


class DesktopCleanerApp:
  def __init__(self):
    self.root = Tk()
    self.root.title('Desktop Cleaner')
    self.root.geometry('400x200')
    self.root.resizable(False, False)
    
    self.label = Label(self.root, text='Click on the button to clean your desktop', font=('Helvetica', 12, 'bold'))
    self.label.pack()
    
    self.button = Button(self.root, text='Clean Desktop', command=self.run_commands, bg='gray', fg='white', font=('Helvetica', 12, 'bold'))
    self.button.pack(pady=20)

    
    
    
    self.root.mainloop()
    
  def run_commands(self):
      self.clean_desktop()
      self.update_status()
      self.root.after(4000, self.close_app)

  def update_status(self):
    self.label = Label(self.root, text='Desktop Cleaned Successfully', font=('Helvetica', 12, 'bold'))
    self.label.pack()
    
  def close_app(self):
    self.root.destroy()
    
  def clean_desktop(self):
    desktop_path = os.path.join(os.path.expanduser("~"), 'Desktop')

    extension_list = {
      'txt': 'TextFiles',
      'pdf': 'PDF',
      'jpg': 'Images',
      'jpeg': 'Images',
      'png': 'Images',
      'docx': 'Documents',
      'xlsx': 'Excel',
      'zip': 'ZIP',
      'jar': 'java',
      'exe': 'Executable',
      'lnk': 'Shortcuts',
      'log': 'TextFiles'
    }

    for folder in extension_list.values():
      folder_path = os.path.join(desktop_path,folder)
      if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    files = os.listdir(desktop_path)

    for file in files:
        file_path = os.path.join(desktop_path, file)
        
        if os.path.isdir(file_path):
          continue 
        
        file_extension = file.split('.')[-1].lower()
        
        if file_extension in extension_list : 
          destination_folder = extension_list[file_extension]
          destination_path = os.path.join(desktop_path, destination_folder)
          shutil.move(file_path, destination_path)
          print(f"Déplacé : {file} -> {destination_folder}")

if __name__ == '__main__':
    app = DesktopCleanerApp()
    app.root.mainloop()
