import os
import nltk
location = 'F:/'
f  = open(os.path.join(location, 'TestLog1.log'), "r")
second_file = f.readlines()
isf  = open(os.path.join(location, 'Functions.sh'), "r")
first_file = isf.readlines()
ranges = []
for i in range(0, len(second_file)):
    if 'This is NuSMV' in second_file[i]:
        ranges.append(i)
correct = []
wrong = []
nones = []
output = []
no_result = []
if len(ranges)==len(first_file):
    ranges.append(len(second_file))

    for i in range(0, len(ranges)-1):
        j=i+1
        tokens = []
        for k in second_file[ranges[i]:ranges[j]]:
            token = words = nltk.word_tokenize(k)
            for t in token:
                tokens.append(t)
        if 'specification' in tokens and 'true' in tokens:
                output.append('True '+first_file[i])
                print('True '+first_file[i])
                correct.append("Ture")
        elif 'specification' in tokens and 'false' in tokens:
                output.append('False '+first_file[i])
                print('False '+ first_file[i])
                wrong.append('Flase')
        else:
                output.append('None '+first_file[i])
                print('None ' + first_file[i])
                nones.append('None')
    output.append("Total True "+str(len(correct)))
    output.append("Total False "+str(len(wrong)))
    output.append("Total None "+str(len(nones)))
    output.append("Total No Result "+str(len(no_result)))
    print("Total True "+str(len(correct)))
    print("Total False "+str(len(wrong)))
    print("Total None "+str(len(no_result)))
    print("Total No Result "+str(len(no_result)))
else:
    dif = len(first_file)-len(ranges)
    no_r = len(ranges)
    ranges.append(len(second_file))
    for i in range(0, len(first_file)-dif):
        j=i+1
        tokens = []
        for k in second_file[ranges[i]:ranges[j]]:
            token = words = nltk.word_tokenize(k)
            for t in token:
                tokens.append(t)
        if 'specification' in tokens and 'true' in tokens:
                output.append('True '+first_file[i])
                print('True '+first_file[i])
                correct.append("Ture")
        elif 'specification' in tokens and 'false' in tokens:
                output.append('False '+first_file[i])
                print('False '+ first_file[i])
                wrong.append('Flase')
        else:
                output.append('None '+first_file[i])
                print('None ' + first_file[i])
                nones.append('None')
    for d in range(0, dif):
        no_result.append('No Result '+first_file[no_r+d])
        print('No Result '+first_file[no_r+d])
        output.append('No Result '+first_file[no_r+d])
    
    output.append("Total True "+str(len(correct)))
    output.append("Total False "+str(len(wrong)))
    output.append("Total None "+str(len(nones)))
    output.append("Total No Result "+str(len(no_result)))
    print("Total True "+str(len(correct)))
    print("Total False "+str(len(wrong)))
    print("Total None "+str(len(nones)))
    print("Total No Result "+str(len(no_result)))
    
with open('output.txt', 'w') as f:
    for item in output:
        f.write("%s\n" % item)   