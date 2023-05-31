ECG-Heartbeat-Categorization
==============================

*This project is focused on classifying the heartbeats using deep neural networks. It is made up of electrocardiogram (ECG) data that indicate various heartbeat types. These heartbeats include both healthy and arrhythmic cases. The labels 'N' (0), 'S' (1), 'V' (2), 'F' (3), and 'Q' (4) in this dataset stand in for the classes. These names are associated with various myocardial infarction cases and arrhythmia kinds.*


| Class         | Heart condition                                                                           |
| ------------- | ----------------------------------------------------------------------------------------- |
| 0             | Normal, Left/Right bundle branch block, Atrial escape, Nodal escape.                      |
| 1             | Atrial premature, Aberrant atrial premature, Nodal premature, Supra-ventricular premature |
| 2             | Premature ventricular contraction, Ventricular escape                                     |
| 3             | Fusion of ventricular and norma                                                           |
| 4             | Paced, Fusion of paced and normal, Unclassifiable                                         |


Class	Heart condition
0	    Normal, Left/Right bundle branch block, Atrial escape, Nodal escape
1	    Atrial premature, Aberrant atrial premature, Nodal premature, Supra-ventricular premature
2	    Premature ventricular contraction, Ventricular escape
3	    Fusion of ventricular and norma
4	    Paced, Fusion of paced and normal, Unclassifiable

CNN model has been trained using Tensorflow Framework to classify the heartbest signals into one of the above 5 different categories.


