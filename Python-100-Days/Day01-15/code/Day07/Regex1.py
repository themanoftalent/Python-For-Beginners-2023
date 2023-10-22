#  !/usr/bin/python
#  Copyright (c) akifciftci 2020. Aim to help new beginner to try hard and learn more.
#
#

import re


tekx='''Abstract: - One of the critical physical ailments in recent years is lung cancer.
 Basically, it is caused by the initiation of rampant malignant abnormal cells grown in
  either both lungs or in one of them. The fatality rate that happens due to lung cancer 
  s highest and is considered the leading cause of mortality out of all types of cancers. 
  t is crucial to identify the ailment at the initial stage of the numerous types of 
  cancer as it critical, to provide a higher survival rate for cancer sufferers. Hence, 
  it is imperative for innovative techniques to be constructed. There were numerous soft 
  computation methods utilized recently to identify the cancerous cells derived from 
  medical image to provide an uncomplicated design, with minimal cost, no time consuming,
   and lastly offer positive outcomes to patients, specifically for patients in remote 
   locations, with ordinary doctors (not specialist) to execute amazing activities to 
   diagnose ailments. The current research introduces and compare between various review 
   techniques and methods to categorize and diagnose pulmonary cancer ailments.'''


print(re.findall('met+...',tekx))
