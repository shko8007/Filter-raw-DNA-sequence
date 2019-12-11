# Filter-raw-DNA-sequence
Using python, I made a code enabling to remove longer or shorter DNA sequence than target length

To acquire meaningful DNA sequence, several analysis steps are required. After DNA library preparation (especially PCR), off-target products are contained in the sample, and these off-target products are larger or smaller than target product. Sequencing machine sequences all of molecules, so filtering off-target product in bioinformatic process is essential and beginning step.

In this project, I made a code enabling to remove off-target product (large or small amplicon) using python. I confirmed that the developed code can filter off-target product successfully by using raw sequencing data of Pacbio sequencing method. Target DNA size is ~ 2.7 kb, so I removed larger or smaller DNA than 3 kb or 2.5 kb, respectively. 

This python course is basic course for entry level of programming. I learned many new knowledge related to python, such as various commands, merit of python compared to other bioinformatic tool, and how to apply python to my current research. Although this code made through this project is very simple and not nice, it is enough to resolve current task. That means, if someone have basic knowledge and a few experiences through this course, I believe that anyone can do like that.   
