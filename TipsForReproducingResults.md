# How to run EDITS

1. Go to folder:
cd  ~/Excitement-Open-Platform-1.2.3/target/EOP-1.2.3/
2. Clear the folder where the model will be located
rm /tmp/EN/dev/*
3. Train the model
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -config ./eop-resources-1.2.3/configuration-files/EditDistanceEDA_EN.xml -train -trainFile ../../../SICK/SICK_train.xml
Here we have to pay attention on path to train file and path to config
4. Test the model
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -config ./eop-resources-1.2.3/configuration-files/EditDistanceEDA_EN.xml -test -testFile ../../../SICK/SICK_test.xml -output ./eop-resources-1.2.3/results/
Again, pay attention on path to test file and path to config (should be same as for trained model)
P.S. You can look at predicted labels now:
vim eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt
5. Generate a report:
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -score -results ./eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt -testFile ../../../SICK/SICK_test.xml
Should write here same test file and same config as in step 4
6. Finally, take a look at report:
vim eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt_report.xml
If you have changed the name of config, the file will be called:
vim eop-resources-1.2.3/results/*your condig name*.xml_results.txt_report.xml


