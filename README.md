# fuzzy-systems

In this project, our goal is to design a fuzzy expert system for diagnosing heart disease. <br>
The inputs to this problem include the following:
- Chest pain: This entry specifies the degree of chest pain. This input is a crisp input and has only four values, one, two, three, or four. If its value is one, it indicates typical angina, if its value is two, it indicates atypical angina, if its value is three, it indicates non-anginal pain. If its value is four, it means asymptomatic.
- Blood pressure: This entry specifies the blood pressure of the person.
- Cholesterol: This entry specifies the level of cholesterol of the person.
- Blood sugar: This input specifies the blood sugar level of the person.
- ECG is a non-invasive test that can detect abnormalities such as arrhythmias, evidence of coronary heart disease, left ventricular hypertrophy and bundle branch blocks.
- Maximum heart rate: This input shows the maximum heart rate of a person during 24 hours.
- Sports activity: This input is a crisp input and has only two values zero or one. If it is zero, it means that sports activity is not suitable for the person, and if it is one, it means that there is no obstacle for the person.
- Peak Old: This entry specifies the level of depression of the person.
- Thallium amount: This entry specifies the amount of thallium (a chemical element) in a person's body. This entry is also a crisp entry and only takes three values: 3, 6, and 7. If the thallium amount is 3, it is normal, if it is 6, it is average, and if it is 7 is high.
- Gender: This input is also a crisp input and has only two values zero and one. If it is zero, it means that the patient is male, and if it is one, it means that the patient is female.
- Age: This entry specifies the age of the person.
<br> 
Finally, the output determines whether or not a person is suffering from heart disease, which is explained in more detail below.

## Fuzzification
To solve the problem with the help of fuzzy logic, it is necessary to convert our values from absolute to fuzzy (imprecise, relative). This stage is called Fuzzification. For this purpose, fuzzy sets must be defined and according to the membership function, the degree of membership of each value For this purpose, the membership functions of the required sets are shown in the following figures:
### Age
![image](https://user-images.githubusercontent.com/117355603/216841266-fe197815-28a3-4ef0-919d-1b8d93564596.png)
### Blood Pressure
![image](https://user-images.githubusercontent.com/117355603/216841292-a486de49-4b4f-4140-ac4e-81d9ed99b367.png)
### Blood Sugar
![image](https://user-images.githubusercontent.com/117355603/216841304-9952b15f-ec67-4682-88a4-fe7456539828.png)
### Cholestrol
![image](https://user-images.githubusercontent.com/117355603/216841319-f3e72aeb-58d6-4aeb-bdce-ba93fb7cdf36.png)
### Heart Rate
![image](https://user-images.githubusercontent.com/117355603/216841420-e8dc1b20-beca-4523-81cb-7d87551cc72a.png)
### ECG
![image](https://user-images.githubusercontent.com/117355603/216841399-b8df683c-368f-43df-9398-093c4d4e19a3.png)
### Old Peak
![image](https://user-images.githubusercontent.com/117355603/216841472-a8207c75-6da5-435e-9d50-26bca5fde85e.png)
### Sickness
![image](https://user-images.githubusercontent.com/117355603/216841461-e7cf816c-a6a3-43f8-b502-1416c887d99c.png)

## Inference
In the next step, it is necessary to check the fuzzy values obtained in the existing rules to solve the problem. This stage is called Inference. For example, consider the following rules:
- If (age is old ) and (blood pressure is very high) then ( result is sick(s4))
- If (cholesterol is low) and ( blood pressure is low) then ( result is health)
- If (blood pressure is high) and ( max heart rate is medium) then (result is sick(s2))
<br>
As you know, in fuzzy logic, there are different methods for calculating community and sharing operators. Here we use the maximum and minimum method. As a result, min=AND and max=OR.

## Defuzzification
The last step is called Defuzzification. At this stage, we return to the world of absolute values with the help of repeated deductions to obtain the answer as an absolute value. There are various methods for dephasing, one of the most important and widely used of which is the center of mass method.
Please note that in some cases, more than 2 rules may be activated and may belong to several sets of values. In these cases, we must combine the obtained answers. To do this, we OR all the answers together, or in other words, we get the Max output of all the rules. After combining the answers of all the rules, we get the center of mass of the resulting figure.

## Try for yourself!
To install the requirements and used libraries, first enter the main directory and then install the requirements using 
```
piptxt.requirements r -install
```
The structure of the project is as follows:
<br>
![image](https://user-images.githubusercontent.com/117355603/216841872-37284040-97f6-4057-abd2-6cbbe0df9764.png)
<br>
It should be noted that in the given gui, the value of thallium can be set to values other than 3, 6, and 7, but you must enter one of the values 3, 6, and 7 as thallium input, otherwise the output number will be incorrect.







