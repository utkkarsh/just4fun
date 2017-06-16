'''Given the following mapping from number to characters:
1 -> @ [@"a", @"b", @"c"]
2 -> d, e
3 -> f, g
4 -> ...
Write a function to output all the possible permutations generated from the input string.
Example input: 
@"213"
@"13" ==> af ag bf bg cf cg
Output: daf, dag, dbf, dbg, dcf, dcg, eaf, eag, ...
'''
import copy

def mul(pres,my_dict,i):
		new_res=my_dict[num[i]]
		i+=1
		for k in range(len(new_res)):
			for j in range(len(pres)):
				fake.append(new_res[k]+""+pres[j])
		r=copy.deepcopy(fake)
		del fake[:]
		return r	

my_dict={'1':['a','b','c'],'2':['d','e'],'3':['f','g'],'4':['h','i']}
num1=input("Input:")
num=copy.deepcopy(num1[::-1])
res=[];fake=[];flag=0;

for i in range(len(num)):
	if num[i] in my_dict:
		
		if len(res)!=0:
			if flag!=1:
				pres=res;flag=1;
			else:
				pres=temp;flag=1;	
			temp=mul(pres,my_dict,i)

		if len(res)==0:
			res=my_dict[num[i]];i+=1;
				
print(temp)
