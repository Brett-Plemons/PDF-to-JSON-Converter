# Calculating TM and dilution volume for primers

**Name:** Brett Plemons 
<br/>
**Semester:** Spring 2019
<br/>
**Project Area:** Molecular Biology

## Objective
Write a python script that will scrape a primer sheet from companies like IDT
and calculate the TM temperature for the forward and reverse primer, and the dilution volume and return it to the user.

## Outcomes
This script should produce an easy to read output(.pdf, .txt) for the user to quickly know how much water to add to dilute their primers,
and what TM temperature to use when doing PCR.

##Rationale
The TM can be calculated as a function of the nucleotide sequence used in the primer, the dilution volume is a function of the
concentration of the pellet used in the primer in ng/&#956;L.

My lab, like many other labs, is constantly receiving new primers specific to each project. Each set of primers typically will have its own
dilution volume, and TM value which are both crucial to accurate results when performing PCR. In order to save time, and commit 
consistency to my lab, I will create a script which will provide the TM values, and dilution volume for primers based on the label paperwork
provided by the manufacturer.

## Diagram
<img src="https://github.com/KaynRyu/semesterProject/blob/Supplementary/semesterproject.jpg">
