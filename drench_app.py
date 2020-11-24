import subprocess

#cmd = 'python -m drench ~/program_code/python_practice/ubuntu-ja-18.04.3-desktop-amd64.iso.torrent --directory ~/Downloads'
#subprocess.run(['python','-m','drench','~/program_code/python_practice/ubuntu-ja-18.04.3-desktop-amd64.iso.torrent','--directory','~/Downloads'])
def drench_subprocess(folder_path,file_path):
  subprocess.run(['python','-m','drench',file_path,'--directory',folder_path])

