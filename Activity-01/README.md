1. Step 1: Generate a test folder structure

   ```bash
   python setup_files.py

2. Step 2: Recursive scanner script

    ```bash
    python scan.py test_root

3. Enhancement Options
    I chose Group files by folder summary. I edited my scan.py code for this to happen. 

4. OUTPUT

    Scanning: C:\Users\User1\Downloads\IT390R\activities-juliandallin\Activity-01\test_root
    Found 20 text files

    File                                      Size (KB)
    ----------------------------------------------------
    docs\file0.txt                                  0.1
    docs\file1.txt                                  0.1
    docs\file2.txt                                  0.1
    docs\file3.txt                                  0.1
    docs\file4.txt                                  0.1
    logs\file0.txt                                  0.1
    logs\file1.txt                                  0.1
    logs\file2.txt                                  0.1
    logs\file3.txt                                  0.1
    logs\file4.txt                                  0.1
    docs\subfolder\file0.txt                        0.1
    docs\subfolder\file1.txt                        0.1
    docs\subfolder\file2.txt                        0.1
    docs\subfolder\file3.txt                        0.1
    docs\subfolder\file4.txt                        0.1
    logs\archive\file0.txt                          0.1
    logs\archive\file1.txt                          0.1
    logs\archive\file2.txt                          0.1
    logs\archive\file3.txt                          0.1
    logs\archive\file4.txt                          0.1
    ----------------------------------------------------
    Total size: 2.0 KB

    📂 Folder Summary:
    docs/ — 5 file(s), 0.5 KB
    logs/ — 5 file(s), 0.5 KB
    docs\subfolder/ — 5 file(s), 0.5 KB
    logs\archive/ — 5 file(s), 0.5 KB