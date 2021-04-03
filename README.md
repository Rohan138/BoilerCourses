# BoilerCourses
A recommender system to find related courses based on course descriptions and NLP

# Documentation
To run sample, only requirements are Python 3+, numpy, and pandas.

cd BoilerCourses
python run.py

# Example
(base) PS D:\Rohan\Subjects\EECS\Projects\BoilerCourses> python .\run.py<br>
Loading catalog<br>
Loading vectors<br>
Enter course code e.g. (AAE 20300) or q to quit: CS 38100<br>
Enter number of similar courses to find: 5<br>
Similar courses in CS:<br>
      Index    Course School  Number                                            Title                                        Description<br>
2323   2323  CS 18000     CS   18000  Problem Solving And Object-Oriented Programming  problem solving and algorithms implementation ...<br>
2366   2366  CS 47300     CS   47300            Web Information Search And Management  this course teaches important concepts and kno...<br>
2389   2389  CS 52900     CS   52900                               Security Analytics  this course focuses on applied data mining mac...<br>
2391   2391  CS 53100     CS   53100                           Computational Geometry  computational geometry studies how to compute ...<br>
2403   2403  CS 57700     CS   57700                      Natural Language Processing  this course will cover the key concepts and me...<br>
Similar courses not in CS:<br>
      Index      Course School  Number                                          Title                                        Description<br>
69       69   AAE 56000    AAE   56000        System-Of-Systems Modeling And Analysis  introduction to features of systemofsystems pr...<br>
1348   1348   BME 45600    BME   45600  Mathematical Models And Methods In Physiology  teaches principles of mathematical modeling ap...<br>
1816   1816    CE 66100     CE   66100                   Algorithms In Transportation  modeling and analysis of transportation networ...<br>
2577   2577  EAPS 30900   EAPS   30900        Computer-Aided Analysis For Geosciences  application of computer analysis techniques in...<br>
5713   5713   MET 16000    MET   16000      Analytical And Computational Tools In MET  the skills needed to solve technical problems ...<br>
<br>
Enter course code e.g. (AAE 20300) or q to quit: CS 37300<br>
Enter number of similar courses to find: 5<br>
Similar courses in CS:<br>
      Index    Course School  Number                                  Title                                        Description<br>
2333   2333  CS 24200     CS   24200           Introduction To Data Science  stat 24200 this course provides a broad introd...<br>
2366   2366  CS 47300     CS   47300  Web Information Search And Management  this course teaches important concepts and kno...<br>
2389   2389  CS 52900     CS   52900                     Security Analytics  this course focuses on applied data mining mac...<br>
2402   2402  CS 57300     CS   57300                            Data Mining  csci 57300 data mining has emerged at the conf...<br>
2403   2403  CS 57700     CS   57700            Natural Language Processing  this course will cover the key concepts and me...<br>
Similar courses not in CS:<br>
      Index      Course School  Number                                        Title                                        Description<br>
1211   1211  BCHM 61200   BCHM   61200  Bioinformatic Analysis of Genome Scale Data  this course provides a handson experience for ...<br>
2307   2307   CGT 57500    CGT   57500    Data Visualization Tools And Applications  this course provides handson experience in dat...<br>
5195   5195  MGMT 40300   MGMT   40300                  Database Management Systems  intensive study of computerbased tools and met...<br>
5248   5248  MGMT 47900   MGMT   47900                           Data Visualization  or 300 this course is an introduction to the t...<br>
7013   7013  STAT 24200   STAT   24200                 Introduction To Data Science  cs 24200 this course provides a broad introduc...<br>
<br>
