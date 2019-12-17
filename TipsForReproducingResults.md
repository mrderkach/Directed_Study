# How to run EDITS

1. Go to folder:
```bash
cd  ~/Excitement-Open-Platform-1.2.3/target/EOP-1.2.3/
```

2. Clear the folder where the model will be located
```bash
rm /tmp/EN/dev/*
```

3. Train the model
```bash
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -config ./eop-resources-1.2.3/configuration-files/EditDistanceEDA_EN.xml -train -trainFile ../../../SICK/SICK_train.xml
```
   Here we have to pay attention on path to train file and path to config
   
4. Test the model
```bash
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -config ./eop-resources-1.2.3/configuration-files/EditDistanceEDA_EN.xml -test -testFile ../../../SICK/SICK_test.xml -output ./eop-resources-1.2.3/results/
```
   Again, pay attention on path to test file and path to config (should be same as for trained model)
   
   P.S. You can look at predicted labels now:
```bash
vim eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt
```

5. Generate a report:
```bash
java -Djava.ext.dirs=../EOP-1.2.3/ eu.excitementproject.eop.util.runner.EOPRunner -score -results ./eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt -testFile ../../../SICK/SICK_test.xml
```
   Should write here same test file and same config as in step 4
   
6. Finally, take a look at report:
```bash
vim eop-resources-1.2.3/results/EditDistanceEDA_EN.xml_results.txt_report.xml
```
   If you have changed the name of config, the file will be called:
```bash
vim eop-resources-1.2.3/results/*your condig name*.xml_results.txt_report.xml
```

# Config file

* To take a look at a config file:
```bash
vim ./eop-resources-1.2.3/configuration-files/EditDistanceEDA_EN.xml
```
* If you want to train a different model, change the path to the folder with model location (lines 135-138).
```bash
        <!-- <property name="trainDir">/tmp/</property> -->
        <property name="trainDir">/tmp/EN/dev/</property>
        <!-- <property name="testDir">/tmp/</property> -->
        <property name="testDir">/tmp/EN/test</property>
```
   It is probably safer to change the path at EN level, e.g. `/tmp/EN_new_model/dev/`
   
# Edits: installation

* How to install JDK:
https://thishosting.rocks/install-java-ubuntu/

* Helpful links:
   Compiling tools jar not found
https://stackoverflow.com/questions/29234759/fatal-error-compiling-tools-jar-not-found-maven-compiler-plugin/33273932

   java_home not defined
https://stackoverflow.com/questions/27319495/error-java-home-is-not-defined-correctly-executing-maven

   If you get an error: "Unrecognized option: - Could not create the Java virtual machine", check your command spelling and parameters in it
