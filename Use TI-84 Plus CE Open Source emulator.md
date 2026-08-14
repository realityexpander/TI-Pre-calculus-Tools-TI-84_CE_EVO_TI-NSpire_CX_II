### Use TI-84 Plus CE Open Source emulator (TI-SmartView is discontinued as of Oct 2026)
  - You will need to copy the ROM from your calculator to your computer to run the emulator on your computer.
    - There are 1 or 2 programs you will need to download to the calculator to make this work.
  1. Download the "CE-EMU" Application (A free TI-84 Emulator program for Mac/Win/Linux)
     - [https://github.com/CE-Programming/CEmu](https://github.com/CE-Programming/CEmu/releases)
     - Install the program on your computer using the correct installer (Mac, Win, Linux)
  3. Launch "CE-EMU" and run the "ROM setup wizard..."
     - (it should pop up automatically upon first launch of app.)
     - click the "Save Program" button and name the file "ROMDUMP", save it to your computer. This will be transferred to your physical calculator to extract the the ROM files from your physical calculator.
     
      <img width="238" alt="Screenshot 2026-08-01 at 12 30 40 PM" src="https://github.com/user-attachments/assets/00dcc709-b3b9-426d-9c7e-e2a73d8610d1" />
    
  4. Transfer the "ROMDUMP.8xp" to your physical calculator using "TI-Connect CE".
  5. Check your OS version number on your physical calculator.
     -   [2nd]  →  [mem/+]  →  [1.About] [ENTER] 
  6. If your physical calculator has OS 5.3 to 5.8.4, you will need to download and transfer the "Artifice" jailbreak program to physical calculator using TI-Connect CE. This program allows your calculator to run old assembly programs on your TI-84 Plus CE physical calculator.

     - https://yvantt.github.io/arTIfiCE/

     <img width="212" alt="image" src="https://github.com/user-attachments/assets/c9838fb4-80b1-439f-9c52-9552014e2524" />

  7. Run the TI-BASIC "ROMDUMP" program to extract the ROM image from the physical calculator.

     - If OS>=5.3,
       - You will need to run the "Artifice" jailbreak program for this more recent OS.
       - This program lets you run old Assembly programs, like "ROMDUMP".
       - The Artifice program is called "A".
       - 7a.

         [prgm] → [TI-Basic] → A → prgmA → ROMDUMP [ENTER] 

     - If OS<5.3,
       - On your physical calculator, Run the "ROMDUMP" program
       - 7b.

         [prgm] → [TI-Basic] → ROMDUMP [ENTER] 
  
      - This will save a copy of the ROM into the calculator main memory as a series of files (ROMData segments of 64k binary ROM info.)
  8. Using "TI-Connect CE", copy all the "ROMData#" (Where # is a letter from A to Z) segments from the physical calculator to your computer.
  
       - <img width="398" alt="image" src="https://github.com/user-attachments/assets/33d1f51e-70c6-48b4-beee-bcc25c01c067" />
  9. Drag and Drop all these "ROMData#" files from your computer to the "Drop ROM Segments Here" target.

       - <img width="238" alt="image" src="https://github.com/user-attachments/assets/8de3576e-dcbd-49a4-ab07-7cc7484e3426" />
  11. The "CE-EMU" program will then boot up the calculator with the ROMDUMP data and show the calculator startup screen.
  12. Transfer programs
     -  You may now drag and drop files to the "CE-EMU" calculator window to load, run and edit programs.
      
        <img width="452" alt="image" src="https://github.com/user-attachments/assets/6aab6d69-8a84-48f2-8f79-824ff8a5c63d" />

        <img width="452" alt="image" src="https://github.com/user-attachments/assets/d7cce519-f066-415f-82ce-a9b4b6afa29a" />
