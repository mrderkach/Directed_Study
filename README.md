# Directed_Study
Detecting Textual Entailments in Biochemical Articles using EDITS and Transfer Learning

For tips on how to install and run EDITS, please refer to TipsForReproducingResults.md

*Original datasets*

https://github.com/facebookresearch/SentEval

*Debatepedia datasets*

http://www-sop.inria.fr/NoDE/NoDE-xml.html

*Edits 2.1*

https://github.com/hltfbk/EOP-1.2.3/wiki/EditDistance

*Edits 3*

https://github.com/kouylekov/edits

*Edits Sourceforge*

https://sourceforge.net/projects/edits/

**Reports explanation**
* SICK_report1 - Sick test trained on Sick train, where entailments are: Entailment, Nonentailment, Contradiction
* SICK_report2 - Sick test trained on Sick train, where entailments are: Entailment, Nonentailment
* SICK_report3 - Full Sick trained on Snli train
* SNLI_report1 - Snli test trained on Snli train
* Debatepedia_report1 - Debatepedia test trained on (Debatepedia train | Snli train - same result)
* Debatepedia_report2 - Debatepedia test trained on (Debatepedia train | Snli train - same result) - each pair has only 1 sentence in text and hypothesis 
* Debatepedia_report3 - Debatepedia test with sentences joined via "and", punctuation removed trained on Snli train


